# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import pickle
# from catboost import CatBoostClassifier
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier

# st.title("📈 Predict Dividend Change using yFinance Data")

# ticker_input = st.text_input("Enter a Ticker Symbol (e.g., AAPL, MSFT, GE):", value="AAPL")
# model_option = st.selectbox("Choose a Model:", ["CatBoost", "XGBoost", "LightGBM"])

# def safe_div(a, b):
#     try:
#         return float(a) / float(b) if a and b and b != 0 else 0
#     except:
#         return 0

# def safe_get(df, key):
#     return df.get(key, 0) or 0

# if st.button("🔍 Fetch & Predict"):
#     try:
#         stock = yf.Ticker(ticker_input)

#         # Use classic quarterly attributes
#         income_raw = stock.quarterly_income_stmt
#         balance_raw = stock.quarterly_balance_sheet
#         cashflow_raw = stock.quarterly_cashflow

#         st.write("🧾 Income Statement Shape:", income_raw.shape)
#         st.write("🧾 Balance Sheet Shape:", balance_raw.shape)
#         st.write("🧾 Cash Flow Shape:", cashflow_raw.shape)

#         if income_raw.empty or balance_raw.empty or cashflow_raw.empty:
#             st.error("❌ One or more financial statements are unavailable. Try a different ticker.")
#             st.stop()

#         income_stmt = income_raw.iloc[:, 0]
#         balance_sheet = balance_raw.iloc[:, 0]
#         cashflow_stmt = cashflow_raw.iloc[:, 0]

#         short_debt = safe_get(balance_sheet, "Short Long Term Debt")
#         long_debt = safe_get(balance_sheet, "Long Term Debt")
#         total_debt = short_debt + long_debt

#         ratios = {
#             'dpr': safe_div(safe_get(cashflow_stmt, "Cash Dividends Paid"), safe_get(income_stmt, "Net Income")),
#             'roe': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Stockholders Equity")),
#             'roa': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Total Assets")),
#             'GProf': safe_div(safe_get(income_stmt, "Gross Profit"), safe_get(income_stmt, "Total Revenue")),
#             'npm': safe_div(safe_get(income_stmt, "Net Income"), safe_get(income_stmt, "Total Revenue")),
#             'fcf_ocf': safe_div(safe_get(cashflow_stmt, "Free Cash Flow"), safe_get(cashflow_stmt, "Operating Cash Flow")),
#             'cash_debt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), total_debt),
#             'cash_lt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), long_debt),
#             'ocf_lct': safe_div(safe_get(cashflow_stmt, "Operating Cash Flow"), total_debt),
#             'totdebt_invcap': safe_div(total_debt, safe_get(balance_sheet, "Invested Capital")),
#             'de_ratio': safe_div(total_debt, safe_get(balance_sheet, "Stockholders Equity")),
#             'debt_ebitda': safe_div(total_debt, safe_get(income_stmt, "EBITDA")),
#             'intcov_ratio': safe_div(safe_get(income_stmt, "EBIT"), safe_get(income_stmt, "Interest Expense")),
#             'curr_ratio': safe_div(safe_get(balance_sheet, "Current Assets"), safe_get(balance_sheet, "Current Liabilities")),
#             'cash_ratio': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), safe_get(balance_sheet, "Current Liabilities")),
#             'quick_ratio': safe_div(safe_get(balance_sheet, "Current Assets") - safe_get(balance_sheet, "Inventory"), safe_get(balance_sheet, "Current Liabilities")),
#         }

#         input_df = pd.DataFrame([ratios])
#         st.subheader("📋 Computed Financial Ratios")
#         st.dataframe(input_df.T)

#         if model_option == "CatBoost":
#             with open("models/catboost_model.pkl", "rb") as f:
#                 model = pickle.load(f)

#         elif model_option == "XGBoost":
#             with open("models/xgboost_model.pkl", "rb") as f:
#                 model = pickle.load(f)
#         elif model_option == "LightGBM":
#             with open("models/lightgbm_model_other.pkl", "rb") as f:
#                 model = pickle.load(f)

#         y_pred = model.predict(input_df)
#         label_map = {-1: "📉 Decrease", 0: "➖ No Change", 1: "📈 Increase"}
#         pred = int(y_pred.flatten()[0]) if hasattr(y_pred, 'flatten') else int(y_pred[0])
#         st.success(f"📊 Predicted Dividend Change: **{label_map[pred]}**")

#     except Exception as e:
#         st.error(f"❌ Error during prediction: {e}")


#old



# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import pickle
# # from catboost import CatBoostClassifier
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier

# st.title("📈 Predict Dividend Change using yFinance Data")

# ticker_input = st.text_input("Enter a Ticker Symbol (e.g., AAPL, MSFT, GE):", value="AAPL")
# industry = st.selectbox("Select Industry", ["Consumer", "Financials", "Energy", "Other"])
# model_option = st.selectbox("Choose a Model:", ["CatBoost", "XGBoost", "LightGBM"])

# def safe_div(a, b):
#     try:
#         return float(a) / float(b) if a and b and b != 0 else 0
#     except:
#         return 0

# def safe_get(df, key):
#     return df.get(key, 0) or 0

# if st.button("🔍 Fetch & Predict"):
#     try:
#         stock = yf.Ticker(ticker_input)

#         # Retrieve quarterly statements
#         income_raw = stock.quarterly_income_stmt
#         balance_raw = stock.quarterly_balance_sheet
#         cashflow_raw = stock.quarterly_cashflow

#         st.write("🧾 Income Statement Shape:", income_raw.shape)
#         st.write("🧾 Balance Sheet Shape:", balance_raw.shape)
#         st.write("🧾 Cash Flow Shape:", cashflow_raw.shape)

#         if income_raw.empty or balance_raw.empty or cashflow_raw.empty:
#             st.error("❌ One or more financial statements are unavailable. Try a different ticker.")
#             st.stop()

#         # Use most recent column
#         income_stmt = income_raw.iloc[:, 0]
#         balance_sheet = balance_raw.iloc[:, 0]
#         cashflow_stmt = cashflow_raw.iloc[:, 0]

#         short_debt = safe_get(balance_sheet, "Short Long Term Debt")
#         long_debt = safe_get(balance_sheet, "Long Term Debt")
#         total_debt = short_debt + long_debt

#         # Compute ratios
#         ratios = {
#             'dpr': safe_div(safe_get(cashflow_stmt, "Cash Dividends Paid"), safe_get(income_stmt, "Net Income")),
#             'roe': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Stockholders Equity")),
#             'roa': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Total Assets")),
#             'GProf': safe_div(safe_get(income_stmt, "Gross Profit"), safe_get(income_stmt, "Total Revenue")),
#             'npm': safe_div(safe_get(income_stmt, "Net Income"), safe_get(income_stmt, "Total Revenue")),
#             'fcf_ocf': safe_div(safe_get(cashflow_stmt, "Free Cash Flow"), safe_get(cashflow_stmt, "Operating Cash Flow")),
#             'cash_debt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), total_debt),
#             'cash_lt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), long_debt),
#             'ocf_lct': safe_div(safe_get(cashflow_stmt, "Operating Cash Flow"), total_debt),
#             'totdebt_invcap': safe_div(total_debt, safe_get(balance_sheet, "Invested Capital")),
#             'de_ratio': safe_div(total_debt, safe_get(balance_sheet, "Stockholders Equity")),
#             'debt_ebitda': safe_div(total_debt, safe_get(income_stmt, "EBITDA")),
#             'intcov_ratio': safe_div(safe_get(income_stmt, "EBIT"), safe_get(income_stmt, "Interest Expense")),
#             'curr_ratio': safe_div(safe_get(balance_sheet, "Current Assets"), safe_get(balance_sheet, "Current Liabilities")),
#             'cash_ratio': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), safe_get(balance_sheet, "Current Liabilities")),
#             'quick_ratio': safe_div(safe_get(balance_sheet, "Current Assets") - safe_get(balance_sheet, "Inventory"), safe_get(balance_sheet, "Current Liabilities")),
#         }

#         input_df = pd.DataFrame([ratios])
#         input_df.fillna(0, inplace=True)  # ✅ fix for NaN
#         if input_df.isnull().values.any():
#             st.warning("⚠️ Warning: NaN detected in input. Filling with 0.")

#         st.subheader("📋 Computed Financial Ratios")
#         st.dataframe(input_df.T)

#         # Model path logic
#         sector_key = industry.lower()
#         model_paths = {
#             # "CatBoost": f"models/catboost_model_{sector_key}.pkl",
#             "XGBoost": f"models/xgboost_model_{sector_key}.pkl",
#             "LightGBM": f"models/lightgbm_model_{sector_key}.pkl",
#         }
#         model_path = model_paths[model_option]

#         # Load and predict
#         with open(model_path, "rb") as f:
#             model = pickle.load(f)

#         y_pred = model.predict(input_df)
#         label_map = {0: "📉 Decrease", 1: "➖ No Change", 2: "📈 Increase"}
#         pred = int(y_pred.flatten()[0]) if hasattr(y_pred, 'flatten') else int(y_pred[0])
#         st.success(f"📊 Predicted Dividend Change: **{label_map[pred]}**")
#         st.session_state.prediction_label = label_map[pred]
#         st.session_state.input_df = input_df
#         st.session_state.ticker = ticker_input
#         st.session_state.industry = industry
#     except Exception as e:
#         st.error(f"❌ Error during prediction: {e}")



# NEW

import streamlit as st
import yfinance as yf
import pandas as pd
import pickle
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

st.title("📈 Predict Dividend Change using yFinance Data")

ticker_input = st.text_input("Enter a Ticker Symbol (e.g., AAPL, MSFT, GE):", value="AAPL")
industry = st.selectbox("Select Industry", ["Consumer", "Financials", "Energy", "Other"])
model_option = st.selectbox("Choose a Model:", ["CatBoost", "XGBoost", "LightGBM"])

def safe_get(df, key):
    df = df.T  # transpose to make metrics the columns
    return df[key].iloc[0] if key in df.columns else 0

def safe_div(a, b):
    try:
        return float(a) / float(b) if a and b and b != 0 else 0
    except:
        return 0

if st.button("🔍 Fetch & Predict"):
    try:
        stock = yf.Ticker(ticker_input)
        # Retrieve quarterly statements
        income_raw = stock.quarterly_income_stmt
        balance_raw = stock.quarterly_balance_sheet
        cashflow_raw = stock.quarterly_cashflow

        st.write("🧾 Income Statement Shape:", income_raw.shape)
        st.write("🧾 Balance Sheet Shape:", balance_raw.shape)
        st.write("🧾 Cash Flow Shape:", cashflow_raw.shape)

        if income_raw.empty or balance_raw.empty or cashflow_raw.empty:
            st.error("❌ One or more financial statements are unavailable. Try a different ticker.")
            st.stop()

        # Compute total debt
        short_debt = safe_get(balance_raw, "Short Long Term Debt")
        long_debt = safe_get(balance_raw, "Long Term Debt")
        total_debt = short_debt + long_debt

        # Compute ratios
        ratios = {
            'dpr': safe_div(safe_get(cashflow_raw, "Cash Dividends Paid"), safe_get(income_raw, "Net Income")),
            'roe': safe_div(safe_get(income_raw, "Net Income"), safe_get(balance_raw, "Stockholders Equity")),
            'roa': safe_div(safe_get(income_raw, "Net Income"), safe_get(balance_raw, "Total Assets")),
            'GProf': safe_div(safe_get(income_raw, "Gross Profit"), safe_get(income_raw, "Total Revenue")),
            'npm': safe_div(safe_get(income_raw, "Net Income"), safe_get(income_raw, "Total Revenue")),
            'fcf_ocf': safe_div(safe_get(cashflow_raw, "Free Cash Flow"), safe_get(cashflow_raw, "Operating Cash Flow")),
            'cash_debt': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), total_debt),
            'cash_lt': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), long_debt),
            'ocf_lct': safe_div(safe_get(cashflow_raw, "Operating Cash Flow"), total_debt),
            'totdebt_invcap': safe_div(total_debt, safe_get(balance_raw, "Invested Capital")),
            'de_ratio': safe_div(total_debt, safe_get(balance_raw, "Stockholders Equity")),
            'debt_ebitda': safe_div(total_debt, safe_get(income_raw, "EBITDA")),
            'intcov_ratio': safe_div(safe_get(income_raw, "EBIT"), safe_get(income_raw, "Interest Expense")),
            'curr_ratio': safe_div(safe_get(balance_raw, "Current Assets"), safe_get(balance_raw, "Current Liabilities")),
            'cash_ratio': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), safe_get(balance_raw, "Current Liabilities")),
            'quick_ratio': safe_div(safe_get(balance_raw, "Current Assets") - safe_get(balance_raw, "Inventory"), safe_get(balance_raw, "Current Liabilities")),
        }
        # ratios = {
        #     'dpr': safe_div(safe_get(cashflow_stmt, "Cash Dividends Paid"), safe_get(income_stmt, "Net Income")),
        #     'roe': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Stockholders Equity")),
        #     'roa': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Total Assets")),
        #     'GProf': safe_div(safe_get(income_stmt, "Gross Profit"), safe_get(income_stmt, "Total Revenue")),
        #     'npm': safe_div(safe_get(income_stmt, "Net Income"), safe_get(income_stmt, "Total Revenue")),
        #     'fcf_ocf': safe_div(safe_get(cashflow_stmt, "Free Cash Flow"), safe_get(cashflow_stmt, "Operating Cash Flow")),
        #     'cash_debt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), total_debt),
        #     'cash_lt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), long_debt),
        #     'ocf_lct': safe_div(safe_get(cashflow_stmt, "Operating Cash Flow"), total_debt),
        #     'totdebt_invcap': safe_div(total_debt, safe_get(balance_sheet, "Invested Capital")),
        #     'de_ratio': safe_div(total_debt, safe_get(balance_sheet, "Stockholders Equity")),
        #     'debt_ebitda': safe_div(total_debt, safe_get(income_stmt, "EBITDA")),
        #     'intcov_ratio': safe_div(safe_get(income_stmt, "EBIT"), safe_get(income_stmt, "Interest Expense")),
        #     'curr_ratio': safe_div(safe_get(balance_sheet, "Current Assets"), safe_get(balance_sheet, "Current Liabilities")),
        #     'cash_ratio': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), safe_get(balance_sheet, "Current Liabilities")),
        #     'quick_ratio': safe_div(safe_get(balance_sheet, "Current Assets") - safe_get(balance_sheet, "Inventory"), safe_get(balance_sheet, "Current Liabilities")),
        # }

        input_df = pd.DataFrame([ratios])
        input_df.fillna(0, inplace=True)
        if input_df.isnull().values.any():
            st.warning("⚠️ Warning: NaN detected in input. Filling with 0.")

        st.subheader("📋 Computed Financial Ratios")
        st.dataframe(input_df.T)

        # Model path logic
        sector_key = industry.lower()
        model_paths = {
            "CatBoost": f"models/catboost_model_{sector_key}.pkl",
            "XGBoost": f"models/xgboost_model_{sector_key}.pkl",
            "LightGBM": f"models/lightgbm_model_{sector_key}.pkl",
        }
        model_path = model_paths[model_option]

        with open(model_path, "rb") as f:
            model = pickle.load(f)

                # Prediction and probabilities
        y_pred = model.predict(input_df)
        y_proba = model.predict_proba(input_df)[0]

        label_map = {
             -1: "📉 Decrease",
             0: "➖ No Change",
             1: "📈 Increase"
        }
  # Display prediction
        pred = int(y_pred.flatten()[0]) if hasattr(y_pred, 'flatten') else int(y_pred[0])
        st.success(f"📊 Predicted Dividend Change: *{label_map[pred]}*")

        # Show probabilities as chart
        proba_map = {-1: y_proba[-1], 0: y_proba[0], 1: y_proba[1]}
        proba_df = pd.DataFrame.from_dict(
            {label_map[k]: [v] for k, v in proba_map.items()},
            orient='columns'
        )
        st.subheader("🔢 Prediction Probabilities")
        st.bar_chart(proba_df.T.rename(columns={0: "Probability"}))

        # --- Optional GPT Explanation (only if prediction exists) ---
        if "prediction_label" in st.session_state and "input_df" in st.session_state:
        
            st.markdown("---")
            st.subheader("🧠 GPT-Powered Analysis")
            with st.form(key="gpt_form"):
                api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password")
                submit_gpt = st.form_submit_button("Generate GPT Interpretation")
        
            if submit_gpt and api_key:
                try:
                    import openai
                    openai.api_key = api_key
        
                    # Load required session state values
                    label = st.session_state.prediction_label
                    ratios_dict = st.session_state.input_df.iloc[0].to_dict()
                    ticker = st.session_state.get("ticker", "N/A")
                    industry = st.session_state.get("industry", "Unknown")
        
                    # Format ratios for GPT
                    ratios_text = "\n".join([f"{k}: {round(v, 4)}" for k, v in ratios_dict.items()])
        
                    # Prompt for GPT
                    prompt = f"""
        You are a financial analyst AI. A machine learning model predicted that the dividend for ticker {ticker} in the {industry} industry will {label.lower().replace('📈 ', 'increase').replace('📉 ', 'decrease').replace('➖ ', 'stay the same')}.
        Here are the computed financial ratios:
        {ratios_text}
        
        Please provide a professional and insightful explanation of why this outcome is likely, referencing the most influential financial ratios.
        """
        
                    with st.spinner("💬 Generating GPT analysis..."):
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a financial analyst."},
                                {"role": "user", "content": prompt}
                            ],
                            temperature=0.7,
                            max_tokens=500
                        )
                        output = response.choices[0].message["content"]
                        st.markdown("### 📘 GPT Interpretation")
                        st.write(output)
        
                except Exception as e:
                    st.error(f"⚠️ GPT Error: {e}")
        
            elif submit_gpt and not api_key:
                st.warning("⚠️ Please enter a valid OpenAI API Key.")

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
