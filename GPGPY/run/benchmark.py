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
from GPGPY.utils.contextmanager import cd

class Benchmark(object):

        def __init__(self, name=None, executable_path=None, suite=None, config=None):
                self._name = str(name)
                self._executable = str(executable_path)
                self.config = config if config is not None else suite.config
                self._run_configs = {}



        def __str__(self):
                return self._name

	
	def __iter__(self):
		return self._run_configs.values().__iter__()

        def add_configs(self, run_configs=[]):
                self._run_configs.update({i + len(self._run_configs):str(run_config) for i, run_config in enumerate(run_configs)})


        def del_configs(self, run_configs=[]):
		reverse_lookup = {value:key for key, value in self._run_configs.items()}
                for run_config in run_configs:
			if run_config in reverse_lookup:
				del self._run_configs[reverse_lookup[run_config]]
				

        def launch(self):
                for i, run_config in enumerate(run_configs):
                        output_dir = self._name + "_output_" + i
                        try:
                                os.mkdir(output_dir)
                        except OSError as e:
                                print("Directory {} exists. Continuing...".format(os.path.abspath(output_dir)))
                        with cd(output_dir):
                                config.write()
