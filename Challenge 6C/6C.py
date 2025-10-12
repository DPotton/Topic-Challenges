"""Dylan Potton
Topic Challenge 6C
October 12th, 2025"""

"""Create and manipulate a SQLite database for weather samples."""

import sqlite3

class DBOperations:
    def __init__(self, db_name='weather.sqlite'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def initialize_db(self):
        """Create the database table if it doesn't exist."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS samples
                                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                date TEXT NOT NULL,
                                location TEXT NOT NULL,
                                min_temp REAL NOT NULL,
                                max_temp REAL NOT NULL,
                                avg_temp REAL NOT NULL);""")
            
            self.conn.commit()
            print("Database initialized and table created successfully.")
            return True
            
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
            return False
    
    def insert_weather_data(self, weather_data, location="Winnipeg, MB"):
        """Insert weather data using parameter substitution to prevent SQL injection."""
        try:
            if not self.conn:
                print("Database not initialized. Call initialize_db() first.")
                return False
            
            sql = """INSERT INTO samples 
                     (date, location, min_temp, max_temp, avg_temp) 
                     VALUES (?, ?, ?, ?, ?)"""
            
            records_added = 0
            for date, temps in weather_data.items():
                data = (
                    date, 
                    location, 
                    temps.get("Min", 0.0), 
                    temps.get("Max", 0.0), 
                    temps.get("Mean", 0.0)
                )
                
                self.cursor.execute(sql, data)
                records_added += 1
            
            self.conn.commit()
            print(f"Successfully added {records_added} weather records.")
            return True
            
        except sqlite3.Error as e:
            print(f"Error inserting weather data: {e}")
            return False
    
    def print_all_data(self):
        """Display all records from the database in a formatted table."""
        try:
            if not self.conn:
                print("Database not initialized. Call initialize_db() first.")
                return False
            
            print("\nWeather Data in Database:")
            print("-" * 80)
            print(f"{'ID':<3} {'Date':<12} {'Location':<15} {'Min Temp':<8} {'Max Temp':<8} {'Avg Temp':<8}")
            print("-" * 80)
            
            self.cursor.execute("SELECT * FROM samples")
            rows = self.cursor.fetchall()
            
            if not rows:
                print("No data found in the database.")
                return True
            
            for row in rows:
                print(f"{row[0]:<3} {row[1]:<12} {row[2]:<15} {row[3]:<8.1f} {row[4]:<8.1f} {row[5]:<8.1f}")
            
            print("-" * 80)
            print(f"Total records: {len(rows)}")
            return True
            
        except sqlite3.Error as e:
            print(f"Error reading data: {e}")
            return False
    
    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")


# Demonstration of the class functionality
if __name__ == "__main__":
    weather = {
        "2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 7.1},
        "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5},
        "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}
    }
    
    db_ops = DBOperations()
    
    if db_ops.initialize_db():
        db_ops.insert_weather_data(weather)
        db_ops.print_all_data()
        db_ops.close_connection()