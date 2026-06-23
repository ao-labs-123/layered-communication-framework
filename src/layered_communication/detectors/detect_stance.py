from project.rules.stance_rules import STANCE_RULES

def detect_stance(text):

    scores = {}

    for stance, keywords in STANCE_RULES.items():

        scores[stance] = sum(
            1 for keyword in keywords
            if keyword in text
        )

    if max(scores.values()) == 0:
        return "分析"

    return max(scores, key=scores.get)

print(detect_stance("怖い"))
    

