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

print(detect_subject("吹き矢を受けても全然気にせずリンゴ食ってて笑った。こいつ駆除しないと来年も絶対このリンゴ園に来るわ"))

