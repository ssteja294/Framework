#  Framework

import sqlite3
dbConnection = sqlite3.connect("Framework.db")
dbCursor = dbConnection.cursor()

def loadConfig():
        keys = dbCursor.execute("SELECT key FROM configuration").fetchall()
        values = dbCursor.execute("SELECT value FROM configuration").fetchall()
        config = {key[0]: eval(value[0]) for key, value in zip(keys, values)}
        return config

def displayMenu():
    print(f"--- {title} Management System ---")
    index = 1 
    for item in menu:
        print(f"{index}. {item}")
        index += 1

def createTable():
     fields_definition = ', '.join([f"{field} TEXT" for field in field_names])
     create_table_query = f"CREATE TABLE IF NOT EXISTS frameworkTable ({fields_definition})"
     dbCursor.execute(create_table_query)
     dbConnection.commit()


def createRecord():
        createTable()
        values = [input(f"Enter {field}: ") for field in field_names]
        dbCursor.execute(f"INSERT INTO frameworkTable VALUES ({', '.join(['?'] * len(values))})", values)
        dbConnection.commit()
        print("Record created successfully.")

def printRecord():
        dbCursor.execute("SELECT * FROM frameworkTable")
        rows = dbCursor.fetchall()
        for row in rows:
            print(row)
 
def updateRecord():
         id = input(f"Enter the {field_names[0]} of the record to update: ")
         updates = []
         for field in field_names[1:]:
            new_value = input(f"Enter new {field}: ")
            updates.append(new_value)
         update_fields = ', '.join([f"{field} = ?" for field in field_names[1:]])
         dbCursor.execute(f"UPDATE frameworkTable SET {update_fields} WHERE {field_names[0]} = ?", (*updates, id))
         dbConnection.commit()
         print("Record updated successfully.")
    
def deleteRecord():
        id = input(f"Enter the {field_names[0]} of the record to delete: ")
        dbCursor.execute(f"DELETE FROM frameworkTable WHERE {field_names[0]} = ?", (id,))
        dbConnection.commit()
        print("Record deleted successfully.")
    
def searchRecord():
        id = input(f"Enter the {field_names[0]} of the record to search: ")
        dbCursor.execute(f"SELECT * FROM frameworkTable WHERE {field_names[0]} = ?", (id,))
        result = dbCursor.fetchone()
        if result:
            print("Record found:", result)
        else:
            print("Record not found.")

def main():
    while True:
        displayMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            createRecord()
        elif choice == '2':
            printRecord()
        elif choice == '3':
            updateRecord()
        elif choice == '4':
            deleteRecord()
        elif choice == '5':
            searchRecord()
        elif choice == '6' or choice.lower() == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

config = loadConfig()
menu = config.get("Menu", [])
title = config.get("Title", "Framework")
field_names = config.get("FieldNames", [])
main()
