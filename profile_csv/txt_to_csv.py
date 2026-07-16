import os
import pandas as pd

CSV_DIR = "/Users/igeondong/KCL/Project/Profiles/profile_csv"


def txt_to_csv(x: str) -> None:
    df = pd.read_csv(x, sep="\t", header=0)

    filename = os.path.splitext(os.path.basename(x))[0]
    out_path = os.path.join(CSV_DIR, f"{filename}.csv")

    df.to_csv(out_path, index=False)
    print(f"Saved: {out_path}")
