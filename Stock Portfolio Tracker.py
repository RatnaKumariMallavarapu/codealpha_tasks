import datetime

# Hardcoded stock prices (you can easily update these anytime)
stock_prices = {
    "AAPL": 226.84,
    "TSLA": 248.23,
    "GOOGL": 163.95,
    "MSFT": 423.35,
    "AMZN": 189.50,
    "NVDA": 125.67,
    "META": 572.00,
    "NFLX": 912.50
}

print("\n" + "="*60)
print("🚀 STOCK PORTFOLIO TRACKER")
print("="*60)
print("Built with Python • Real-time style report • File export ready")
print(f"Report generated on: {datetime.datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}")
print("-"*60)
print("Available stocks:", ", ".join(stock_prices.keys()))
print("-"*60)

portfolio = {}
total_value = 0.0

while True:
    ticker = input("\n➤ Enter stock ticker (or type 'done' to finish): ").strip().upper()
    
    if ticker == "DONE":
        break
    
    if ticker not in stock_prices:
        print("❌ Stock not found in database. Please use one of the available tickers above.")
        continue
    
    try:
        quantity = float(input(f"➤ Enter quantity of {ticker} shares: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            continue
    except ValueError:
        print("❌ Please enter a valid number for quantity.")
        continue
    
    price = stock_prices[ticker]
    value = price * quantity
    
    portfolio[ticker] = {
        "quantity": quantity,
        "price": price,
        "value": value
    }
    
    total_value += value
    print(f"✅ Added: {quantity:.2f} shares of {ticker} @ ${price:.2f} = ${value:,.2f}\n")

# === FINAL PORTFOLIO SUMMARY ===
if not portfolio:
    print("\n⚠️  No stocks added. Portfolio is empty.")
else:
    print("\n" + "="*60)
    print("📊 FINAL PORTFOLIO SUMMARY")
    print("="*60)
    print(f"{'Ticker':<8} {'Shares':<10} {'Price':<12} {'Value ($)':<15} {'Allocation'}")
    print("-"*60)
    
    for ticker, data in portfolio.items():
        allocation = (data["value"] / total_value * 100) if total_value > 0 else 0
        print(f"{ticker:<8} {data['quantity']:<10.2f} ${data['price']:<11.2f} ${data['value']:<14,.2f} {allocation:6.2f}%")
    
    print("-"*60)
    print(f"{'TOTAL PORTFOLIO VALUE':<30} ${total_value:,.2f}")
    print("="*60)
    print("🎉 Well done! Your portfolio is now tracked perfectly.")

# === OPTIONAL FILE SAVE ===
save_choice = input("\n💾 Would you like to save this report? (y/n): ").strip().lower()
if save_choice == "y":
    # Save as CSV (easy to open in Excel)
    csv_filename = "portfolio_report.csv"
    with open(csv_filename, "w") as f:
        f.write("Ticker,Shares,Price per Share,Total Value,Allocation (%)\n")
        for ticker, data in portfolio.items():
            allocation = (data["value"] / total_value * 100) if total_value > 0 else 0
            f.write(f"{ticker},{data['quantity']:.2f},{data['price']:.2f},{data['value']:.2f},{allocation:.2f}\n")
        f.write(f"TOTAL,,,${total_value:,.2f},\n")
    
    # Save beautiful text summary
    txt_filename = "portfolio_summary.txt"
    with open(txt_filename, "w") as f:
        f.write("STOCK PORTFOLIO TRACKER SUMMARY\n")
        f.write("="*60 + "\n")
        f.write(f"Generated on: {datetime.datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}\n\n")
        f.write(f"{'Ticker':<8} {'Shares':<10} {'Price':<12} {'Value ($)':<15} {'Allocation'}\n")
        f.write("-"*60 + "\n")
        for ticker, data in portfolio.items():
            allocation = (data["value"] / total_value * 100) if total_value > 0 else 0
            f.write(f"{ticker:<8} {data['quantity']:<10.2f} ${data['price']:<11.2f} ${data['value']:<14,.2f} {allocation:6.2f}%\n")
        f.write("-"*60 + "\n")
        f.write(f"{'TOTAL PORTFOLIO VALUE':<30} ${total_value:,.2f}\n")
        f.write("="*60 + "\n")
        f.write("Thank you for using Stock Portfolio Tracker!\n")
    
    print(f"✅ Files saved successfully!")
    print(f"   📄 portfolio_report.csv  (open in Excel)")
    print(f"   📝 portfolio_summary.txt  (clean text report)")
    print("\n🎯 You can now email/share these files instantly!")

print("\n" + "="*60)
print("Thank you for using Stock Portfolio Tracker!")
print("Built to impress • Clean • Professional • Ready for real use")
print("="*60)