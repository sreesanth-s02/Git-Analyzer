from datetime import datetime

def calculate_score(repos):
    score = 0

    # -------------------------
    # 1. Project Quality (30)
    # -------------------------
    if len(repos) >= 5:
        score += 30
    elif len(repos) >= 2:
        score += 15

    # -------------------------
    # 2. Activity Recency (15)
    # -------------------------
    recent_count = 0
    for repo in repos:
        updated = repo["updated_at"]
        updated_date = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%SZ")

        if (datetime.now() - updated_date).days < 90:
            recent_count += 1

    if recent_count > 3:
        score += 15
    elif recent_count > 0:
        score += 8

    # -------------------------
    # 3. Code Depth (20)
    # -------------------------
    size_total = sum(repo["size"] for repo in repos)

    if size_total > 5000:
        score += 20
    elif size_total > 1000:
        score += 10

    # -------------------------
    # 4. Consistency (20)
    # -------------------------
    if len(repos) > 3:
        score += 20
    else:
        score += 10

    # -------------------------
    # 5. Collaboration (15)
    # -------------------------
    forked = sum(1 for repo in repos if repo["fork"])

    if forked > 2:
        score += 15
    elif forked > 0:
        score += 8

    return score


# ✅ NEW: Category
def get_category(score):
    if score >= 80:
        return "Job Ready"
    elif score >= 50:
        return "Needs Improvement"
    else:
        return "Not Ready"