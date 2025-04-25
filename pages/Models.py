import streamlit as st

st.set_page_config(page_title="Model Training Code and Performance", layout="wide")

st.title("🧠 Model Training Code and Performance")

st.markdown("""
Explore the training code, rationale, and performance of each model (CatBoost, XGBoost, LightGBM) used in our project.
""")

# Define tabs
catboost_tab, xgboost_tab, lightgbm_tab, model_choosing_Tab = st.tabs([
    "CatBoost",
    "XGBoost",
    "LightGBM Ensemble",
    "Model Choice Rationale and Summary"
])

with catboost_tab:
    st.subheader("CatBoost Model Training")
    st.markdown("""
CatBoost is particularly effective for small to medium-sized datasets and handles categorical data well. It includes built-in mechanisms to deal with class imbalance using `auto_class_weights='Balanced'`, making it ideal for our dividend prediction task.
""")
    st.code("""
from catboost import CatBoostClassifier

cat_model = CatBoostClassifier(
    iterations=300,
    learning_rate=0.05,
    depth=6,
    loss_function='MultiClass',
    eval_metric='TotalF1',
    random_seed=42,
    verbose=0,
    auto_class_weights='Balanced'
)

cat_model.fit(X_train_resampled, y_train_resampled)
y_pred = cat_model.predict(X_test)
y_pred = y_pred.flatten()

# Decode predictions
y_pred_decoded = [inv_label_map[p] for p in y_pred]
y_test_decoded = [inv_label_map[t] for t in y_test]
    """, language="python")
    st.image("images/catboost.png", caption="Classification Report and Confusion Matrix", use_column_width=True)

with lightgbm_tab:
    st.subheader("💡 LightGBM Ensemble Model Training")
    st.markdown("""
We chose a LightGBM-based ensemble with Logistic Regression and Decision Trees because it balances speed and performance, especially with class imbalance managed via SMOTE. The soft-voting ensemble helps average diverse decision boundaries for robust predictions.
""")
    st.code("""
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from imblearn.over_sampling import SMOTE
from collections import Counter
import pickle, os

lgb_model = LGBMClassifier(class_weight='balanced', random_state=42)
log_model = LogisticRegression(max_iter=1000, class_weight='balanced')
tree_model = DecisionTreeClassifier(class_weight='balanced', max_depth=5)
ensemble = VotingClassifier(estimators=[('lgb', lgb_model), ('lr', log_model), ('dt', tree_model)], voting='soft')
ensemble.fit(X_train_resampled, y_train_resampled)
    """, language="python")
    st.subheader("1. Voting Ensemble method :")
    st.image("images/le.png", caption="Classification Report Ensemble", use_column_width=True)
    st.image("images/lightensemble.png", caption="Confusion Matrix Ensemble", use_column_width=True)
    st.subheader("2. Financial Sector :")
    st.image("images/lf.png", caption="Classification Report for Financial", use_column_width=True)
    st.image("images/lfconf.png", caption="Confusion Matrix for Financial", use_column_width=True)

with xgboost_tab:
    st.subheader("XGBoost Model Training")
    st.markdown("""XGBoost is a gradient boosting framework that excels on structured/tabular data. It’s widely used for its speed, regularization capabilities, and scalability.""")
    st.code("""
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

model = XGBClassifier(
    objective='multi:softprob',
    num_class=3,
    eval_metric='mlogloss',
    use_label_encoder=False,
    learning_rate=0.05,
    max_depth=5,
    n_estimators=300,
    random_state=42
)

model.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_test)
y_pred_decoded = [inv_label_map[p] for p in y_pred]
y_test_decoded = [inv_label_map[t] for t in y_test]
    """, language="python")
    st.subheader("1. Consumer Sector :")
    st.image("images/xgbc.png", caption="Classification Report for Consumer", use_column_width=True)
    st.image("images/xgbcconf.png", caption="Confusion Matrix for Consumer", use_column_width=True)
    st.subheader("2. Energy Sector :")
    st.image("images/xgbe.png", caption="Classification Report for Energy", use_column_width=True)
    st.image("images/xgbeconf.png", caption="Confusion Matrix for Energy", use_column_width=True)
    st.subheader("3. Financial Sector :")
    st.image("images/xgbf.png", caption="Classification Report for Financial", use_column_width=True)
    st.image("images/xgbfconf.png", caption="Confusion Matrix for Financial", use_column_width=True)
    st.subheader("4. Other Sector :")
    st.image("images/xgbo.png", caption="Classification Report for Other", use_column_width=True)
    st.image("images/xgboconf.png", caption="Confusion Matrix for Other", use_column_width=True)

with model_choosing_Tab:
    st.title("Model Choice Rationale and Training Summary")

    st.header("CatBoost")
    st.markdown("""
- **Why CatBoost?**
  - Handles categorical features inherently (though not used directly here).
  - Excellent performance on small/medium-sized tabular datasets.
  - Robust to overfitting and handles class imbalance using `auto_class_weights='Balanced'`.

- **Training Highlights:**
  - Iterations: 300
  - Learning Rate: 0.05
  - Depth: 6
  - Evaluation Metric: Total F1
  - auto_class_weights='Balanced'
""")

    st.header("LightGBM Ensemble")
    st.markdown("""
- **Why LightGBM Ensemble?**
  - Fast, efficient boosting algorithm optimized for speed and memory.
  - Paired with Logistic Regression and Decision Trees in a **soft voting ensemble** to combine strengths of linear and nonlinear learners.
  - Uses **SMOTE** for oversampling minority classes where needed.

- **Training Highlights:**
  - Models: LightGBM + Logistic Regression + Decision Tree
  - Voting: Soft
  - Industry-specific models saved individually
""")

    st.header("XGBoost")
    st.markdown("""
- **Why XGBoost?**
  - Highly optimized gradient boosting algorithm.
  - Strong performance on structured/tabular data.
  - Good regularization capabilities (L1/L2) to prevent overfitting.

- **Training Highlights:**
  - Model Objective: Multiclass classification with softprob output for 3 dividend change classes (Increase, Decrease, No Change).
  - Hyperparameters: Trained with learning_rate = 0.05, max_depth = 5, and n_estimators = 300 for balanced performance.
  - Class Imbalance Handling: Used SMOTE oversampling on minority classes before training to improve recall on rare outcomes.
  - Industry-Specific Training: Separate models were trained for each sector — Consumer, Financials, Energy, and Others — to better capture domain-specific patterns.
""")
