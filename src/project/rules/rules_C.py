C_WORDS = [
    "してほしい",
    "しろ",
    "法改正",
    "対応",
    "熊を減らさないと",
    "駆除",
    "法律変えろ"
]

def score_C(text):
    return sum(
        1 for w in C_WORDS
        if w in text
    )