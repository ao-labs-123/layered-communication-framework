import pandas as pd

from rules.rules_B import analyze_B
from rules.rules_C import analyze_C

df = pd.read_csv("data/comments_raw.csv")

results = []

for _, row in df.iterrows():

    comment = row["comment"]

    result_B = analyze_B(text)
    result_C = analyze_C(text)

    results.append({
        "id": row["id"],
        "video_id": row["video_id"],
        "comment": comment,
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
