# ShareData

Use yahoo_finance_pynterface python package to grab historical data from Yahoo finance

Append indicies and stockNames with the indicies/companies that you require and adjust period for the dates

    indicies = ["^GSPC", "QQQ", "^IXIC"]

    stockNames = ["BLDP", "AAPL", "MSFT", "FCEL", "NVAX", "QCOM", "CSCO", "PLUG", "INTC", "NFLX",
                  "GILT", "GE", "MGIC", "SBUX", "ADBE", "AMZN", "LBTYK", "SINA", "LPSN", "JBLU", "AMAT", "GOOG",
                  "BEAT", "DLTR", "LSCC", "LRCX", "SIRI", "NURO", "TSCO", "LOGI", "OPNT", "CGNX", "GILD", "IIVI",
                  "ADSK", "COST", "CME", "ISRG", "NVDA", "SPNS", "TSEM"]
    
    period = ['2000-01-01','2020-01-20']

Run GetData.py, it will grab the data and save to an .csv file in the folders
