"""Dylan Potton
Topic Challenge 8A
October 25th, 2025"""

from setuptools import setup, find_packages
"""Setup script for the ip_checker package."""

with open('README.txt', 'r') as f:
    long_description = f.read()

setup(
    name='ip_checker',
    version='1.0.0',
    author='Dylan Potton',
    author_email='your-email@example.com',
    description='A simple tool to retrieve the current public IP address',
    long_description=long_description,
    long_description_content_type='text/plain',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'ip-checker=ip_checker.ip_checker:get_ip_address',
        ],
    },
)