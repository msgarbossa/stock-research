#!/usr/bin/env python3

import yfinance as yf
import os
import sys
import json

input_file = "stocks.lst"
data_dir = "./data"

if not os.path.exists(input_file):
    print("Input file %s not found" % input_file)
    sys.exit(1)

if not os.path.exists(data_dir):
    os.mkdir(data_dir)

def get_stock_data(ticker):
    outfile = os.path.join(data_dir, '{0}.json'.format(ticker))
    print(outfile)
    ticker_obj = yf.Ticker(ticker)
    with open(outfile, "w", encoding="utf-8") as fo:
        json.dump(ticker_obj.info, fo, ensure_ascii=True, indent=4, default=str)

with open(input_file, "r", encoding="utf-8") as fh:
    while True:
        line = fh.readline().rstrip()
        if not line:
            break
        print(line)
        get_stock_data(line)

