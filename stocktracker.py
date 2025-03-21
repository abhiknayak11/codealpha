import yfinance as yf
import pandas as pd
import json

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary to hold stock symbol, shares, and purchase price
        self.load_portfolio()

    def load_portfolio(self):
        """ Load portfolio from a file (if it exists). """
        try:
            with open('portfolio.json', 'r') as file:
                self.portfolio = json.load(file)
        except FileNotFoundError:
            print("No saved portfolio found, starting with an empty portfolio.")

    def save_portfolio(self):
        """ Save portfolio to a file. """
        with open('portfolio.json', 'w') as file:
            json.dump(self.portfolio, file)

    def add_stock(self, symbol, shares, purchase_price):
        """ Add a stock to the portfolio. """
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {
                'shares': shares,
                'purchase_price': purchase_price
            }
        print(f"Added {shares} shares of {symbol} at ${purchase_price:.2f} each.")
        self.save_portfolio()

    def remove_stock(self, symbol, shares):
        """ Remove shares of a stock from the portfolio. """
        if symbol in self.portfolio and self.portfolio[symbol]['shares'] >= shares:
            self.portfolio[symbol]['shares'] -= shares
            if self.portfolio[symbol]['shares'] == 0:
                del self.portfolio[symbol]
            print(f"Removed {shares} shares of {symbol}.")
            self.save_portfolio()
        else:
            print(f"Error: Not enough shares of {symbol} to remove.")

    def get_stock_data(self, symbol):
        """ Fetch real-time stock data using yfinance. """
        stock = yf.Ticker(symbol)
        stock_data = stock.history(period="1d")
        return stock_data['Close'][0] if not stock_data.empty else None

    def display_portfolio(self):
        """ Display the current portfolio. """
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        portfolio_data = []
        total_value = 0
        for symbol, data in self.portfolio.items():
            current_price = self.get_stock_data(symbol)
            if current_price is None:
                print(f"Could not fetch data for {symbol}. Skipping.")
                continue
            current_value = current_price * data['shares']
            portfolio_data.append({
                'symbol': symbol,
                'shares': data['shares'],
                'purchase_price': data['purchase_price'],
                'current_price': current_price,
                'current_value': current_value
            })
            total_value += current_value

        df = pd.DataFrame(portfolio_data)
        print("\nCurrent Portfolio:")
        print(df)
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    
    def portfolio_performance(self):
        """ Display portfolio performance (gains/losses). """
        total_investment = 0
        total_current_value = 0
        for symbol, data in self.portfolio.items():
            purchase_value = data['purchase_price'] * data['shares']
            current_price = self.get_stock_data(symbol)
            if current_price is None:
                continue
            current_value = current_price * data['shares']
            total_investment += purchase_value
            total_current_value += current_value
            gain_loss = current_value - purchase_value
            print(f"{symbol}:")
            print(f"  Purchased at ${data['purchase_price']:.2f}, Shares: {data['shares']}")
            print(f"  Current Price: ${current_price:.2f}, Current Value: ${current_value:.2f}")
            print(f"  Gain/Loss: ${gain_loss:.2f}\n")

        print(f"\nTotal Investment: ${total_investment:.2f}")
        print(f"Total Current Value: ${total_current_value:.2f}")
        print(f"Overall Gain/Loss: ${total_current_value - total_investment:.2f}")

# Main program
def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Portfolio Performance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price per share: "))
            portfolio.add_stock(symbol, shares, purchase_price)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)

        elif choice == '3':
            portfolio.display_portfolio()

        elif choice == '4':
            portfolio.portfolio_performance()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
