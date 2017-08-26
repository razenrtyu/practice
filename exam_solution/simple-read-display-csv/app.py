"""Simple-read-display-csv."""


import csv


class Readfilewritetoconsole:
	"""."""

	def __init__(self):
		"""."""
		self.__data = []

	def readsheet(self):
		"""Read csv file."""
		with open('in.csv', 'r') as file:
			result = csv.reader(file)
			self.__data = list(result)

	def writesheet(self):
		"""Print to console."""
		for meta_data in self.__data:
			print(''.join(['[{}]'.format(x) for x in meta_data]))

if __name__ == "__main__":
	rfc = Readfilewritetoconsole()
	rfc.readsheet()
	rfc.writesheet()
