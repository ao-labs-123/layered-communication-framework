A_WORDS = [
    "と思ったら",
    "はずなのに",
    "なのに",
    "逆だろ",
    "聞いてた話と違う"
]

def score_A(text):
    return sum(
        1 for w in A_WORDS
        if w in text
    )