#MIT License
#
#Copyright (c) 2016 Colin Weinshenker
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import os
from GPGPY.run.benchmark import Benchmark
from nose.tools import assert_true, assert_false, assert_raises
from GPGPY.config.config import Config


config_filename = os.path.dirname(os.path.abspath(__file__)) + "/fixtures/gpgpusim.config"

class TestBenchmark(object):


	def setup(self): 	
		c = Config()
		c.load_config(config_filename)
		self.benchmark = Benchmark(name="bench", executable_path="executable_path", config=c)


	def teardown(self):
		c = None


	def test__str__(self):
		assert_true(str(self.benchmark) == "bench")		


	def test__iter__(self):
		config_1 = ["1 2 3 4 5"]
		config_2 = ["0 1", "34"]
		self.benchmark.add_configs(config_1)
		self.benchmark.add_configs(config_2)
		run_configs = [config for config in self.benchmark]
		assert_true(len(run_configs) == 3)	

	
	def test_add_configs(self):
		config_1 = ["1 2 3 4 5"]
		config_2 = ["0 1", "34"]
		self.benchmark.add_configs(config_1)
		self.benchmark.add_configs(config_2)
		config_1.extend(config_2)
		assert_true(set(self.benchmark._run_configs.values()) == set(config_1))


	def test_del_configs(self):
		config_1 = ["1 2 3 4 5"]
		self.benchmark.add_configs(config_1)
		self.benchmark.del_configs(config_1)
		print(self.benchmark._run_configs)
		assert_true(self.benchmark._run_configs == {})						 
