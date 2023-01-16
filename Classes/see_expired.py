#This class shows what products will be expired at incremented day in the future

import pandas as pd
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table


class see_expired():
	def __init__(self, increment=0):
		projected_time = (datetime.now() + timedelta(days=increment)).strftime('%Y-%m-%d')
		items = pd.read_csv("bought.csv")
		items["expiration_date"] = pd.to_datetime(items["expiration_date"], format='%Y-%m-%d')
		item_index = items[(items["expiration_date"] < projected_time)].index.tolist()

		print(f"The following products are expired on {projected_time}\n")
		
		#Report data in Rich table
		table = Table(title="Expired")
		table.add_column("Product", style="cyan", no_wrap=True)
		table.add_column("Ammount", style="magenta")

		for item in item_index:
			table.add_row(f'{items.loc[item,"product_name"]}', f'{items.loc[item,"ammount_bought"]}')

		console = Console()
		console.print(table)

