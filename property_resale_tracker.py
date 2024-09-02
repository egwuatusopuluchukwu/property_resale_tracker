import csv
from datetime import datetime

# File to store property data
FILE_NAME = 'property_resale_tracker.csv'

# Define the columns
COLUMNS = [
    "Property ID", "Property Type", "Location", "Client Name", "Contact Info", 
    "Date Listed", "Asking Price", "Status", "Date Sold", "Buyer Name", 
    "Buyer Contact Info", "Comments"
]

def initialize_csv(file_name):
    try:
        with open(file_name, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)
    except FileExistsError:
        pass

def add_property():
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        property_id = input("Enter Property ID: ")
        property_type = input("Enter Property Type: ")
        location = input("Enter Location: ")
        client_name = input("Enter Client Name: ")
        contact_info = input("Enter Client Contact Info: ")
        date_listed = input("Enter Date Listed (YYYY-MM-DD): ")
        asking_price = input("Enter Asking Price: ")
        status = "Listed"
        date_sold = ""
        buyer_name = ""
        buyer_contact_info = ""
        comments = input("Enter Comments: ")
        
        writer.writerow([
            property_id, property_type, location, client_name, contact_info,
            date_listed, asking_price, status, date_sold, buyer_name,
            buyer_contact_info, comments
        ])
        print("Property added successfully.\n")

def update_property():
    properties = []
    property_id = input("Enter the Property ID to update: ")
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        properties = list(reader)
    
    for i, row in enumerate(properties):
        if row[0] == property_id:
            properties[i][7] = "Sold"
            properties[i][8] = input("Enter Date Sold (YYYY-MM-DD): ")
            properties[i][9] = input("Enter Buyer Name: ")
            properties[i][10] = input("Enter Buyer Contact Info: ")
            print("Property updated successfully.\n")
            break
    else:
        print("Property ID not found.\n")
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(properties)

def view_properties():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
        print()

def main():
    initialize_csv(FILE_NAME)
    
    while True:
        print("Property Resale Tracker")
        print("1. Add Property")
        print("2. Update Property")
        print("3. View Properties")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_property()
        elif choice == '2':
            update_property()
        elif choice == '3':
            view_properties()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
