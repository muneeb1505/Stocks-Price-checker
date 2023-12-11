import requests

def get_stock_price(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "GLOBAL_QUOTE"

    # Make API request
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the request was successful
    if "Global Quote" in data:
        stock_data = data["Global Quote"]
        return stock_data["05. price"]
    else:
        return None

def main():
    # Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
    api_key = 'YOUR_API_KEY'
    
    # Get stock symbol from the user
    symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()

    # Fetch and display the stock price
    stock_price = get_stock_price(symbol, api_key)

    if stock_price is not None:
        print(f"The current price of {symbol} is ${stock_price}")
    else:
        print(f"Failed to retrieve stock data for {symbol}")

if __name__ == "__main__":
    main()
