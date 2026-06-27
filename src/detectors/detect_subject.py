from src.project.ontology.subject_rules import SUBJECT_RULES

def detect_subject(text):

    scores = {}

    for subject, keywords in SUBJECT_RULES.items():

        score = 0

        for keyword in keywords:
            if keyword in text:
                score += 1

        scores[subject] = score

    if max(scores.values()) == 0:
        return "不明"

    return max(scores, key=scores.get)

print(detect_subject("一般人にクマの駆除をお願いする以上、危険手当を手厚くして十分な報酬を出すべき。"))

