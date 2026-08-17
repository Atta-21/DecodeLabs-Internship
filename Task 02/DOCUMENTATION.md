# Project 2 Documentation

## 1. Objective

The aim of this project is to demonstrate a basic supervised-learning classification pipeline.

The DecodeLabs brief asks the intern to load and understand a dataset, split it into training and testing sets, and apply a simple classification algorithm. This implementation follows those three requirements.

## 2. Problem

The model predicts whether a student is likely to be classified as **Pass** or **Fail** using:

- Study hours per day
- Attendance percentage
- Assignment score

## 3. Dataset preparation

A small dataset was prepared specifically for this demonstration. It contains numeric input features and a categorical target.

The target column is `result`.

## 4. Train/test split

The data is split into two parts:

- Training data: 75%
- Testing data: 25%

The model only learns from the training portion. The testing portion is kept separate so that we can check how the trained model performs on records it did not train on.

## 5. Classification algorithm

The project uses `DecisionTreeClassifier` from scikit-learn.

A decision tree makes predictions by learning simple decision boundaries from the training data. It is a useful first classification algorithm because its general idea is easier to understand than a more complex model.

## 6. Model training

The classifier is fitted using:

- `x_train` as the input features
- `y_train` as the target labels

After training, the model can predict the class of unseen records.

## 7. Evaluation

The model is evaluated with the test set.

### Accuracy

Accuracy tells us the proportion of test predictions that were correct.

### Classification report

The report gives precision, recall and F1-score for each class.

### Confusion matrix

The confusion matrix shows how many Pass and Fail records were classified correctly or incorrectly.

## 8. New prediction

After evaluation, the program allows the user to enter a new student's:

- Study hours
- Attendance
- Assignment score

The trained model then returns a predicted class and its highest class probability.

## 9. Limitations

The dataset is intentionally small and created for learning. The model should not be treated as a real student assessment system.

The classification result depends on the quality and size of the training data. A larger real-world dataset would be needed for a reliable practical system.

## 10. Future improvements

Possible next steps include:

- Comparing Decision Tree with Logistic Regression or KNN
- Trying different train/test ratios
- Cross-validation
- Feature scaling where required
- Hyperparameter tuning
- Adding a larger real-world dataset
- Creating a simple GUI
- Saving the trained model for later predictions
