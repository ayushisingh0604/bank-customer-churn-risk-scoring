# bank-customer-churn-risk-scoring
Predictive modeling a# 🏦 Bank Customer Churn Prediction & Risk Scoring

### Predictive Analytics | Machine Learning | Financial Analysis | Customer Retention

<p align="center">
  <b>An End-to-End Machine Learning Project for Predicting Bank Customer Churn</b>
</p>

---

## 📌 Project Overview

Customer retention is one of the major challenges faced by banking institutions.

This project develops a machine learning-based predictive framework to identify bank customers who are likely to leave the institution.

The objective is to transform customer data into actionable insights through exploratory data analysis, feature engineering, predictive modeling, customer risk scoring, and financial scenario analysis.

Five machine learning algorithms were developed and evaluated to identify the most suitable predictive model.

The final model generates customer churn probabilities that are converted into risk categories to support customer retention strategies.

---

## 🎯 Project Objectives

- Understand customer churn patterns.
- Perform exploratory data analysis.
- Clean and preprocess customer data.
- Develop meaningful predictive features.
- Build multiple machine learning models.
- Compare model performance.
- Identify customers with higher churn probabilities.
- Develop a customer risk-scoring framework.
- Analyze potential financial implications.
- Provide actionable business recommendations.

---

## 📊 Dataset Overview

| Metric | Value |
|---|---:|
| Total Customer Records | 10,000 |
| Original Features | 14 |
| Customers Exited | 2,037 |
| Customers Retained | 7,963 |
| Churn Rate | 20.37% |
| Retention Rate | 79.63% |
| Target Variable | Exited |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data manipulation |
| NumPy | Numerical analysis |
| Matplotlib | Data visualization |
| Seaborn | Exploratory analysis |
| Scikit-learn | Machine learning |
| XGBoost | Predictive modeling |
| Google Colab | Development environment |
| Microsoft Excel | Data analysis |
| Microsoft Word | Documentation |
| GitHub | Project management |

---

## 🔍 Project Methodology

### 1. Data Exploration

- Dataset inspection
- Data quality assessment
- Churn distribution analysis
- Exploratory data analysis
- Identification of important patterns

### 2. Data Cleaning

- Missing-value assessment
- Data preparation
- Feature validation
- Dataset organization

### 3. Feature Engineering

Four additional features were developed:

- BalanceSalaryRatio
- ProductDensity
- EngagementProduct
- AgeTenureInteraction

### 4. Data Preprocessing

- Categorical encoding
- Numerical scaling
- Stratified train-test split
- Class weighting

### 5. Model Development

Five machine learning algorithms were implemented:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost

### 6. Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

### 7. Customer Risk Scoring

Predicted churn probabilities were classified into four risk categories.

| Risk Category | Probability |
|---|---|
| 🟢 Low | Below 30% |
| 🟡 Medium | 30% – Below 60% |
| 🟠 High | 60% – Below 80% |
| 🔴 Critical | 80% and Above |

*Risk thresholds are project-defined analytical categories.*

---

## 🏆 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 70.95% | 38.28% | 69.78% | 49.43% | 77.59% |
| Decision Tree | 66.95% | 45.47% | 73.96% | 56.13% | N/A |
| Random Forest | 83.75% | 58.76% | 67.57% | 62.86% | 86.45% |
| Gradient Boosting | 86.75% | 77.10% | 49.63% | 60.39% | 86.59% |
| XGBoost | 86.95% | 78.97% | 48.89% | 60.40% | 86.37% |

### Selected Champion Model

**Gradient Boosting**

- Accuracy: 86.75%
- Precision: 77.10%
- Recall: 49.63%
- F1 Score: 60.39%
- ROC-AUC: 86.59%

Gradient Boosting was selected based on its highest reported ROC-AUC score.

---

## 💼 Business & Financial Analysis

The project connects machine learning predictions with practical business applications.

Key areas include:

- Customer risk segmentation
- High-risk customer identification
- Customer prioritization
- Retention campaign planning
- Financial scenario analysis
- Retention strategy recommendations

The financial scenarios are illustrative and are not actual campaign results.

---

## 📁 Repository Contents

| File | Description |
|---|---|
| Bank_Customer_Churn_Prediction_Day_1.ipynb | Data exploration and initial analysis |
| Bank_Churn_Day2_ModelBuilding_.ipynb | Model development and evaluation |
| Bank_Churn_Cleaned (1).csv | Cleaned customer dataset |
| Final Portfolio PDF | Complete project portfolio |
| Project Report PDF | Project documentation |
| Research Paper PDF | Research paper |

---

## 📈 Key Findings

- The dataset contains a customer churn rate of 20.37%.
- Gradient Boosting achieved the highest reported ROC-AUC.
- XGBoost achieved the highest reported accuracy.
- Random Forest achieved the highest reported recall and F1-score.
- Probability-based risk segmentation provides a structured way to prioritize retention efforts.

---

## ⚠️ Project Limitations

- The analysis uses a single supplied dataset.
- Model performance may vary across banking populations.
- The classification threshold affects precision and recall.
- Risk categories require business validation.
- Financial scenarios use hypothetical assumptions.
- Further validation is necessary before real-world deployment.

---

## 👩‍💻 Author

**Ayushi Singh**

M.Com Graduate

Areas of Interest:
- Financial Analysis
- Business Analytics
- Machine Learning
- Predictive Modeling
- Financial Reporting

**Internship Organization:** Unified Mentor

**Project:** Bank Customer Churn Prediction & Risk Scoring

---

⭐ Thank you for exploring this project!nd risk scoring for bank customer churn using machine learning, customer analytics, and retention-focused business insights.
