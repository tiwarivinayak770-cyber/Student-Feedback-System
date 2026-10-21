from pathlib import Path
import pandas as pd

# Go to the project root
BASE_DIR = Path(__file__).resolve().parent.parent

# datasets folder
DATASET_DIR = BASE_DIR / "datasets"

files = [
    "students_part1_1000 (1).csv",
    "faculty_part2 (2).csv",
    "subjects_part2 (1).csv",
    "feedback_5000 (1).csv"
]

for file in files:
    print("=" * 60)
    print("File:", file)

    df = pd.read_csv(DATASET_DIR / file)

    print("Columns:")
    print(df.columns.tolist())