B_WORDS = [
    "怖い",
    "危険",
    "すごい",
    "尊敬",
    "ハラハラ"
]

def score_B(text):
    return sum(
        1 for w in B_WORDS
        if w in text
    )