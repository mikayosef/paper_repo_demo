% Binary Classification of Iris Species using Random Forest
% Research Team
% March 19, 2026

# Abstract

This paper presents a comprehensive machine learning pipeline for binary classification of iris species using the classic Iris dataset. We employ a Random Forest classifier with optimized hyperparameters to distinguish between *Iris setosa* (class 0) and *Iris versicolor* (class 1). Our model achieves exceptional performance with 100% accuracy, precision, recall, and AUC (Area Under Curve) on the test set.

**Keywords:** machine learning, random forest, binary classification, iris classification

---

# 1. Introduction

The Iris dataset is a classic machine learning dataset containing 150 samples of iris flowers with 4 features. This work focuses on binary classification of two iris species: *Iris setosa* and *Iris versicolor*.

# 2. Materials and Methods

## 2.1 Dataset

The Iris dataset comprises 100 samples for binary classification (classes 0 and 1). Features include:
- Sepal length
- Sepal width  
- Petal length
- Petal width

## 2.2 Data Preprocessing

- **Train-Test Split:** 80/20 stratified split (80 training, 20 test)
- **Feature Standardization:** Z-score normalization applied

## 2.3 Model Architecture

**Algorithm:** Random Forest Classifier

Hyperparameters:
- n_estimators: 100
- max_depth: 10
- min_samples_split: 5
- min_samples_leaf: 2
- random_state: 42

## 2.4 Evaluation Metrics

- Accuracy
- Precision
- Recall
- AUC-ROC

# 3. Results

The Random Forest classifier achieved perfect performance:

| Metric | Score |
|--------|-------|
| Accuracy | 1.00 |
| Precision | 1.00 |
| Recall | 1.00 |
| AUC-ROC | 1.00 |

# 4. Discussion

Perfect classification performance indicates complete separability of the two iris species in feature space. This demonstrates the effectiveness of Random Forest for botanical classification tasks.

# 5. Conclusion

We present a reproducible machine learning pipeline for iris species classification achieving perfect performance. The code and results are publicly available on GitHub.

---

**For the complete paper with detailed methodology, background, and discussion, see PAPER.md**
