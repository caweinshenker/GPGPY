import nose
from nose.tools import assert_equal, assert_true, assert_false, assert_raises
from ..config import Config
from pprint import pprint


class TestConfig:


	def setup(self):
		self.c = Config()
		self.c.load_config("fixtures/gpgpusim.config")
	
	def teardown(self):
		self.c = None


	def test_config_file_write(self):
		self.c.write_config("fixtures/config_test_output.config")

	
	def test_broken_config_file(self):
		self.c = Config()
		assert_raises(ValueError, self.c.load_config, "fixtures/gpgpusim_invalid.config")

	
	def test_get_and_set_item(self):
		assert_true(self.c["-gpgpu_dram_buswidth"] == "4")
		self.c["-gpgpu_dram_buswidth"] = 5
		assert_true(self.c["-gpgpu_dram_buswidth"] == "5")

			

	

