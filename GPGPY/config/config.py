###############################
# Colin Weinshenker
# caweinshenker@email.wm.edu
#
# 12/2016
#
#
######################################


import re
import sys
from .config_constants import *


class Config(object):

	def __init__(self):
		self._load_defaults()

	def __getitem__(self, key):
		return self._config_dict[key]


	def __setitem__(self, key, value):
		try:
			self._config_dict[key] = str(value)
		except TypeError as e:
			print("Key or value must have a string format")
			raise(e)


	def __str__(self):
		return str(self._config_dict)


	def _load_defaults(self):
		"""Load None as default value for all configuration options"""
		self._config_dict = {}
		for default_config in default_configs:
			for config_option in default_config:
				self._config_dict[config_option] = None


	def load_config(self, config_filename):
		config_file = open(config_filename, "r")
		for line in config_file:
			if re.match("(^#|^\s*\n)", line): continue #Skip comments and blank lines 
			else:
				try: 
					option, value = line.split()[0], " ".join(line.split()[1:])
					if len(line.split()) < 2: raise(ValueError)
					if option not in self._config_dict:
						print("Warning: {} is not a default option for GPGPU-Sim".format(option)) 
						unrecognized_configuration_options.add(option)
					self._config_dict[option] = value
				except ValueError as e:
					print("ERROR: Option {} found, but no arguments were given".format(option))
					raise(e)	

	def write_config(self, config_filename):

		def _write_option(config_file, option):
			if self._config_dict[option] is not None: #Skip unset parameters to accept GPGPU-sim defaults
				config_file.write(option + " ")
				config_file.write(self._config_dict[option] + " \n")

		def _write_header(config_file, config):

			config_file.write("###########################\n")
			config_file.write("# " + config.name + "\n")

		config_file = open(config_filename, "w")
		for config in default_configs:
				_write_header(config_file, config)
				for option in config:
					_write_option(config_file, option)
		config_file.close()
				
							   
				      
