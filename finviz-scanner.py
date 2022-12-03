import requests
import csv
import click
import time

# Globals
NEW_52_HIGH_SCAN = 'https://elite.finviz.com/export.ashx?v=111&f=sh_avgvol_o500,ta_beta_o0.5,cap_smallover,ind_stocksonly,ipodate_01-01-2002,sh_price_o30,ta_highlow52w_nh,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='
TEN_PERCENT_TO_52_HIGH_SCAN = 'https://elite.finviz.com/export.ashx?v=111&f=sh_avgvol_o500,ta_beta_o0.5,cap_smallover,ind_stocksonly,ipodate_01-01-2002,sh_price_o30,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='
PRCT70_ABOVE_52W_LOW_SCAN = 'https://elite.finviz.com/export.ashx?v=111&f=sh_avgvol_o500,ta_beta_o0.5,cap_smallover,ind_stocksonly,ipodate_01-01-2002,sh_price_o30,ta_highlow52w_a70h,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='

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
    scan(NEW_52_HIGH_SCAN, username)
    time.sleep(3)
    scan(TEN_PERCENT_TO_52_HIGH_SCAN, username)
    time.sleep(3)
    scan(PRCT70_ABOVE_52W_LOW_SCAN, username)

if __name__ == '__main__':
    print_scan_results()
