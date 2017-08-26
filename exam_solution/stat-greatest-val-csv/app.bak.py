"""Stat-greatest-val-csv."""


import csv


class Statgreatestval:
	"""."""

	def __init__(self):
		"""."""
		self.__sheet = []
		self.__max_row = 16
		self.__max_col = 16
		self.__rows = 0
		self.__cols = 0

	def writesheet(self):
		"""Generate new csv data."""
		with open('data02.csv', 'w+') as file:

			try:
				fieldnames = sorted(self.__sheet[0])
			except IndexError:
				print('Sheet is empty')
				return None

			dw = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
			dw.writeheader()

			for data in self.__sheet:
				dw.writerow(data)

	def readsheet(self):
		"""Read from csv data."""
		with open('data01.csv', 'r') as file:
			dict_data = csv.DictReader(file)
			for data in dict_data:
				self.__sheet.append(data)

	def getrows(self):
		"""Row count."""
		self.__rows = len(self.__sheet)
		
		return self.__rows

	def setrows(self, rowcount):
		"""Set row count."""
		self.__rows += int(rowcount)

	def getcols(self):
		"""Col count."""
		for data in self.__sheet:
			self.__cols = len(data)
			break

		return self.__cols

	def getdata(self):
		"""."""
		return self.__sheet


class Stats:
	"""."""

	def __init__(self, row, col, data):
		"""."""
		self.__greatest_value(data)

	def __greatest_value(self, sheetdata):
		"""Get greatest value."""
		retval = {}
		retval[fieldnames[0]] = 'Greatest'
		retval[fieldnames[1]] = 'Value'

		for key in fieldnames[2::]:
			temp_list = []

			for data in sheetdata:
				temp_list.append(data.get(key, 0))

			retval[key] = max(temp_list)

		return retval

if __name__ == "__main__":
	sgv = Statgreatestval()
	sgv.readsheet()
	sgv.writesheet()
