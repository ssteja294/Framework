#  Framework

import sqlite3
dbConnection = sqlite3.connect("Framework.db")
dbCursor = dbConnection.cursor()

def loadConfig():
        config = {}
        rows = dbCursor.execute("SELECT key, value FROM configuration").fetchall()
        for key, value in rows:
            if value.startswith("[") and value.endswith("]"):
                config[key] = eval(value)
            else:
                config[key] = value
        return config

def displayMenu():
    print(f"--- {title} Management System ---")
    menuIndex = 1 
    for menuItem in menu:
        if menuItem == "Exit":
            print(f"{menuIndex}. {menuItem}")
        else:
            print(f"{menuIndex}. {menuItem} {keyword}")
        menuIndex += 1


def createTable():
     fieldsDefinition = ', '.join([f"{field} TEXT" for field in fieldNames])
     createTableQuery = f"CREATE TABLE IF NOT EXISTS frameworkTable ({fieldsDefinition})"
     dbCursor.execute(createTableQuery)
     dbConnection.commit()


def createRecord():
        values = [input(f"Enter {field}: ") for field in fieldNames]
        dbCursor.execute(f"INSERT INTO frameworkTable VALUES ({', '.join(['?'] * len(values))})", values)
        dbConnection.commit()
        print("Record created successfully.")

def printRecord():
        dbCursor.execute("SELECT * FROM frameworkTable")
        rows = dbCursor.fetchall()
        for row in rows:
            print(row)
 
def updateRecord():
         id = input(f"Enter the {fieldNames[0]} update: ")
         updates = []
         for field in fieldNames[1:]:
            newValue = input(f"Enter new {field}: ")
            updates.append(newValue)
         updateFields = ', '.join([f"{field} = ?" for field in fieldNames[1:]])
         dbCursor.execute(f"UPDATE frameworkTable SET {updateFields} WHERE {fieldNames[0]} = ?", (*updates, id))
         dbConnection.commit()
         print("Record updated successfully.")
    
def deleteRecord():
        id = input(f"Enter the {fieldNames[0]} to delete: ")
        dbCursor.execute(f"DELETE FROM frameworkTable WHERE {fieldNames[0]} = ?", (id,))
        dbConnection.commit()
        print("Record deleted successfully.")
    
def searchRecord():
        id = input(f"Enter the {fieldNames[0]} to search: ")
        dbCursor.execute(f"SELECT * FROM frameworkTable WHERE {fieldNames[0]} = ?", (id,))
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
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

config = loadConfig()
menu = config.get("Menu", [])
title = config.get("Title")
fieldNames = config.get("FieldNames", [])
keyword = config.get("keyword" )
createTable()
main()
