def extract_languages(repos):
    language_count = {}

    for repo in repos:
        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1

    return language_count
from backend.analyzer.role_config import ROLE_TECH

def calculate_relevance(languages, role):
    required_tech = ROLE_TECH.get(role.lower(), [])

    if not required_tech:
        return 0

    total = sum(languages.values())
    score = 0

    for tech in required_tech:
        if tech in languages:
            weight = languages[tech] / total
            score += weight * 100

    return round(score, 2)