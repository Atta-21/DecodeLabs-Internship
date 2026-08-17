from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
data = pd.read_csv(BASE_DIR / "student_performance.csv")

for label, group in data.groupby("result"):
    plt.scatter(
        group["study_hours_per_day"],
        group["assignment_score"],
        label=label
    )

plt.xlabel("Study Hours Per Day")
plt.ylabel("Assignment Score")
plt.title("Student Performance Dataset")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / "dataset_visualization.png", dpi=150)
plt.show()
