import pandas as pd
from csv import writer
import csv
from Classes.timedate_keeper import timedate_keeper

#this class adds a new product to bought csv
class addproduct():
	def __init__(self, id, item, price, quantity, buy_date, exp_date, in_stock, ammount_expired):		
		if timedate_keeper.date_checker(buy_date) and timedate_keeper.date_checker(exp_date) == False:
			return

		#register item as bought in the csv file					
		new_item = {
		"id": len(pd.read_csv('bought.csv')),
		"product_name" : item,
		"buy_date" : buy_date,
		"buy_price" : price,	
		"ammount_bought" : quantity,
		"expiration_date" : exp_date,
		"ammount_expired" : ammount_expired,
		"in_stock" : in_stock,
		}

		items = pd.read_csv("bought.csv")
		items = items.append(new_item, ignore_index=True)		
		items.to_csv("bought.csv", index=False)
		print("\nYour product has been added")