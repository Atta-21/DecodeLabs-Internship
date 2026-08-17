import re
from pathlib import Path
import pandas as pd

# DecodeLabs Project 1
# E-commerce Dataset Chatbot
#
# The chatbot reads the supplied order dataset and answers
# common questions about orders, products, sales and customers.

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "ecommerce_orders.csv"


def load_data():
    """Load the project dataset and prepare a few useful columns."""
    data = pd.read_csv(DATA_FILE)

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["TotalPrice"] = pd.to_numeric(data["TotalPrice"], errors="coerce")
    data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
    data["UnitPrice"] = pd.to_numeric(data["UnitPrice"], errors="coerce")

    return data


def clean_text(message):
    """Make simple informal/casual typing easier to recognise."""
    message = str(message).lower().strip()

    replacements = {
        "whats": "what is",
        "what's": "what is",
        "how many": "how many",
        "ur": "your",
        "u": "you",
        "pls": "please",
        "plz": "please",
        "show me": "show",
        "tell me": "show",
    }

    for old, new in replacements.items():
        message = message.replace(old, new)

    message = re.sub(r"[!?.,;:]+", " ", message)
    return " ".join(message.split())


def money(value):
    return f"${value:,.2f}"


def year_from_message(message):
    years = re.findall(r"\b(20\d{2})\b", message)
    return int(years[0]) if years else None


def filtered_data(data, message):
    """Return the full data or a year-filtered view if a year was mentioned."""
    year = year_from_message(message)

    if year is not None:
        result = data[data["Date"].dt.year == year]
        return result, year

    return data, None


def answer_total_sales(data):
    return f"Bot: Total sales are {money(data['TotalPrice'].sum())}."


def answer_order_count(data):
    return f"Bot: There are {len(data):,} orders in the selected data."


def answer_cancelled(data):
    if "OrderStatus" not in data.columns:
        return "Bot: The dataset does not contain an OrderStatus column."

    cancelled = (data["OrderStatus"].astype(str).str.lower() == "cancelled").sum()
    return f"Bot: There are {cancelled:,} cancelled orders."


def answer_delivered(data):
    if "OrderStatus" not in data.columns:
        return "Bot: The dataset does not contain an OrderStatus column."

    delivered = (data["OrderStatus"].astype(str).str.lower() == "delivered").sum()
    return f"Bot: There are {delivered:,} delivered orders."


def answer_top_product(data):
    if data.empty:
        return "Bot: There is no data for that selection."

    product_sales = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

    if product_sales.empty:
        return "Bot: I could not find product information."

    product = product_sales.index[0]
    quantity = int(product_sales.iloc[0])

    return f"Bot: The most ordered product is '{product}' with {quantity:,} units."


def answer_top_payment(data):
    if data.empty:
        return "Bot: There is no data for that selection."

    counts = data["PaymentMethod"].value_counts()
    method = counts.index[0]

    return f"Bot: The most common payment method is {method}, with {counts.iloc[0]:,} orders."


def answer_top_referral(data):
    if data.empty:
        return "Bot: There is no data for that selection."

    counts = data["ReferralSource"].fillna("Unknown").value_counts()
    source = counts.index[0]

    return f"Bot: The referral source with the most orders is {source}, with {counts.iloc[0]:,} orders."


def answer_average_order(data):
    if data.empty:
        return "Bot: There is no data for that selection."

    average = data["TotalPrice"].mean()
    return f"Bot: The average order value is {money(average)}."


def answer_total_quantity(data):
    return f"Bot: The total quantity of products ordered is {int(data['Quantity'].sum()):,}."


def answer_top_customer(data):
    if data.empty:
        return "Bot: There is no data for that selection."

    customer_sales = data.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False)

    customer = customer_sales.index[0]
    amount = customer_sales.iloc[0]

    return f"Bot: Customer {customer} has the highest total order value: {money(amount)}."


def answer_coupon(data):
    if "CouponCode" not in data.columns:
        return "Bot: The dataset does not contain coupon information."

    used = data["CouponCode"].fillna("No Coupon")
    used = used[used.astype(str).str.lower() != "no coupon"]

    if used.empty:
        return "Bot: I could not find any used coupon codes."

    coupon = used.value_counts().index[0]
    count = used.value_counts().iloc[0]

    return f"Bot: The most frequently used coupon code is {coupon}, used in {count:,} orders."


def show_summary(data):
    print("\n---------------- DATASET SUMMARY ----------------")
    print(f"Rows: {len(data):,}")
    print(f"Columns: {len(data.columns)}")
    print(f"Total sales: {money(data['TotalPrice'].sum())}")
    print(f"Total quantity: {int(data['Quantity'].sum()):,}")

    if "OrderStatus" in data.columns:
        status = data["OrderStatus"].value_counts()
        print("\nOrder status:")
        for name, count in status.items():
            print(f"  {name}: {count:,}")

    print("--------------------------------------------------")


def show_help():
    print("""
---------------------- CHATBOT HELP ----------------------

Try questions like:

Sales
  total sales
  total sales in 2024
  average order value
  total quantity sold

Orders
  how many orders
  how many cancelled orders
  how many delivered orders

Products
  which product was ordered the most
  most ordered product

Customers
  which customer spent the most

Payments / Marketing
  most common payment method
  which referral source has the most orders
  most used coupon

Other
  summary
  help
  bye

You can also mention a year, for example:
  total sales in 2024
  orders in 2023
-----------------------------------------------------------
""")


def get_response(data, message):
    text = clean_text(message)

    if text in {"bye", "exit", "quit", "goodbye"}:
        return "EXIT", "Bot: Goodbye! 👋"

    if text in {"help", "menu", "commands"}:
        show_help()
        return "OK", None

    if text in {"summary", "show summary", "dataset summary"}:
        show_summary(data)
        return "OK", None

    selected, year = filtered_data(data, text)

    if year is not None and selected.empty:
        return "OK", f"Bot: I could not find any records for {year}."

    if "total sales" in text or "total sale" in text:
        answer = answer_total_sales(selected)
        if year:
            answer = answer.replace("are ", f"in {year} are ", 1)
        return "OK", answer

    if "average order" in text or "average sale" in text:
        answer = answer_average_order(selected)
        if year:
            answer = answer.replace("is ", f"in {year} is ", 1)
        return "OK", answer

    if "total quantity" in text or "quantity sold" in text or "units sold" in text:
        return "OK", answer_total_quantity(selected)

    if "cancelled" in text or "canceled" in text:
        return "OK", answer_cancelled(selected)

    if "delivered" in text:
        return "OK", answer_delivered(selected)

    if ("most ordered" in text or "ordered the most" in text or
            "best selling" in text or "top product" in text):
        return "OK", answer_top_product(selected)

    if "payment" in text and ("common" in text or "most" in text):
        return "OK", answer_top_payment(selected)

    if "referral" in text and ("most" in text or "highest" in text):
        return "OK", answer_top_referral(selected)

    if "customer" in text and ("spent" in text or "highest" in text or "most" in text):
        return "OK", answer_top_customer(selected)

    if "coupon" in text and ("most" in text or "used" in text):
        return "OK", answer_coupon(selected)

    if ("how many orders" in text or "number of orders" in text or
            text == "orders" or text.startswith("how many order")):
        answer = answer_order_count(selected)
        if year:
            answer = answer.replace("There are", f"There are", 1)
            answer += f" in {year}."
        return "OK", answer

    if text in {"hello", "hi", "hey", "salam", "assalamualaikum"}:
        return "OK", "Bot: Hey! Ask me something about the order dataset."

    return "UNKNOWN", (
        "Bot: I could not match that question to the dataset. "
        "Type 'help' to see examples of questions I can answer."
    )


def main():
    try:
        data = load_data()
    except Exception as error:
        print("Bot: I could not load the dataset.")
        print(f"Details: {error}")
        return

    print("=" * 62)
    print("             E-COMMERCE DATA CHATBOT")
    print("                 DecodeLabs Project 1")
    print("=" * 62)
    print("Bot: Hi! I can answer questions from the supplied order dataset.")
    print("Bot: Type 'help' to see examples or 'bye' to leave.")

    while True:
        message = input("\nYou: ").strip()

        if not message:
            print("Bot: Please type a question.")
            continue

        status, response = get_response(data, message)

        if response:
            print(response)

        if status == "EXIT":
            break


if __name__ == "__main__":
    main()
