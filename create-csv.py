#!/usr/bin/env python3

import yfinance as yf
import os
import sys
import json

input_file = "stocks.lst"
output_file = "report.csv"
data_dir = "./data"

if not os.path.exists(input_file):
    print("Input file %s not found" % input_file)
    sys.exit(1)

fields = [
    'symbol',
    'shortName',
    'sector',
    'industry',
    'recommendationKey',
    'currentPrice',
    'shortRatio',
    'fullTimeEmployees',
    'marketCap',
    'totalRevenue',
    'revenueGrowth',
    'ebitdaMargins',
    'profitMargins',
    'grossMargins',
    'earningsGrowth',
    'dividendYield',
    'debtToEquity',
    'forwardEps',
    'trailingEps',
    'trailingEps',
    'forwardPE',
    'pegRatio',
]


with open(input_file, "r", encoding="utf-8") as fh_tickers:
    with open(output_file, "w", encoding="utf-8") as fh_report:
        record_line = ';'.join(fields)
        record_line += '\n'
        fh_report.write(record_line)
        while True:
            line = fh_tickers.readline().rstrip()
            if not line:
                break
            print(line)
            ticker_file = os.path.join(data_dir, '{0}.json'.format(line))
            json_data = open(ticker_file, "r", encoding="utf-8").read()
            ticker_data = json.loads(json_data)
            record_list = []
            for field in fields:
                if field in ticker_data:
                    record_list.append(str(ticker_data[field]))
                else:
                    record_list.append("")
            record_list.append('\n')
            # print(type(record_list))
            record_line = ';'.join(record_list)
            # print(type(record))
            fh_report.write(record_line)
