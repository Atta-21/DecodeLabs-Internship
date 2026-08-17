# DecodeLabs Project 2 — Data Classification Using AI

## Project idea

This project is a small supervised-learning classification example. It uses a student-performance dataset and trains a Decision Tree to classify a student's result as **Pass** or **Fail**.

The project follows the main requirements from the DecodeLabs Project 2 brief:

- Load and understand a dataset
- Split the data into training and testing sets
- Apply a simple classification algorithm

The brief describes Project 2 as the predictive phase and focuses on supervised learning, model training, testing and validation.

## Files

```text
DecodeLabs_Project2_Classification/
│
├── classification_model.py
├── student_performance.csv
├── visualize_data.py
├── README.md
├── DOCUMENTATION.md
├── SUBMISSION_CHECKLIST.md
└── .gitignore
```

## Dataset

The included dataset is a small project-specific dataset with these columns:

- `study_hours_per_day`
- `attendance_percent`
- `assignment_score`
- `result`

The target is `result`, with two classes:

- Pass
- Fail

## Algorithm

A **Decision Tree Classifier** is used because it is simple to understand and suitable for a small classification example.

The model is limited to a depth of 3 so that the example stays relatively easy to inspect.

## Training and testing

The dataset is divided using `train_test_split`.

- 75% → training
- 25% → testing

`random_state=42` is used so the split is repeatable.

## Evaluation

The program prints:

- Test-set accuracy
- Classification report
- Confusion matrix

It also allows a new student record to be entered so the trained model can produce a prediction.

## Installation

Use Python 3.x and install:

```text
pip install pandas scikit-learn matplotlib
```

## Run

```text
python classification_model.py
```

For the optional graph:

```text
python visualize_data.py
```

## Important note

This is a learning project using a small custom dataset. Its purpose is to demonstrate the classification workflow, not to make real academic decisions about students.
