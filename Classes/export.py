#This class exports asked for data into asked for file structure
import pandas as pd
import csv
from Classes.timedate_keeper import timedate_keeper

class export():
	def __init__(self, item, start_date, end_date, data, file_structure):	
		if timedate_keeper.date_checker(start_date) and timedate_keeper.date_checker(end_date) == False:
			return
		#This function profides item index on the asked for data
		if data == "sold" or data == "Sold":
			items_sold = pd.read_csv("sold.csv")
			if item == "all" or item == "All":
				item_index = items_sold[((items_sold["sell_date"] >= start_date)
					&(items_sold["sell_date"] <= end_date))].index.tolist()
			else:
				item_index = items_sold[((items_sold["sell_date"] >= start_date)
					&(items_sold["sell_date"] <= end_date)
					&(items_sold["product_name"]==item))].index.tolist()

		elif data == "bought" or data == "Bought":
			items_bought = pd.read_csv("bought.csv")
			if item == "all" or item == "All":
				item_index = items_sold[((items_sold["sell_date"] >= start_date)
					&(items_sold["sell_date"] <= end_date))].index.tolist()
			else: 
				item_index = items_bought[((items_bought["buy_date"] >= start_date)
					&(items_bought["buy_date"] <= end_date)
					&(items_bought["product_name"]==item))].index.tolist()
		else:
			print("You used the wrong keywords, please try again")

		if file_structure == "excel" or file_structure == "xcl" or file_structure == "Excel":
			export.to_excel(item_index, data, start_date, end_date)
		if file_structure == "csv" or file_structure == "CSV" or file_structure == "Csv":
			export.to_csv(item_index, data, start_date, end_date)
	
	#function to export to excel		
	def to_excel(item_index, data, start_date, end_date):
		if data == "sold" or data == "Sold":
			items_sold = pd.read_csv("sold.csv")
			items_sold = items_sold.iloc[item_index]
			SoldExcelFile = pd.ExcelWriter(f"Exported files/Sold {start_date}-{end_date}.xlsx")
			items_sold.to_excel(SoldExcelFile, index=False)
			SoldExcelFile.save()
			print(f"Your data is exported and could be found in the folder 'Exported files' as 'Sold {start_date}-{end_date}.xlsx")
		elif data == "bought" or data == "Bought":
			items_bought = pd.read_csv("bought.csv")
			items_bought = items_bought.iloc[item_index]
			BoughtExcelFile = pd.ExcelWriter(f"Exported files/Bought {start_date}-{end_date}.xlsx")
			items_bought.to_excel(BoughtExcelFile, index=False)
			BoughtExcelFile.save()
			print(f"Your data is exported and could be found in the folder 'Exported files' as 'Bought {start_date}-{end_date}.xlsx")		

	#function to export to csv
	def to_csv(item_index, data, start_date, end_date):
		if data == "sold" or data == "Sold":
			items_sold = pd.read_csv("sold.csv")
			items_sold = items_sold.iloc[item_index]
			items_sold.to_csv(f"Exported files/Sold {start_date}-{end_date}.csv", index=False)
			print(f"Your data is exported and could be found in the folder 'Exported files' as 'Sold {start_date}-{end_date}.csv")
		elif data == "bought" or data == "Bought":
			items_bought = pd.read_csv("bought.csv")
			items_bought = items_bought.iloc[item_index]
			items_bought.to_csv(f"Exported files/Bought {start_date}-{end_date}.csv", index=False)
			print(f"Your data is exported and could be found in the folder 'Exported files' as 'Bought {start_date}-{end_date}.csv")			
	

	


