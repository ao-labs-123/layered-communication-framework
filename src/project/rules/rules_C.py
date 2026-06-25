C_WORDS = [
    "してほしい",
    "しろ",
    "法改正",
    "対応",
    "駆除"
]

def score_C(text):
    return sum(
        1 for w in C_WORDS
        if w in text
    )