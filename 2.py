from pykrx import stock

tickers = stock.get_elw_ticker_list('220614')
print(tickers)
