from src.project.ontology.stance_rules import STANCE_RULES

def detect_stance(text):

    scores = {}

    for stance, words in STANCE_RULES.items():
        scores[stance] = sum(
            1 for word in words
            if word in text
        )

    if max(scores.values()) == 0:
        return "不明"

    return max(scores, key=scores.get)
    
    
print(detect_stance("ちょっと待て、殺さずに眠らせたまま運ぶんかいwこの工程すんの怖すぎるだろw"))

