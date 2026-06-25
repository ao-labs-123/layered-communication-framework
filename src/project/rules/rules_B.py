B_WORDS = [
    "と思ったら",
    "はずなのに",
    "なのに",
    "逆だろ",
    "聞いてた話と違う"
]

def score_B(text):
    return sum(
        1 for w in B_WORDS
        if w in text
    )