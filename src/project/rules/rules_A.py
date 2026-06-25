A_WORDS = [
    "怖い",
    "危険",
    "すごい",
    "尊敬",
    "ハラハラ"
]

def score_A(text):
    return sum(
        1 for w in A_WORDS
        if w in text
    )