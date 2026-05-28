import pandas as pd

from rules.rules_B import analyze_B
from rules.rules_C import analyze_C

df = pd.read_csv("data/comments.csv")

results = []

for _, row in df.iterrows():

    text = row["text"]

    result_B = analyze_B(text)
    result_C = analyze_C(text)

    results.append({
        "comment_id": row["comment_id"],
        "video_id": row["video_id"],
        "text": text,
        "B_score": result_B["score"],
        "C_score": result_C["score"],
        "layer": result_B["layer"]
    })

output_df = pd.DataFrame(results)

output_df.to_csv(
    "data/analysis_output.csv",
    index=False,
    encoding="utf-8-sig"
)

print("analysis_output.csv generated")
