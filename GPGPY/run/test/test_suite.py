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


from nose.tools import assert_true, assert_false, assert_raises
from ....config.config import Config




config_filename = os.path.dirname(os.path.abspath(__file__)) + "/fixtures/gpgpusim.config"

class TestSuite(self):

	def setup(self): 
		config = Config()
		config.load(config_filename)
		self.suite = Suite("Demo", config)	
		self.bench1 = Benchmark(name="bench", executable_path="executable_path", config=c)
		self.bench2 = Benchmark(name="bench2", executable_path="executable_path2", config=c)



	def teardown(self):
		pass	



	def test__init__(self):
		assert_true(self.suite._benchmarks == [])
	

	def test__str__(self):
		assert_true(str(self.suite) == "Demo")


	def test_add_benchmark(self):
		self.suite.add_benchmarks(bench1, bench2)
					


			
