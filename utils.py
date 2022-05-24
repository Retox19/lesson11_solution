import json
from pprint import pprint as pp

PATH = "templates/data/candidates.json"


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""

    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_all_candidates():
    candidates = load_candidates_from_json(path=PATH)
    return candidates


def get_candidate_by_id(candidate_id):
    """возвращает одного кандидата по его id"""

    candidates = load_candidates_from_json(path=PATH)
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json(path=PATH)
    candidates_found = []

    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""

    skill_name = skill_name.lower()
    candidates = load_candidates_from_json(path=PATH)
    candidates_found = []

    for candidate in candidates:
        skills = candidate.get("skills")
        list_of_skills = skills.lower().split(", ")
        if skill_name in list_of_skills:
            candidates_found.append(candidate)
    return candidates_found
