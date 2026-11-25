import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Bank Churn Intelligence",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background-color: #111b2e;
}
div[data-testid="stMetric"] {
    background-color: #162338;
    border: 1px solid #273953;
    padding: 18px;
    border-radius: 12px;
}
h1, h2, h3 {
    color: #67e8c5 !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECT DATA
# --------------------------------------------------
total_customers = 10000
churned = 2037
retained = 7963

model_results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting",
        "XGBoost"
    ],
    "Accuracy": [0.7095, 0.6695, 0.8375, 0.8675, 0.8695],
    "Precision": [0.3828, 0.4547, 0.5876, 0.7710, 0.7897],
    "Recall": [0.6978, 0.7396, 0.6757, 0.4963, 0.4889],
    "F1 Score": [0.4943, 0.5613, 0.6286, 0.6039, 0.6040],
    "ROC-AUC": [0.7759, 0.0000, 0.8645, 0.8659, 0.8637]
})

# Correct Decision Tree ROC-AUC will be displayed as unavailable
model_results.loc[1, "ROC-AUC"] = None

risk_segments = pd.DataFrame({
    "Risk Category": ["Low", "Medium", "High", "Critical"],
    "Customers": [1107, 552, 185, 156],
    "Average Risk (%)": [14.64, 42.87, 69.78, 87.40],
    "Actual Churn Rate (%)": [5.24, 21.01, 51.35, 88.46]
})

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🏦 Bank Churn Intelligence")
st.sidebar.caption("Predictive Analytics & Risk Scoring")
page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Churn Analytics",
        "Model Performance",
        "Risk Segmentation",
        "Financial Impact",
        "Data Explorer"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "Machine-learning project developed as part of the Unified Mentor internship."
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🏦 Bank Customer Churn Intelligence")
st.caption("Predictive Modeling • Risk Scoring • Customer Retention Analytics")
st.divider()

# --------------------------------------------------
# PAGE 1: EXECUTIVE OVERVIEW
# --------------------------------------------------
if page == "Executive Overview":

    st.subheader("Executive Summary")

    st.write(
        "An analytical dashboard designed to understand bank customer churn, "
        "compare machine-learning models and identify customer groups requiring "
        "retention attention."
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Customers", "10,000")
    c2.metric("Churned Customers", "2,037")
    c3.metric("Retention Rate", "79.63%")
    c4.metric("Churn Rate", "20.37%")

    st.subheader("Customer Status Distribution")

    status_data = pd.DataFrame({
        "Customer Status": ["Retained", "Exited"],
        "Customers": [retained, churned]
    }).set_index("Customer Status")

    st.bar_chart(status_data)

    st.subheader("Project Highlights")

    a, b = st.columns(2)

    with a:
        st.markdown("#### 🏆 Champion Model")
        st.metric("Gradient Boosting ROC-AUC", "86.59%")
        st.write(
            "Gradient Boosting was selected as the champion model "
            "based on ROC-AUC."
        )

    with b:
        st.markdown("#### 🎯 Risk Prioritization")
        st.metric("High + Critical Risk Customers", "341")
        st.write(
            "These customers represent 17.05% of the test population "
            "and can be prioritized for targeted retention strategies."
        )

    st.subheader("Key Business Insights")
    st.markdown("""
    - Customer churn is approximately one-fifth of the dataset.
    - Age and number of products were among the most important model features.
    - Risk scores can help prioritize customer retention outreach.
    - Model scores should support decisions, not replace human judgment.
    """)

# --------------------------------------------------
# PAGE 2: CHURN ANALYTICS
# --------------------------------------------------
elif page == "Churn Analytics":

    st.subheader("Customer Churn Analysis")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Customers", "10,000")
    c2.metric("Exited", "2,037")
    c3.metric("Retained", "7,963")

    churn_data = pd.DataFrame({
        "Status": ["Retained", "Exited"],
        "Count": [7963, 2037]
    }).set_index("Status")

    st.markdown("#### Retained vs Exited Customers")
    st.bar_chart(churn_data)

    st.markdown("#### Churn Rate")
    st.progress(0.2037)
    st.write("20.37% of customers exited in the dataset.")

    st.info(
        "Customer churn analysis helps businesses identify retention "
        "challenges and design more focused customer engagement strategies."
    )

# --------------------------------------------------
# PAGE 3: MODEL PERFORMANCE
# --------------------------------------------------
elif page == "Model Performance":

    st.subheader("Machine Learning Model Comparison")

    st.write(
        "Five classification models were evaluated using multiple "
        "performance metrics."
    )

    st.dataframe(
        model_results.style.format({
            "Accuracy": "{:.2%}",
            "Precision": "{:.2%}",
            "Recall": "{:.2%}",
            "F1 Score": "{:.2%}",
            "ROC-AUC": lambda x: "N/A" if pd.isna(x) else f"{x:.2%}"
        }),
        use_container_width=True
    )

    st.markdown("#### Accuracy Comparison")
    st.bar_chart(
        model_results.set_index("Model")[["Accuracy"]]
    )

    st.markdown("#### ROC-AUC Comparison")
    auc_data = model_results.dropna(subset=["ROC-AUC"])
    st.bar_chart(
        auc_data.set_index("Model")[["ROC-AUC"]]
    )

    st.markdown("#### Champion Model — Gradient Boosting")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Accuracy", "86.75%")
    c2.metric("Precision", "77.10%")
    c3.metric("Recall", "49.63%")
    c4.metric("ROC-AUC", "86.59%")

    st.success(
        "Gradient Boosting was selected as the champion based on ROC-AUC."
    )

    st.caption(
        "XGBoost achieved the highest accuracy and precision. "
        "Random Forest achieved the highest recall and F1-score. "
        "Model selection depends on the business objective."
    )

# --------------------------------------------------
# PAGE 4: RISK SEGMENTATION
# --------------------------------------------------
elif page == "Risk Segmentation":

    st.subheader("Customer Risk Classification")

    st.write(
        "Customers are categorized based on their predicted probability of churn."
    )

    st.dataframe(risk_segments, use_container_width=True)

    st.markdown("#### Customer Distribution by Risk")
    st.bar_chart(
        risk_segments.set_index("Risk Category")[["Customers"]]
    )

    st.markdown("#### Average Predicted Risk by Segment")
    st.bar_chart(
        risk_segments.set_index("Risk Category")[["Average Risk (%)"]]
    )

    st.markdown("#### Actual Churn Rate by Risk Segment")
    st.bar_chart(
        risk_segments.set_index("Risk Category")[["Actual Churn Rate (%)"]]
    )

    st.markdown("#### Risk Bands & Suggested Actions")

    st.markdown("""
    | Risk Band | Probability | Recommended Action |
    |---|---|---|
    | 🟢 Low | Below 30% | Maintain engagement |
    | 🟡 Medium | 30%–below 60% | Monitor behavior |
    | 🟠 High | 60%–below 80% | Targeted retention |
    | 🔴 Critical | 80% and above | Prioritized intervention |
    """)

    st.warning(
        "High and Critical segments together contain 341 customers "
        "in the evaluated test sample."
    )

# --------------------------------------------------
# PAGE 5: FINANCIAL IMPACT
# --------------------------------------------------
elif page == "Financial Impact":

    st.subheader("Retention Campaign Financial Scenario Analysis")

    st.write(
        "Illustrative scenarios estimate the potential financial impact "
        "of targeted retention outreach. These are hypothetical assumptions, "
        "not observed campaign results."
    )

    contact_cost = 500
    customers_targeted = 468
    campaign_cost = contact_cost * customers_targeted

    c1, c2, c3 = st.columns(3)
    c1.metric("Contact Cost / Customer", "₹500")
    c2.metric("Target Customers", "468")
    c3.metric("Campaign Cost", "₹2,34,000")

    financial = pd.DataFrame({
        "Scenario": ["Conservative", "Moderate", "Optimistic"],
        "Customers Saved": [27, 55, 82],
        "Benefit (₹)": [216000, 550000, 984000],
        "Net Benefit (₹)": [-18000, 316000, 750000],
        "ROI (%)": [-7.69, 135.04, 320.51]
    })

    st.markdown("#### Scenario Comparison")
    st.dataframe(financial, use_container_width=True)

    st.markdown("#### Net Benefit by Scenario")
    st.bar_chart(
        financial.set_index("Scenario")[["Net Benefit (₹)"]]
    )

    st.markdown("#### ROI Comparison")
    st.bar_chart(
        financial.set_index("Scenario")[["ROI (%)"]]
    )

    st.info(
        "The moderate and optimistic scenarios illustrate how retention "
        "campaign effectiveness could influence financial returns. "
        "Actual results would depend on campaign costs, customer value "
        "and realized save rates."
    )

# --------------------------------------------------
# PAGE 6: DATA EXPLORER
# --------------------------------------------------
elif page == "Data Explorer":

    st.subheader("Explore Your Own Customer Dataset")

    st.write(
        "Upload a CSV file to inspect the data, explore columns, "
        "review descriptive statistics and visualize selected variables."
    )

    uploaded_file = st.file_uploader(
        "Upload a customer CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:
            df = pd.read_csv(uploaded_file)

            st.success("Dataset uploaded successfully!")

            c1, c2, c3 = st.columns(3)
            c1.metric("Rows", f"{df.shape[0]:,}")
            c2.metric("Columns", df.shape[1])
            c3.metric("Missing Cells", f"{df.isna().sum().sum():,}")

            st.markdown("#### Data Preview")
            st.dataframe(df.head(100), use_container_width=True)

            st.markdown("#### Descriptive Statistics")
            st.dataframe(df.describe(include="all").T, use_container_width=True)

            st.markdown("#### Missing Values by Column")
            missing = df.isnull().sum()
            st.bar_chart(missing)

            numeric_columns = df.select_dtypes(include="number").columns.tolist()

            if numeric_columns:
                selected_column = st.selectbox(
                    "Select a numeric column to visualize",
                    numeric_columns
                )

                st.markdown(f"#### Distribution of {selected_column}")
                st.bar_chart(df[selected_column].value_counts().sort_index().head(50))

        except Exception as e:
            st.error(f"Unable to read the file: {e}")

    else:
        st.info("Upload a CSV file to begin exploring your data.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.markdown("""
<div style="text-align:center; color:#94a3b8;">
Bank Customer Churn Risk Scoring | Unified Mentor Project<br>
Predictive Analytics • Machine Learning • Banking Insights
</div>
""", unsafe_allow_html=True)
