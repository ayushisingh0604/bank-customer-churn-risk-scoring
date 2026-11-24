# Machine Learning Model Evaluation

## Models Evaluated

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost

## Performance Comparison

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 70.95% | 38.28% | 69.78% | 49.43% |
| Decision Tree | 66.95% | 45.47% | 73.96% | 56.13% |
| Random Forest | 83.75% | 58.76% | 67.57% | 62.86% |
| Gradient Boosting | 86.75% | 77.10% | 49.63% | 60.39% |
| XGBoost | 86.95% | 78.97% | 48.89% | 60.40% |

## Champion Model

Gradient Boosting

ROC-AUC: 0.8659

## Confusion Matrix

| | Predicted Retained | Predicted Churn |
|---|---:|---:|
| Actual Retained | 1533 | 60 |
| Actual Churn | 205 | 202 |

## Interpretation

Gradient Boosting achieved the highest reported ROC-AUC.

XGBoost achieved the highest accuracy and precision.

Random Forest achieved the highest recall and F1-score.

The final model selection was based on ROC-AUC.
