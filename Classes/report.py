#This class calculate and report the total revenue, total profit, total products sold and left

import pandas as pd
import csv
from Classes.timedate_keeper import timedate_keeper
from rich.console import Console
from rich.table import Table

class report():
	def __init__(self, item, start_date, end_date):	
		#check if date was provided in te correct format
		if timedate_keeper.date_checker(start_date) and timedate_keeper.date_checker(end_date) == False:
			return

		#local variables
		total_revenue = 0
		total_profit = 0
		total_sold = 0
		total_left = 0

		#calculate data
		items_sold = pd.read_csv("sold.csv")
		items_bought = pd.read_csv("bought.csv")
		
		if item == "all" or item == "All":
			item_index = items_sold[((items_sold["sell_date"] >= start_date)
				&(items_sold["sell_date"] <= end_date))].index.tolist()

			for i in item_index:
				total_sold += items_sold.loc[i,"ammount"]
				total_revenue += items_sold.loc[i,"sell_price"]
				total_profit += items_sold.loc[i, "profit"]
			
			item_index = (items_bought).index.tolist()
			for i in item_index:
				total_left += items_bought.loc[i, "in_stock"]
				
		elif item in items_sold.values:
			item_index = items_sold[((items_sold["sell_date"] >= start_date)
				&(items_sold["sell_date"] <= end_date)
				&(items_sold["product_name"]==item))].index.tolist()

			for i in item_index:
				total_sold += items_sold.loc[i,"ammount"]
				total_revenue += items_sold.loc[i,"sell_price"]
				total_profit += items_sold.loc[i,"profit"]

			item_index = (items_bought[(items_bought["product_name"] == item)]).index.tolist()
			for item in item_index:
				total_left += items_bought.loc[item, "in_stock"]
		
		else: 
			print("This item was never sold, please try again")

		#Report data in Rich table
		table = Table(title="Report")

		table.add_column("", style="cyan", no_wrap=True)
		table.add_column("Ammount", style="magenta")

		table.add_row("Amount Sold", f'{total_sold}')
		table.add_row("Revenue made" , f'{total_revenue}')
		table.add_row("Profit made", f'{total_profit}')
		table.add_row("Products left in stock", f'{total_left}')

		console = Console()
		console.print(table)

