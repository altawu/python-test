try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Alta',
	'url': '',
	'download_url': '',
	'author_email': 'wuchenxv@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['myprj'],
	'scripts': [],
	'name': 'mypj'
	}

setup(**config)
