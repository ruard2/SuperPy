# Assignment files
# Student Ruard Stolper

import argparse
from Classes.Router import Router
from Classes.new_user import new_user
from Classes.timedate_keeper import timedate_keeper
import os

#in this function the parser is set up
def parser():
	parser = argparse.ArgumentParser(prog="main.py", description="Keep track of supermarket inventory.")
	parser.add_argument('action',
							action='store',
							choices=['buy', 'sell', 'advance-time','report', 'export'],
							help='the action to perform: buy, sell, advance time, report, export',
							metavar='action',
							nargs='?',
							type=str,)
	subparsers = parser.add_subparsers(help="type of action", dest="command")
	subparsers.required = True

	buy_parser = subparsers.add_parser("buy", help="Register bought product")
	buy_parser.add_argument(
		"--product", 
		dest="product", 
		type=str, 
		help="product name", 
		required=True
	)
	buy_parser.add_argument(
		"--buy-price",
		type=float,
		dest="price",
		help="buy price per product",
		required=True,
	)
	buy_parser.add_argument(
		"--quantity",
		type=int,
		dest="quantity",
		help="quantity of product",
		default=1,
	)
	buy_parser.add_argument(
		"--buy-date",
		type=str,
		dest="buy_date",
		help="product buy date (format YYYY-MM-DD)",
		required=True,
	)
	buy_parser.add_argument(
		"--exp-date",
		type=str,
		dest="exp_date",
		help="product expiration date (format YYYY-MM-DD)",
		required=True,
	)

	sell_parser = subparsers.add_parser("sell", help="Register sold product")
	sell_parser.add_argument(
		"--product", 
		dest="product", 
		type=str, 
		help="product name", 
		required=True
	)
	sell_parser.add_argument(
		"--sell-date",
		type=str,
		dest="sell_date",
		help="product sold date (format YYYY-MM-DD)",
		required=True,
	)
	sell_parser.add_argument(
		"--sold-price",
		type=float,
		dest="price",
		help="buy price per product",
		required=True,
	)
	sell_parser.add_argument(
		"--quantity",
		type=int,
		dest="quantity",
		help="quantity of products sold",
		default=1,
	)
	
	advancetime_parser = subparsers.add_parser("advance-time", help="Provide us the ammount of days you want to advance")
	advancetime_parser.add_argument(
		"--increment", 
		dest="increment", 
		type=int, 
		help="how many days do you want to advance", 
		required=True
	)

	report_parser = subparsers.add_parser("report", help="Report profit and revenue over provided ammount of time")
	report_parser.add_argument(
		"--product", 
		dest="product", 
		type=str, 
		help="on what product do you want to see the provit and revenue, if all command is: 'all'", 
		required=True
	)
	
	report_parser.add_argument(
		"--start-date", 
		dest="start_date", 
		type=str, 
		help="start date of revenue and profit reporting, (format YYYY-MM-DD)", 
		required=True
	)

	report_parser.add_argument(
		"--end-date", 
		dest="end_date", 
		type=str, 
		help="end date of revenue and profit reporting, (format YYYY-MM-DD)", 
		required=True
	)

	export_parser = subparsers.add_parser("export", help="Export any data in excel, csv or pdf on a specific product or all producs")
	export_parser.add_argument(
		"--product", 
		dest="product", 
		type=str, 
		help="Provide the product name you want more information on, if all the command is: 'all'", 
		required=True
	)
	
	export_parser.add_argument(
		"--start-date", 
		dest="start_date", 
		type=str, 
		help="start date of reporting, (format YYYY-MM-DD)", 
		required=True
	)

	export_parser.add_argument(
		"--end-date", 
		dest="end_date", 
		type=str, 
		help="end date of reporting, (format YYYY-MM-DD)", 
		required=True
	)

	export_parser.add_argument(
		"--data", 
		dest="data", 
		type=str, 
		help="What do you wnat to export? Stock sold or stock baught? Please use the keyword: bought/sold", 
		required=True
	)

	export_parser.add_argument(
		"--file-structure", 
		dest="file_structure", 
		type=str, 
		help="In what file format do you want to export, options: csv, excel", 
		required=True
	)

	args = parser.parse_args()
	Router(args)

if __name__ == "__main__":
	#block to check if file exist and if not write data files and folder for exporting
	isFile = os.path.isfile("bought.csv")
	if isFile == False:
		os.makedirs("Exported files") 
		new_user()	
	timedate_keeper.register_date()
	parser()