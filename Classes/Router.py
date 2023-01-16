#the router receives the arguments profided and executed the arguments

from Classes.addproduct import addproduct
from Classes.register_sold_product import register_sold_product
from Classes.see_expired import see_expired
from Classes.report import report
from Classes.export import export
import csv
from csv import writer

class Router():
	def __init__(self, args):
		if args.command == 'buy':
			addproduct(id=id,
				item=args.product,
				quantity=args.quantity,
				price=args.price,
				buy_date=args.buy_date,
				exp_date=args.exp_date,
				in_stock=args.quantity,
				ammount_expired = args.quantity,
			)
		elif args.command == 'sell':
			register_sold_product(product=args.product,
				sell_date=args.sell_date,
				sell_price=args.price,
				ammount=args.quantity
			)
		elif args.command == 'advance-time':
			see_expired(args.increment)
		elif args.command == 'report':
			report(item=args.product,
				start_date=args.start_date,
				end_date=args.end_date
			)
		elif args.command == 'export':
			export(item=args.product,
				start_date=args.start_date,
				end_date=args.end_date,
				data=args.data,
				file_structure=args.file_structure,
				)
		else:
			quit()

