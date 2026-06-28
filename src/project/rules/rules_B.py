B_WORDS = [
    "怖い",
    "こわい",
    "すごい",
    "尊敬",
    "プロすぎ",
    "差別",
    "時代",
    "害獣",
    "ハラハラ",
    "危険すぎる",
    "最悪すぎる",
    "馬鹿馬鹿しい",
    "危機感なさすぎる"
]

def score_B(text):
    return sum(
        1 for w in B_WORDS
        if w in text
    )