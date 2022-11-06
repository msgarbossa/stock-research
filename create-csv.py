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

# Pull out interesting fields
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
        # generate header
        record_line = ';'.join(fields)
        record_line += '\n'
        fh_report.write(record_line)

        # loop through list of tickers
        while True:
            ticker = fh_tickers.readline().rstrip()
            if not ticker:
                break
            print(ticker)
            ticker_file = os.path.join(data_dir, '{0}.json'.format(ticker))
            if not os.path.exists(ticker_file):
                print("ticket data file not found: %s" % ticker_file)
                print('Run "./get_one.py {0}" or  "./refresh-data.py"'.format(ticker))
                continue

            # read and parse ticker data file
            json_data = open(ticker_file, "r", encoding="utf-8").read()
            ticker_data = json.loads(json_data)

            # test data is valid
            if "shortName" not in ticker_data:
                print("data file is invalid and will be skipped (shortName not found): %s" % ticker_file)
                continue

            # build record from fields
            record_list = []
            for field in fields:
                if field in ticker_data:
                    record_list.append(str(ticker_data[field]))
                else:
                    record_list.append("")

            # write report line
            record_line = ';'.join(record_list)
            record_line += "\n"
            fh_report.write(record_line)

