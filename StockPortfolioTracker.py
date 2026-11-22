stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

print("===== STOCK PRICE CHECKER =====")
for stock, price in stock_prices.items(): #iterating through the dictionary
    print(stock, ":", price)
portfolio = {}

while True: #loop to keep asking for a valid stock symbol until the user enters one

    stock = input("Enter the stock symbol to check its price: ").strip().upper() #taking input from user and converting it to uppercase

    if stock in stock_prices: #checking if the stock symbol exists in the dictionary
        print(f"The stored price of {stock} is: ${stock_prices[stock]}")
    else:
        print(f"Sorry, {stock} is not in the stock price dictionary.")
        continue #continue to the next iteration of the loop if the stock symbol is not valid
 
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                break

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")
        
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    another_stock = input("Do you want to check another stock? (yes/no): ").strip().lower() #asking user if they want to check another stock    
    if another_stock == "no": #breaking the loop if the user does not want to check another stock
        break

total_value = 0

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_value += investment

    print(f"{stock}: {quantity} shares = ${investment:.2f}")

print(f"\nTotal Portfolio Value: ${total_value:.2f}")

with open("stock_portfolio.txt", "w") as file:
    file.write("===== PORTFOLIO SUMMARY =====\n")
    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${investment:.2f}\n")
    file.write(f"\nTotal Portfolio Value: ${total_value:.2f}\n")    

print("\nYour stock portfolio summary has been saved to 'stock_portfolio.txt'.")