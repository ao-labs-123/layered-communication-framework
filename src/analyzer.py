# analyzer.py

import pandas as pd

from detect_layer import detect_layer
from detect_subject import detect_subject
from detect_stance import detect_stance


INPUT_FILE = "comments.csv"
OUTPUT_FILE = "analysis_output.csv"


def analyze_comment(text):
    """1件のコメントを解析"""

    return {
        "layer": detect_layer(text),
        "subject": detect_subject(text),
        "stance": detect_stance(text)
    }


def main():

    df = pd.read_csv(INPUT_FILE)

    results = []

    for _, row in df.iterrows():

        text = str(row["comment"])

        result = analyze_comment(text)

        results.append({
            "id": row["id"],
            "video_id": row["video_id"],
            "comment": text,
            "layer": result["layer"],
            "subject": result["subject"],
            "stance": result["stance"]
        })

    output_df = pd.DataFrame(results)

    output_df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Saved {len(output_df)} comments to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

