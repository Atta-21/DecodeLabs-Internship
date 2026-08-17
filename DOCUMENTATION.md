# Project Documentation

## 1. Project objective

The goal is to build a chatbot that can answer useful questions about the supplied e-commerce dataset instead of requiring the user to manually inspect the spreadsheet.

## 2. Technology

- Python
- Pandas
- Regular expressions
- Standard Python modules

## 3. Data flow

1. The program loads `ecommerce_orders.csv`.
2. Date, quantity, unit price and total price fields are converted into useful data types.
3. The user's message is cleaned.
4. The chatbot checks the message against its supported question patterns.
5. If a year is mentioned, the matching records are selected.
6. Pandas performs the calculation.
7. The result is displayed in a simple sentence.

## 4. Main functions

### `load_data()`
Loads the supplied dataset and prepares numeric/date columns.

### `clean_text()`
Handles basic punctuation and common casual typing.

### `filtered_data()`
Checks whether the user mentioned a year and filters the data accordingly.

### `answer_total_sales()`
Calculates the sum of `TotalPrice`.

### `answer_order_count()`
Counts the records in the selected data.

### `answer_top_product()`
Groups the data by product and finds the highest total quantity.

### `answer_average_order()`
Calculates the mean of `TotalPrice`.

### `answer_cancelled()` and `answer_delivered()`
Count orders by `OrderStatus`.

### `answer_top_payment()`
Finds the payment method with the highest number of orders.

### `answer_top_referral()`
Finds the referral source with the highest number of orders.

### `answer_top_customer()`
Groups sales by customer and finds the customer with the highest total order value.

## 5. Why the chatbot is rule-based

The project uses predefined question patterns instead of an online language model. This keeps the program understandable and demonstrates programming concepts such as conditions, functions, string handling, data filtering and aggregation.

## 6. Testing plan

Test at least these inputs:

- `total sales`
- `total sales in 2024`
- `how many orders`
- `how many cancelled orders`
- `how many delivered orders`
- `which product was ordered the most`
- `which payment method is most common`
- `which referral source has the most orders`
- `which customer spent the most`
- `average order value`
- `total quantity sold`
- `most used coupon`
- `summary`
- `help`
- `bye`

Also test casual variations such as:

- `whats total sales`
- `tell me total sales`
- `total sales pls`

## 7. Limitations

The bot only supports question patterns that have been programmed. A question outside those patterns may be rejected even when the dataset contains the required information.

## 8. Possible improvements

The next version could include a GUI, charts, more flexible natural-language matching, additional dataset filters and a conversation history.
