from setuptools import setup

setup(name="GPGPY",
      version = '0.1',
      description = 'Package for managing GPGPU-sim output using SQLite3',
     url='',
     author='Colin Weinshenker',
     author_email='caweinshenker@email.wm.edu',
     license='',
     test_suite='nose.collector',
     tests_require=['nose', 'nose-cover3'],
     packages=['GPGPY'],
     include_package_data=True,
     zip_safe=False)
