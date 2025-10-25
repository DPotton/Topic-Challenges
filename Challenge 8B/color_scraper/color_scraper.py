"""Dylan Potton
Topic Challenge 7A
October 19th, 2025"""

import urllib.request
from html.parser import HTMLParser

class ColorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.colours = {}
        self.in_table_row = False
        self.in_table_data = False
        self.current_data = []
        self.current_row = []
    
    def handle_starttag(self, tag, attrs):
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
        if tag == "td" and self.in_table_data:
            self.in_table_data = False
            if self.current_data:
                self.current_row.extend(self.current_data)
        elif tag == "tr" and self.in_table_row:
            self.in_table_row = False
            if len(self.current_row) >= 2:
                color_name = self.current_row[0]
                hex_value = self.current_row[1]
                if color_name and hex_value.startswith("#"):
                    self.colours[color_name] = hex_value.lower()

def extract_colors():
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

def main():
    print("Color Scraper - Extracting color names and hex values...")
    print("=" * 50)
    
    try:
        colours = extract_colors()

        for color_name, hex_value in sorted(colours.items()):
            print(f"{color_name}: {hex_value}")

        print(f"\nTotal colors found: {len(colours)}")
        input("\nPress Enter to exit...")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()