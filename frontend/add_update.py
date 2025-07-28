import streamlit as st
from datetime import datetime
import requests

def add_update_tab(API_URL):
    selected_date = st.date_input("Enter Date", datetime(2024 ,8 ,1),
                                  label_visibility="collapsed")
    with st.spinner("Loading existing expenses..."):
        response = requests.get(f"{API_URL}/expenses/{selected_date}")
    existing_expenses = []
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("Failed to retrieve")
        existing_expenses = []

    # Set initial number of rows based on existing expenses
    row_key = f"num_rows_{selected_date}"
    if row_key not in st.session_state:
        st.session_state[row_key] = len(existing_expenses) if existing_expenses else 1

    # Show "Add Row" button outside the form
    if st.button("➕ Add Another Expense"):
        st.session_state[row_key] += 1

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    expenses = []

    with st.form(key="expense_form"):
        # Header row
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Amount**")
        with col2:
            st.markdown("**Category**")
        with col3:
            st.markdown("**Notes**")

        # Get total rows to show
        num_rows = st.session_state[row_key]

        # Input rows
        for i in range(num_rows):
            # Prefill from existing if available
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = "Rent"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount",
                                               min_value=0.0, step=1.0,
                                               value=amount, key=f"amount_{selected_date}_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category",
                                              options=categories,
                                              index=categories.index(category),
                                              key=f"category_{selected_date}_{i}",
                                              label_visibility="collapsed"
                                              )
            with col3:
                notes_input = st.text_input(label="Notes", value=notes,
                                            key=f"notes_{selected_date}_{i}",
                                            label_visibility="collapsed")


            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [e for e in expenses if e['amount'] != 0.0]
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")


