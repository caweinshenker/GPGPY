"""
Colin Weinshenker -- caweinshenker@email.wm.edu
11/27/2016

Manages SQLite3 database connections 
"""

import sqlite3

class SQLiteManager(object):
	"""Uses context manager pattern to handle database transactions"""

	def __init__(self, database_file):
		"""Stores database file location"""
		self.db = database_file

	def __enter__(self, database):
		self.conn = sqlite3.connect(database)
		self.cursor = self.conn.cursor()

	def __exit__(self):
		self.conn.close()
	

	def __scrub_table_name(table_name):
		return ''.join(chr for chr in table_name if chr.isalnum())
	
	def fieldnames(table_name):
		""" Return list of column names gives table name"""
		table_name == self.__scrub_table_name(table_name)
		tmp_cursor = self.conn.cursor()
		tmp_cursor.execute("SELECT * from {}".format(table_name))
		return [f[0] for f in tmp_cursor.description]	

	def execute(query, *args):
		self.cursor.execute(query, [args])



