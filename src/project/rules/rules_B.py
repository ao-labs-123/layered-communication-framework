B_WORDS = [
    "怖い",
    "こわい",
    "すごい",
    "尊敬",
    "差別",
    "ハラハラ",
    "最悪すぎる",
    "馬鹿馬鹿しい",
    "危機感なさすぎる"
]

def score_B(text):
    return sum(
        1 for w in B_WORDS
        if w in text
    )