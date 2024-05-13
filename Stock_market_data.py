def average_closing_price(stock_data, stock_symbol, start_date, end_date):
    total_closing_price = 0
    count = 0
    for symbol, date, closing_price in stock_data:
        if symbol == stock_symbol and start_date <= date <= end_date:
            total_closing_price += closing_price
            count += 1
    if count == 0:
        return f"No data found for {stock_symbol} between {start_date} and {end_date}."
    else:
        return total_closing_price / count

# Sample Data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]


average_price_aapl = average_closing_price(stock_data, "AAPL", "2021-01-01", "2021-01-02")
print("Average closing price of AAPL between 2021-01-01 and 2021-01-02:", average_price_aapl)

average_price_msft = average_closing_price(stock_data, "MSFT", "2021-01-01", "2021-01-02")
print("Average closing price of MSFT between 2021-01-01 and 2021-01-02:", average_price_msft)
