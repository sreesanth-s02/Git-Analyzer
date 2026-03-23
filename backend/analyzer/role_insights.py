from backend.analyzer.role_config import ROLE_TECH


def generate_role_insights(languages, role, relevance_score):
    strengths = []
    weaknesses = []

    required_tech = ROLE_TECH.get(role.lower(), [])

    # 🔹 Convert languages dict to set
    user_tech = set(languages.keys())

    # -------------------------
    # 1. Relevance-based insight
    # -------------------------
    if relevance_score > 70:
        strengths.append(f"Strong alignment with {role} role")
    elif relevance_score > 40:
        strengths.append(f"Moderate alignment with {role} role")
        weaknesses.append(f"Can improve skills for {role}")
    else:
        weaknesses.append(f"Low alignment with {role} role")

    # -------------------------
    # 2. Missing technologies
    # -------------------------
    missing = []

    for tech in required_tech:
        if tech not in user_tech:
            missing.append(tech)

    if missing:
        weaknesses.append(f"Missing key technologies: {', '.join(missing)}")
        weaknesses.append(f"Recommended to learn: {', '.join(missing[:2])}")
    else:
        strengths.append("Covers all key technologies for the role")

    # -------------------------
    # 3. Tech diversity bonus
    # -------------------------
    if len(user_tech) > 5:
        strengths.append("Good technology diversity")

    return strengths, weaknesses