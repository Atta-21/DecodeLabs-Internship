from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ------------------------------------------------------------
# DecodeLabs - Artificial Intelligence Project 2
# Data Classification Using AI
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "student_performance.csv"


def load_dataset():
    """Read the small classification dataset."""
    data = pd.read_csv(DATA_FILE)
    return data


def prepare_data(data):
    """Separate input features from the target column."""
    features = data[
        ["study_hours_per_day", "attendance_percent", "assignment_score"]
    ]
    target = data["result"]

    return features, target


def train_model(features, target):
    """Split the data and train a simple Decision Tree model."""
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.25,
        random_state=42,
        stratify=target
    )

    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(x_train, y_train)

    return model, x_train, x_test, y_train, y_test


def evaluate_model(model, x_test, y_test):
    """Show the basic evaluation results."""
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n---------------- MODEL RESULTS ----------------")
    print(f"Testing records : {len(x_test)}")
    print(f"Accuracy        : {accuracy:.2%}")

    print("\nClassification report:")
    print(classification_report(y_test, predictions, zero_division=0))

    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))
    print("-----------------------------------------------")

    return accuracy


def predict_new_student(model):
    """Let the user try the trained classifier on new values."""
    print("\nTry the model with a new student.")
    print("Enter numbers only. Type 'skip' to finish.")

    while True:
        first = input("\nStudy hours per day: ").strip()

        if first.lower() == "skip":
            break

        try:
            study_hours = float(first)
            attendance = float(input("Attendance percentage: "))
            assignment = float(input("Assignment score: "))

            new_student = pd.DataFrame([{
                "study_hours_per_day": study_hours,
                "attendance_percent": attendance,
                "assignment_score": assignment
            }])

            prediction = model.predict(new_student)[0]
            probabilities = model.predict_proba(new_student)[0]
            confidence = probabilities.max()

            print(f"Predicted result: {prediction}")
            print(f"Model confidence: {confidence:.2%}")

        except ValueError:
            print("Please enter valid numeric values.")


def main():
    print("=" * 60)
    print("        DECODELABS - PROJECT 2")
    print("          DATA CLASSIFICATION USING AI")
    print("=" * 60)

    try:
        data = load_dataset()
    except FileNotFoundError:
        print("Dataset file was not found.")
        return

    print(f"\nDataset loaded: {len(data)} records")
    print("\nFirst five records:")
    print(data.head())

    features, target = prepare_data(data)

    print("\nTarget classes:")
    print(target.value_counts())

    model, x_train, x_test, y_train, y_test = train_model(features, target)

    print(f"\nTraining records: {len(x_train)}")
    print(f"Testing records : {len(x_test)}")

    evaluate_model(model, x_test, y_test)

    # Optional user prediction after the evaluation.
    predict_new_student(model)


if __name__ == "__main__":
    main()
