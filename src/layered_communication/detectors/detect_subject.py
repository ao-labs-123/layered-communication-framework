from project.rules.subject_rules import SUBJECT_RULES

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


from detect_subject import detect_subject
from detect_stance import detect_stance
from detect_layer import detect_layer

text = "ここまで同じタイミングで一斉に街に流れ出てるの凄いな。ただ熊被害で亡くなる人が増える前に対策してほしい"

print(detect_subject(text))
print(detect_stance(text))
print(detect_layer(text))
