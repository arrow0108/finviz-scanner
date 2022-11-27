import requests
import csv
import time

# Globals
NEW_52_HIGH_SCAN = 'https://elite.finviz.com/export.ashx?v=111&f=cap_smallover,ind_stocksonly,ipodate_01-01-2007x,sh_price_o30,ta_highlow52w_nh,ta_perf_4w20o,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='
TEN_PERCENT_TO_52_HIGH_SCAN = 'https://elite.finviz.com/export.ashx?v=111&f=cap_smallover,ind_stocksonly,ipodate_01-01-2007x,sh_price_o30,ta_highlow52w_b0to10h,ta_perf_4w20o,ta_sma200_sb50,ta_sma50_pa&ft=4&auth='


def scan(URL):
    url = URL + os.environ.get(USERMAIL, '')
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

scan(NEW_52_HIGH_SCAN)
time.sleep(3)
scan(TEN_PERCENT_TO_52_HIGH_SCAN)
