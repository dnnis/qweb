#!/usr/bin/python

import ez_setup, os, setuptools, sys
ez_setup.use_setuptools()

sys.path[0:0]=['python']
import qweb

setuptools.setup(
	name = 'QWeb',
	version = '0.6',
	url = 'http://antony.lesuisse.org/',
	download_url = 'http://antony.lesuisse.org/',
	license = 'BSD',
	author = 'Antony Lesuisse',
	author_email = 'qweb@udev.org',
	description = 'A high-level Python Web framework, a xml-based templating system, a controler and a request handler.',
	keywords = 'web application server wsgi template xml',
	package_dir = {'': 'python'},
	packages = [i for i in os.listdir('python') if i.startswith("qweb")],
	package_data = {
		'qweb_dbadmin': ['*.xml','*.txt'],
	}
)

if not os.path.isfile("README.txt"):
	s=qweb.qweb_doc()
	pub=s.split('QWeb Components:\n')[0]
	file("README.txt","w").write(s)
	file("dist/QWeb-README-wiki.txt","w").write(pub)
