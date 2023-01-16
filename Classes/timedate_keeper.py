import pandas as pd
from datetime import datetime, timedelta

class timedate_keeper():
    #function to register and increment date
    def register_date():
        #see if items today expired and register that on bought csv
        curent_date = datetime.today().strftime('%Y-%m-%d')
        items = pd.read_csv("bought.csv")
        items["expiration_date"] = pd.to_datetime(items["expiration_date"], format='%Y-%m-%d')
        item_index = items[(items["expiration_date"] < curent_date)].index.tolist()
        for item in item_index:
            items.loc[item, "ammount_expired"] = items.loc[item, "in_stock"]
            items.loc[item, "in_stock"] = 0
        items.to_csv("bought.csv", index=False)
       
    #function to see if the time was profided in the correct format
    def date_checker(date_provided):
        try:
            if date_provided != datetime.strptime(date_provided, "%Y-%m-%d").strftime("%Y-%m-%d"):
                raise ValueError
            return True
        except ValueError:
            print("The date was not provided in the correct format. Please provide it in the format: YYYY-MM-DD")
            return False
