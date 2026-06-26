B_WORDS = [
    "怖い",
    "危険",
    "すごい",
    "尊敬",
    "ハラハラ",
    "馬鹿馬鹿しい",
    "危機感なさすぎる"
]

def score_B(text):
    return sum(
        1 for w in B_WORDS
        if w in text
    )