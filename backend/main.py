from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.analyzer.github_api import get_user_repos
from backend.analyzer.scoring import calculate_score, get_category
from backend.analyzer.edge_cases import (
    detect_empty_repos,
    detect_forked_repos,
    get_activity_status,
    get_insights
)
from backend.analyzer.advanced_scoring import (
    calculate_depth_score,
    calculate_authenticity_score,
    calculate_consistency_score
)
from backend.analyzer.features import extract_languages, calculate_relevance
from backend.analyzer.role_insights import generate_role_insights


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Recruitability API Running"}


# 🔥 UPDATED: added mode parameter
@app.get("/analyze/{username}")
def analyze(username: str, role: str = "frontend", mode: str = "student"):

    repos = get_user_repos(username)

    if isinstance(repos, dict) and repos.get("message"):
        return {"error": "User not found"}

    # -------------------------
    # 🔹 QUALITY SCORE
    # -------------------------
    quality_score = calculate_score(repos)

    # -------------------------
    # 🔹 FEATURE EXTRACTION
    # -------------------------
    languages = extract_languages(repos)
    relevance = calculate_relevance(languages, role)

    depth_score = calculate_depth_score(repos)
    authenticity_score = calculate_authenticity_score(repos)
    consistency_score = calculate_consistency_score(repos)

    # -------------------------
    # 🔹 EDGE CASES
    # -------------------------
    empty = detect_empty_repos(repos)
    forks = detect_forked_repos(repos)
    activity = get_activity_status(repos)

    # -------------------------
    # 🔹 GENERAL INSIGHTS
    # -------------------------
    general_strengths, general_weaknesses = get_insights(repos, empty, forks)

    # -------------------------
    # 🔹 ROLE-BASED INSIGHTS
    # -------------------------
    role_strengths, role_weaknesses = generate_role_insights(
        languages, role, relevance
    )

    # -------------------------
    # 🔹 MERGE INSIGHTS
    # -------------------------
    strengths = general_strengths + role_strengths
    weaknesses = general_weaknesses + role_weaknesses

    # -------------------------
    # 🔹 FINAL SCORE (HYBRID)
    # -------------------------
    final_score = (
        0.25 * quality_score +
        0.35 * relevance +
        0.15 * depth_score +
        0.15 * consistency_score +
        0.1 * authenticity_score
    )

    final_score = round(final_score, 2)

    # -------------------------
    # 🔹 CATEGORY
    # -------------------------
    category = get_category(final_score)

    # =========================================================
    # 🔥 🔥 🔥 DUAL MODE LOGIC STARTS HERE 🔥 🔥 🔥
    # =========================================================

    # 👨‍🎓 STUDENT MODE
    if mode == "student":
        return {
            "username": username,
            "mode": mode,
            "role": role,
            "quality_score": quality_score,
            "relevance_score": relevance,
            "depth_score": depth_score,
            "consistency_score": consistency_score,
            "authenticity_score": authenticity_score,
            "final_score": final_score,
            "languages": list(languages.keys()),
            "category": category,
            "empty_repos": empty,
            "forked_repos": forks,
            "recent_activity": activity,
            "strengths": strengths,
            "weaknesses": weaknesses
        }

    # 🧑‍💼 RECRUITER MODE
    elif mode == "recruiter":

        # 🔹 Hire decision logic
        if final_score >= 80:
            hire_decision = "Strong Hire"
        elif final_score >= 60:
            hire_decision = "Consider"
        else:
            hire_decision = "Reject"

        # 🔹 Risk level
        if final_score >= 75:
            risk_level = "Low"
        elif final_score >= 50:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "username": username,
            "mode": mode,
            "role": role,
            "final_score": final_score,
            "category": category,
            "hire_decision": hire_decision,
            "risk_level": risk_level,
            "summary": f"Candidate shows {category.lower()} readiness with a score of {final_score}"
        }

    # 🔹 fallback (safety)
    return {"error": "Invalid mode. Use 'student' or 'recruiter'"}


# -------------------------
# 🔹 CORS CONFIG
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)