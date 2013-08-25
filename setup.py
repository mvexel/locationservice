from setuptools import setup

setup(
  name="LocationService",
  version="1.0",
  packages=["locationservice"],
  include_package_data=True,
  install_requires=[
	'Flask==0.10.1',
	'pysqlite==2.6.3',
	'wsgiref==0.1.2'
]
)
