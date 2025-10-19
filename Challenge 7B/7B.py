"""Dylan Potton
Topic Challenge 7A
October 19th, 2025"""

import urllib.request
from html.parser import HTMLParser

"""This program retrieves a list of color names and their hex values from colorhexa.com"""
class ColorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.colours = {}
        self.in_table_row = False
        self.in_table_data = False
        self.current_data = []
        self.current_row = []
    
    def handle_starttag(self, tag, attrs):
        """Handles the start of HTML tags to identify table rows and data."""
        if tag == "tr":
            self.in_table_row = True
            self.current_row = []
        elif tag == "td" and self.in_table_row:
            self.in_table_data = True
            self.current_data = []
    
    def handle_data(self, data):
        if self.in_table_data:
            stripped_data = data.strip()
            if stripped_data:
                self.current_data.append(stripped_data)
    
    def handle_endtag(self, tag):
        """Handles the end of HTML tags to process collected data."""
        if tag == "td" and self.in_table_data:
            self.in_table_data = False
            if self.current_data:
                self.current_row.extend(self.current_data)
        elif tag == "tr" and self.in_table_row:
            self.in_table_row = False
            # Each row should have: [color_name, hex, red, green, blue, hue, saturation, lightness]
            if len(self.current_row) >= 2:
                color_name = self.current_row[0]
                hex_value = self.current_row[1]
                if color_name and hex_value.startswith("#"):
                    self.colours[color_name] = hex_value.lower()

def extract_colors():
    """Fetches the color names and their hex values from colorhexa.com"""
    url = "https://www.colorhexa.com/color-names"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        html_content = response.read().decode('utf-8')
    
    parser = ColorParser()
    parser.feed(html_content)
    
    return parser.colours

# Extract and display colors
colours = extract_colors()

# Print all colors
for color_name, hex_value in sorted(colours.items()):
    print(f"{color_name} {hex_value}")

print(f"\nTotal colors: {len(colours)}")