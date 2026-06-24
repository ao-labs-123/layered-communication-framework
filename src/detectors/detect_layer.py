from project.rules.rules_A import RULES_A
from project.rules.rules_B import RULES_B
from project.rules.rules_C import RULES_C

def detect_layer(text):

    score_A = sum(1 for x in RULES_A if x in text)
    score_B = sum(1 for x in RULES_B if x in text)
    score_C = sum(1 for x in RULES_C if x in text)

    scores = {
        "A": score_A,
        "B": score_B,
        "C": score_C
    }

    return max(scores, key=scores.get)
