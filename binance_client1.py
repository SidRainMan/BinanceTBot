import argparse
import binance

class BinanceClient1:
    def __init__(self, api_key, api_secret):
        self.client = binance.Client(api_key=api_key, api_secret=api_secret)

    def buy_futures(self, symbol, quantity):
        """Buy a futures contract for a specific token"""
        order = self.client.futures_create_order(
            symbol=symbol,
            side=binance.SIDE_BUY,
            type=binance.ORDER_TYPE_MARKET,
            quantity=quantity
        )
        print('Bought', quantity, 'futures contract for', symbol)

    def sell_futures(self, symbol, quantity):
        """Sell a futures contract for a specific token"""
        order = self.client.futures_create_order(
            symbol=symbol,
            side=binance.SIDE_SELL,
            type=binance.ORDER_TYPE_MARKET,
            quantity=quantity
        )
        print('Sold', quantity, 'futures contract for', symbol)

    def get_price(self, symbol):
        """Get the current live price of a token"""
        ticker = self.client.futures_ticker(symbol=symbol)
        print('Current price of', symbol, 'is', ticker['lastPrice'])

def main():
    parser = argparse.ArgumentParser(description='Interact with Binance API')
    parser.add_argument('api_key', help='Binance API key')
    parser.add_argument('api_secret', help='Binance API secret')
    parser.add_argument('symbol', help='Token symbol')
    parser.add_argument('quantity', type=float, help='Quantity of futures contract')
    parser.add_argument('--buy', action='store_true', help='Buy a futures contract')
    parser.add_argument('--sell', action='store_true', help='Sell a futures contract')
    parser.add_argument('--price', action='store_true', help='Get the current live price of a token')
    args = parser.parse_args()

    client = BinanceClient(args.api_key, args.api_secret)

    if args.buy:
        client.buy_futures(args.symbol, args.quantity)
    elif args.sell:
        client.sell_futures(args.symbol, args.quantity)
    elif args.price:
        client.get_price(args.symbol)
    else:
        print('No action specified')

if __name__ == '__main__':
    main()
