import os
try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages
	
setup(
	name='scrapex', 
	version='0.1.1',
	packages=find_packages(),
	author='valen0214',
	author_email='jiajia0214@mail.ru',
	description='A simple web scraping lib for Python',    
	long_description= 'You can also install by download the package here:\n https://github.com/valen0214/scrapex/archive/master.zip',
	url='https://github.com/valen0214/scrapex',   
	download_url = 'https://github.com/valen0214/scrapex/archive/master.zip', 
	install_requires = [
		'lxml',
		'xlwt',
		'xlrd',
		'openpyxl',
		'twisted',
		'pyOpenSSL',
		'service_identity'
	],
	
	license='LGPL',

)
