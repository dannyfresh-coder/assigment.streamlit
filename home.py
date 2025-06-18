import streamlit as st
from current_account import CurrentAccount
from savings_account import SavingsAccount

# Set up the page configuration
st.set_page_config(page_title="Banking App", layout="centered")

# Initialize account balances
current_balance = 0
savings_balance = 0

# Create account instances
current_account = CurrentAccount(current_balance)
savings_account = SavingsAccount(savings_balance)

# Sidebar navigation
st.sidebar.title("Banking Operations")
operation = st.sidebar.radio("Choose an account", ["Current Account", "Savings Account"])

# Display account details
if operation == "Current Account":
    account = current_account
    account_type = "Current"
elif operation == "Savings Account":
    account = savings_account
    account_type = "Savings"

st.title(f"{account_type} Account Operations")
st.write(f"Current Balance: ₦{account.balance:,.2f}")

# Deposit operation
with st.form(key="deposit_form"):
    deposit_amount = st.number_input("Enter deposit amount", min_value=1000, step=1000)
    deposit_button = st.form_submit_button("Deposit")
    if deposit_button:
        account.deposit(deposit_amount)
        st.success(f"Deposited ₦{deposit_amount:,.2f}. New balance: ₦{account.balance:,.2f}")

# Withdraw operation
with st.form(key="withdraw_form"):
    withdraw_amount = st.number_input("Enter withdrawal amount", min_value=1000, step=1000)
    withdraw_button = st.form_submit_button("Withdraw")
    if withdraw_button:
        try:
            account.withdraw(withdraw_amount)
            st.success(f"Withdrew ₦{withdraw_amount:,.2f}. New balance: ₦{account.balance:,.2f}")
        except ValueError as e:
            st.error(e)
