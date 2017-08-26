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
			csvwriter = csv.writer(file, delimiter=',', lineterminator='\n')
			for data in self.__sheet:
				csvwriter.writerow(data)

	def readsheet(self):
		"""Read from csv data."""
		with open('data01.csv', 'r') as file:
			csvdata = list(csv.reader(file))
			self.__sheet = [meta[:self.__max_col] for meta in csvdata[:self.__max_row]]

	def getrows(self):
		"""Row count."""
		self.__rows = len(self.__sheet)
		
		return self.__rows

	def setrows(self, new_rowcount):
		"""Set row count."""
		self.__rows = int(new_rowcount)

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
		self.__sheetdata = data
		self.__greatest_value(col)

	def __greatest_value(self, col):
		"""Get greatest value."""
		self.__greatest_val_row = ['Greatest', 'Value']

		for count in range(col):
			if count in (0, 1):
				continue
			self.__greatest_val_row.insert(count,
										   (max([int(data[count]) for data in self.__sheetdata[1:]])))

		self.__sheetdata.append(self.__greatest_val_row)

	def writedata(self):
		"""Make output."""
		try:
			with open('data02.csv', 'w') as file:
				csvwriter = csv.writer(file, delimiter=',', lineterminator='\n')

				for data in self.__sheetdata:
					csvwriter.writerow(data)
		except:
			print('Appending greatest value failed')
		else:
			for data in self.__sheetdata:
				print(' '.join([str(x) for x in data]))


if __name__ == "__main__":
	sgv = Statgreatestval()
	sgv.readsheet()
	sts = Stats(sgv.getrows(), sgv.getcols(), sgv.getdata())
	sgv.setrows(sgv.getrows() + 1)
	sgv.writesheet()
	sts.writedata()

