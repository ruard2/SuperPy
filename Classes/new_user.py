import csv
from csv import writer
import pandas as pd

# if the program is executed for the first time this creates new databases
class new_user():
	def __init__(self):
		data_frame_bought = pd.DataFrame(
			columns=[
				"id",
				"product_name",
				"buy_date",
				"buy_price",
				"ammount_bought",
				"expiration_date",
				"ammount_expired",
				"in_stock",
				]
				)
		data_frame_bought.to_csv("bought.csv", index = False)			

		data_frame_sold = pd.DataFrame(
			columns=[
			"id", 
			"product_name", 
			"sell_date", 
			"sell_price", 
			"ammount",
			"profit"]
			)
		data_frame_sold.to_csv("sold.csv", index = False)