# E-commerce Data Chatbot — DecodeLabs Project 1

## Overview

This project turns the supplied e-commerce order dataset into a small interactive chatbot.

Instead of giving fixed jokes or general answers, the chatbot reads the dataset and calculates answers from the actual records. A user can ask about sales, orders, products, customers, payments and marketing information.

## Dataset

The project uses the supplied Excel dataset, which is copied into the project as:

`ecommerce_orders.csv`

The chatbot expects fields including:

- OrderID
- Date
- CustomerID
- Product
- Quantity
- UnitPrice
- OrderStatus
- PaymentMethod
- CouponCode
- ReferralSource
- TotalPrice

## Main features

- Total sales
- Total orders
- Average order value
- Total quantity sold
- Cancelled orders
- Delivered orders
- Most ordered product
- Most common payment method
- Referral source with the most orders
- Customer with the highest total order value
- Most frequently used coupon
- Year-based filtering when a year is included in the question
- Dataset summary
- Help menu
- Simple casual-typing support
- Unknown-question handling

## Example questions

```text
total sales
total sales in 2024
how many orders
how many cancelled orders
how many delivered orders
which product was ordered the most
which payment method is most common
which referral source has the most orders
which customer spent the most
what is the average order value
what is the total quantity sold
most used coupon
summary
help
bye
```

## Run the project

1. Install Python 3.x.
2. Open this folder in VS Code.
3. Make sure `chatbot.py` and `ecommerce_orders.csv` are in the same folder.
4. Install the required packages:

```text
pip install pandas openpyxl
```

5. Run:

```text
python chatbot.py
```

## How it works

The chatbot first loads the dataset with pandas. It then cleans the user's question, checks which type of request it looks like, and performs the relevant calculation on the data.

For example, if the user asks for total sales, the program sums the `TotalPrice` column. If a year is included, the records are filtered to that year first.

## Limitations

This is a rule-based data chatbot. It does not understand every possible sentence and it does not use a generative AI API. The available answers are based on the columns and information present in the supplied dataset.

## Future enhancements

- Add a graphical interface.
- Add charts and visual reports.
- Support more natural language variations.
- Add more filters such as product, payment method or order status.
- Store a conversation history.
