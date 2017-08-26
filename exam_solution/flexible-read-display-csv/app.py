"""flexible-read-display-csv."""

import csv
import sys


class Readfilewritetoconsole:
	"""Class."""

	def __init__(self):
		"""Initialize."""
		self.__data_list = []

	def getcell(self, row, col):
		"""Get the value of the spreadsheet at the given row and column."""
		int_row = int(row) - 1
		int_col = int(col) - 1
		retval = None
		
		if int_row >= 0 and int_col >= 0:
			try:
				retval = self.__data_list[int_row][int_col]
			except IndexError:
				print("Invalid Origin")
		else:
			print("Invalid Origin")

		return retval

	def getrowcount(self):
		"""Get the number of rows in the spreadsheet."""
		return len(self.__data_list)

	def getcolcount(self):
		"""Get the number of columns in row."""
		retval = 0
		if self.__data_list:
			try:
				retval = len(self.__data_list[0])
			except IndexError:
				retval = 0

		return retval

	def makesheet(self):
		"""Read the data from inFile."""
		with open('in.csv', 'r') as file:
			reader = csv.reader(file)
			self.__data_list = list(reader)

	def writesheet(self):
		"""Format data to console."""
		for meta_data in self.__data_list:
			print(''.join(['[{}]'.format(x) for x in meta_data]))


if __name__ == "__main__":
	rfc = Readfilewritetoconsole()
	rfc.makesheet()
	rfc.writesheet()

	for arg in sys.argv:

		if arg == 'getrowcount':
			print('Total row count = {}'.format(rfc.getrowcount()))

		if arg == 'getcolcount':
			print('Total col count = {}'.format(rfc.getcolcount()))

		if 'getcell' in arg:
			import re

			paramtext = re.compile('(.)(\\d)(.)(\\d)(.)', re.IGNORECASE|re.DOTALL)
			param = paramtext.search(arg)

			if param:
				row = param.group(2)
				column = param.group(4)

				print('Row - {}, Column - {} have value of "{}"'.format(row, column, rfc.getcell(row, column)))
			else:
				print('Missing parameter - ex. getcell(row, col)')
