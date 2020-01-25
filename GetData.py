import yahoo_finance_pynterface as yahoo
import pandas as pd

if __name__ == '__main__':

    indicies = ["^GSPC", "QQQ", "^IXIC"]

    stockNames = ["BLDP", "AAPL", "MSFT", "FCEL", "NVAX", "QCOM", "CSCO", "PLUG", "INTC", "NFLX",
                  "GILT", "GE", "MGIC", "SBUX", "ADBE", "AMZN", "LBTYK", "SINA", "LPSN", "JBLU", "AMAT", "GOOG",
                  "BEAT", "DLTR", "LSCC", "LRCX", "SIRI", "NURO", "TSCO", "LOGI", "OPNT", "CGNX", "GILD", "IIVI",
                  "ADSK", "COST", "CME", "ISRG", "NVDA", "SPNS", "TSEM"]

    period = ['2000-01-01','2020-01-20']

    for indicie in indicies:
        print(indicie)
        prices = pd.DataFrame(yahoo.Get.Prices(indicie, period=period), columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']).reset_index('Date (UTC)')
        prices['Date (UTC)'] = prices['Date (UTC)'].dt.date
        prices.to_csv("Indicies/" + indicie + ".csv", index=False)


    for stock in stockNames:
        print(stock)

        prices = pd.DataFrame(yahoo.Get.Prices(stock, period=period), columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']).reset_index('Date (UTC)')
        prices['Date (UTC)'] = prices['Date (UTC)'].dt.date

        try:
            dividend = pd.DataFrame(yahoo.Get.Dividends(stock, period=period), columns=['Dividends']).reset_index('Date (UTC)')
            dividend['Date (UTC)'] = dividend['Date (UTC)'].dt.date
            prices = prices.merge(dividend, how='outer', left_on='Date (UTC)', right_on='Date (UTC)')

        except:
           prices['Dividends'] = 0.0

        prices.to_csv("Shares/" + stock +".csv", index=False)
