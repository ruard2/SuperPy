import pandas as pd
from csv import writer
import csv
from Classes.timedate_keeper import timedate_keeper

class register_sold_product():
	def __init__(self, product, sell_date, sell_price, ammount):	
		#check if date was provided in te correct format
		if timedate_keeper.date_checker(sell_date) == False:
			return

		profit_on_item = sell_price/ammount
		profit=0
		total=0
		total_profit=0

		#see if item exist, if enough and update stock in bought.csv and also calculate profit on products sold,
		items = pd.read_csv("bought.csv")
		item_exist = (items["product_name"] == product).any()
		if item_exist == False:
			print("Item does not exist in inventory")
		if item_exist:	
			#see if there is enough of the product in stock to sell it		
			item_index = (items[(items["product_name"] == product)]).index.tolist()
			total_in_stock = 0
			for item in item_index:
				total_in_stock += items.loc[item, "in_stock"]
			
			if total_in_stock < ammount:
				print(f"You do not have enough to sell this much. Available ammount: {total_in_stock}")
			#if there is enough stock, calculate the profit made on sale and update in_stock in bought.csv
			else:
				for item in item_index:
					if items.loc[item, "in_stock"] >= ammount:
						items.loc[item, "in_stock"] = items.loc[item, "in_stock"] - ammount
						total_profit = total_profit + ((profit_on_item - items.loc[item, "buy_price"]/items.loc[item, "ammount_bought"]) * ammount)
						break

					else:
						ammount_taken = items.loc[item, "in_stock"] 
						ammount = ammount - ammount_taken 	 	
						items.loc[item, "in_stock"] = 0
						profit = (profit_on_item - items.loc[item, "buy_price"]/items.loc[item, "ammount_bought"])*ammount_taken
						total_profit += profit
						items_sold = pd.read_csv("sold.csv")
						items_sold.loc[item, "profit"] = profit
			
			items.to_csv("bought.csv", index=False)
			print(f'The order is registerd!')
		
			#register new sold item to sold list
			items_sold = pd.read_csv("sold.csv")
			new_item = {
			"id": len(pd.read_csv('sold.csv')),
			"product_name" : product,
			"sell_date" : sell_date,
			"sell_price" : sell_price,
			"ammount" : ammount,
			"profit" : total_profit,
			}
			items_sold = items_sold.append(new_item, ignore_index=True)
			items_sold.to_csv("sold.csv", index=False)

