"""Dylan Potton
Topic Challenge 7A
October 19th, 2025"""

from html.parser import HTMLParser
import urllib.request

"""This program retrieves the current public IP address of the machine"""
class IPParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_body = False
        self.ip_address = None
    
    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            self.in_body = True
    
    def handle_data(self, data):
        if self.in_body and 'Current IP Address:' in data:
            # The unique piece that precedes our data is "Current IP Address:"
            # Split the string to extract just the IP portion
            ip_part = data.split('Current IP Address: ')[1]
            self.ip_address = ip_part.strip()

def get_ip_address():
    """Fetches and prints the current public IP address."""
    try:
        with urllib.request.urlopen('http://checkip.dyndns.org') as response:
            html = response.read().decode('utf-8')
        
        parser = IPParser()
        parser.feed(html)
        
        if parser.ip_address:
            print(parser.ip_address)
        else:
            print("IP address not found")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ip_address()