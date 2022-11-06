#!/usr/bin/env python3

import yfinance as yf
import os
import sys
import json

# Help message
def usage(exit_code=0):
    """ Display help message if invalid syntax. """
    print(os.path.basename(__file__) + ' <ticker>')
    sys.exit(exit_code)

if len(sys.argv) != 2:
    print("Exactly 1 argument required.")
    usage(1)

data_dir = "./data"

def get_stock_data(ticker):
    outfile = os.path.join(data_dir, '{0}.json'.format(ticker))
    print(outfile)
    ticker_obj = yf.Ticker(ticker)
    with open(outfile, "w", encoding="utf-8") as fo:
        json.dump(ticker_obj.info, fo, ensure_ascii=True, indent=4, default=str)

if __name__ == '__main__':
    ticker = sys.argv[1]
    get_stock_data(ticker)

