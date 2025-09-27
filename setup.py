from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lorep_agui_app/__init__.py
from lorep_agui_app import __version__ as version

setup(
	name="lorep_agui_app",
	version=version,
	description="Custom Frappe v15 app with AgUI integration",
	author="Your Company",
	author_email="developer@company.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
	# Frappe is already installed in the environment, don't include it as dependency
)