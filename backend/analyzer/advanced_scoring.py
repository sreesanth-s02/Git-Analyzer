def calculate_depth_score(repos):
    total_size = sum(repo["size"] for repo in repos)
    total_repos = len(repos)

    if total_repos == 0:
        return 0

    avg_size = total_size / total_repos

    # 🎯 Logic
    if avg_size > 1500:
        return 90
    elif avg_size > 500:
        return 70
    elif avg_size > 100:
        return 50
    else:
        return 30
def calculate_authenticity_score(repos):
    total = len(repos)

    if total == 0:
        return 0

    forked = sum(1 for repo in repos if repo["fork"])
    empty = sum(1 for repo in repos if repo["size"] == 0)

    fork_ratio = forked / total
    empty_ratio = empty / total

    score = 100

    # ❌ Penalize bad patterns
    if fork_ratio > 0.7:
        score -= 40
    elif fork_ratio > 0.4:
        score -= 20

    if empty_ratio > 0.5:
        score -= 30
    elif empty_ratio > 0.2:
        score -= 15
    if fork_ratio < 0.2:
        score += 0
    elif fork_ratio < 0.5:
        score -= 20
    else:
        score -= 40
    if total <3:
        score -= 20

    return max(score, 0)
from datetime import datetime

def calculate_consistency_score(repos):
    recent = 0

    for repo in repos:
        updated = datetime.strptime(repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ")

        if (datetime.now() - updated).days < 90:
            recent += 1

    if recent > 5:
        return 90
    elif recent > 2:
        return 70
    elif recent > 0:
        return 50
    else:
        return 20