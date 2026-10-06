# Personal Library Management System
A simple command-line Personal Library Management System built with Python.

This version uses temporary in-memory storage. Any books added during a session 
will be lost when the program exits. Future versions will introduce permanent 
data storage.

## About the Project
Version 1 is a console-based application that allows a user to manage a small 
collection of books using Python.

Books are temporarily stored in a list, with each book represented as a dictionary 
containing its ID, title, author, and publication year.

## Features
The current version supports:

- Add a new book
- View all books
- Search for a book by title
- Update book information
- Delete a book
- Prevent duplicate book IDs
- Run through a simple command-line menu

## Technologies / Concepts Used
### Technology
- Python

### Concepts
- Lists
- Dictionaries
- Functions
- Boolean values
- Flag variables
- List methods such as append() and remove()
- Dictionary access and modification

## How to Run
1. Clone or download the repository.
2. Open the project folder in your preferred Python editor.
3. Run the main Python file.
4. Use the numbered menu to interact with the application.

## Current Version
Version 1 → Lists + Dictionaries + Functions

## Future Plans
1. Version 2 → Object-Oriented Programming
2. Version 3 → JSON persistence
3. Version 4 → SQLite
4. Version 5 → Tkinter GUI

## What I Learned in V1
- Using dictionaries to represent real-world objects such as books
- Using lists to store multiple records
- Creating functions to separate different operations
- Searching through a list using loops and conditions
- Using flag variables to track whether a record was found
- Updating dictionary values
- Removing items from a list
- Preventing duplicate IDs
- Using loops and conditional statements to control program flow
