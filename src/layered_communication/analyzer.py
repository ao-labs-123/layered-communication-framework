import pandas as pd

from rules.rules_B import analyze_B
from rules.rules_C import analyze_C

df = pd.read_csv("data/comments_raw.csv")

results = []

for _, row in df.iterrows():

    comment = row["comment"]

    result_B = analyze_B(comment)
    result_C = analyze_C(comment)

    results.append({
        "id": row["id"],
        "video_id": row["video_id"],
        "comment": comment,
        "B_score": result_B["score"],
        "C_score": result_C["score"],
        "layer": result_B["layer"]
    })
