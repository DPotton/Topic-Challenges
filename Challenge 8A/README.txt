IP Checker
==========

A simple Python module that retrieves and displays your current public IP address.

Description
-----------
This module uses the service at checkip.dyndns.org to fetch your public IP address.
It parses the HTML response to extract and display the IP address.

Installation
------------
pip install ip_checker-1.0.0.tar.gz

Usage
-----
After installation, you can run the module from the command line:

    ip-checker

Or import it in your Python code:

    from ip_checker.ip_checker import get_ip_address
    get_ip_address()

Requirements
------------
- Python 3.6 or higher
- Standard library modules only (html.parser, urllib.request)

Author
------
Dylan Potton