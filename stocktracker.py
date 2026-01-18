
stock_price_list = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140,
    "AMZN": 130
}

user_portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_price_list.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_price_list:
        print("❌ Stock not found. Please choose from the available list.")
        continue

    try:
        stock_quantity = int(input("Enter quantity: "))
        if stock_quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    user_portfolio[stock_name] = user_portfolio.get(stock_name, 0) + stock_quantity

print("\n📁 Portfolio Summary")
for stock, qty in user_portfolio.items():
    stock_value = stock_price_list[stock] * qty
    total_investment += stock_value
    print(f"{stock} | Quantity: {qty} | Value: ₹{stock_value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Optional: Save to file
save_choice = input("\nDo you want to save the summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("stock_portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in user_portfolio.items():
            value = stock_price_list[stock] * qty
            file.write(f"{stock} - Quantity: {qty}, Value: ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_investment}\n")

    print("✅ Portfolio saved successfully in stock_portfolio.txt")
