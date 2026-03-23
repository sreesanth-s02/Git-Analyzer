from datetime import datetime

def detect_empty_repos(repos):
    return sum(1 for repo in repos if repo["size"] == 0)


def detect_forked_repos(repos):
    return sum(1 for repo in repos if repo["fork"])


# ✅ NEW: Activity Status
def get_activity_status(repos):
    recent = 0

    for repo in repos:
        updated = repo["updated_at"]
        updated_date = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%SZ")

        if (datetime.now() - updated_date).days < 30:
            recent += 1

    if recent > 3:
        return "Active"
    elif recent > 0:
        return "Moderate"
    else:
        return "Inactive"


# ✅ NEW: Strengths & Weaknesses
def get_insights(repos, empty_count, fork_count):
    strengths = []
    weaknesses = []

    if len(repos) >= 5:
        strengths.append("Good number of projects")
    else:
        weaknesses.append("Less number of projects")

    if empty_count == 0:
        strengths.append("No empty repositories")
    else:
        weaknesses.append("Contains empty repositories")

    if fork_count > 2:
        weaknesses.append("Too many forked repositories")
    else:
        strengths.append("Original work present")

    return strengths, weaknesses