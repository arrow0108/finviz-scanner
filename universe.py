import requests
import csv
import click
import time

# Globals
UNIVERSE = 'https://elite.finviz.com/export.ashx?v=151&f=ind_stocksonly,sh_avgvol_o500,sh_short_o5,ta_beta_o1,ta_sma200_sb50,ta_sma50_pa&auth='

FILTERS = [UNIVERSE]
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
