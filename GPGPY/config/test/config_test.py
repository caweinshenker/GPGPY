import nose
from nose.tools import assert_equal, assert_true, assert_false, assert_raises
from ..config import Config
from pprint import pprint
import os

testfile_good = os.path.dirname(os.path.abspath(__file__)) + "/fixtures/gpgpusim.config"
testfile_bad = os.path.dirname(os.path.abspath(__file__)) + "/fixtures/gpgpusim_invalid.config"
outfile = os.path.dirname(os.path.abspath(__file__)) + "/fixtures/config_test_output.config"


class TestConfig:

	def setup(self):
		self.c = Config()
		self.c.load_config(testfile_good)
	
	def teardown(self):
		self.c = None


	def test_config_file_write(self):
		self.c.write(outfile)

	
	def test_broken_config_file(self):
		self.c = Config()
		assert_raises(ValueError, self.c.load_config, testfile_bad)

	
	def test_get_and_set_item(self):
		assert_true(self.c["-gpgpu_dram_buswidth"] == "4")
		self.c["-gpgpu_dram_buswidth"] = 5
		assert_true(self.c["-gpgpu_dram_buswidth"] == "5")

			

	

