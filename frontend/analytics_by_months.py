import streamlit as st
import requests
import pandas as pd

def analytics_by_months_tab(API_URL):
    with st.spinner("Loading Analytics..."):
        response = requests.get(f"{API_URL}/analytics/month")
        response = response.json()

        months = []
        totals = []
        for item in response:
            months.append(item["month"])
            totals.append(item["total"])
        data = {
            "month": months,
            "total": totals
        }
        df = pd.DataFrame(data)
#
        st.subheader("Expense Breakdown by Months")
        st.bar_chart(data=df.set_index("month"), width=0, height=0, use_container_width=50)
        df["total"] = df["total"].map("{:.2f}".format)
        st.table(df)