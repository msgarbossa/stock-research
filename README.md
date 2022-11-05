
## Setup

### Python virtual environment

```
sudo apt install -y python3-virtualenv
mkdir ~/venv
virtualenv -p python3 ~/venv/yfinance
. ~/venv/yfinance/bin/activate
pip3 install yfinance

cat <<EOF > envs.local
. ~/venv/yfinance/bin/activate
EOF
```

### Watch List

In the same directory as the Python scripts, put a list of stock tickers in a file named `stocks.lst`.  One stock ticker per line.  No blank spaces or comments.

## Usage

Source environment file with Python virtual environment with the yfinance module.
```
. envs.local
```

Refresh data for all stocks in the list.  The data will be written to individual files at ./data/TICKER.json.
```
./refresh-data.py
```

Create csv report file from data.  The file will be named report.csv.
```
./create-csv.py
```

The report.csv file can be opened as a spreadsheet in LibreOffice Calc.
- separated by: Semicolon

