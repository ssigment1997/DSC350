stocks = {
    'MCD': 275.50,      # McDonald's
    'SBUX': 105.25,     # Starbucks
    'WMT': 160.40,      # Walmart
    'TGT': 145.10,      # Target
    'COST': 720.30,     # Costco
    'KR': 52.80,        # Kroger
    'YUM': 130.60,      # Yum! Brands
    'DPZ': 410.90,      # Domino's Pizza
    'CMG': 2050.75      # Chipotle Mexican Grill
}

# Ask user to enter a ticker symbol
ticker = input('Enter a company ticker symbol: ').upper()

# Get the stock price if the ticker exists
if ticker in stocks:
    print(f"The stock price for {ticker} is ${stocks[ticker]}")
else:
    print("Ticker not found.")
