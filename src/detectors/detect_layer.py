from src.project.rules.rules_A import A_WORDS
from src.project.rules.rules_B import B_WORDS
from src.project.rules.rules_C import C_WORDS

def detect_layer(text):

    score_A = sum(1 for x in A_WORDS if x in text)
    score_B = sum(1 for x in B_WORDS if x in text)
    score_C = sum(1 for x in C_WORDS if x in text)

    scores = {
        "A": score_A,
        "B": score_B,
        "C": score_C
    }

    return max(scores, key=scores.get)

print(detect_layer("日の出町、あきる野よく行くけど山でなく街に出て来たら本当に危険!早く対応してもらわないと取り返しつかなくなる..."))