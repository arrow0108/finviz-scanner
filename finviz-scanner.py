import requests
import csv
import click
import time

# Globals
NEW_52_HIGH_SCAN = 'https://elite.finviz.com/export.ashx?f=sh_avgvol_o500,cap_smallover,ind_stocksonly,ipodate_01-01-2002x,sh_price_o30,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='

TEN_PERCENT_TO_52_HIGH_SCAN = 'https://elite.finviz.com/export.ashx?v=111&f=sh_avgvol_o500,cap_smallover,ind_stocksonly,ipodate_01-01-2002x,sh_price_o30,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='

PRCT70_ABOVE_52W_LOW_SCAN_EPS30 = 'https://elite.finviz.com/export.ashx?f=sh_avgvol_o500,cap_smallover,ind_stocksonly,ipodate_01-01-2002x,sh_price_o30,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='

PERF_MONTH_ABOVE_20 = 'https://elite.finviz.com/export.ashx?f=cap_smallover,ind_stocksonly,ipodate_01-01-2002x,sh_avgvol_o500,sh_price_o30,ta_perf_4w20o,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='

FILTERS = [PERF_MONTH_ABOVE_20, NEW_52_HIGH_SCAN, TEN_PERCENT_TO_52_HIGH_SCAN, PRCT70_ABOVE_52W_LOW_SCAN]
def scan(URL, username):
    url = f"{URL}{username}"
    response = requests.get(url)
    open("export.csv", "wb").write(response.content)
    with open("export.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        first_line_read = False
        for row in csv_reader:
            if not first_line_read:
                first_line_read = True
                continue
            print(row[1])

@click.command()
@click.option('--username', default="user@email", help='FinViz User Email')
def print_scan_results(username):
    for filter in FILTERS:
        scan(filter, username)
        time.sleep(3)

if __name__ == '__main__':
    print_scan_results()
