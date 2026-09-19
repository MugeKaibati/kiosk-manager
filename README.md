# THE KIOSK MANAGER

## 1. ABOUT THE PROJECT

The Kiosk Manager is a simple Python program designed to help a small kiosk manage its daily operations. It allows the user to manage stock, sell products, view sales, search for products, and save information so that it is not lost when the program is closed.

## 2. FEATURES

* View available stock
* Add new products
* Restock existing products
* Sell products
* Check available stock before selling
* Calculate the total cost of a sale
* Record sales
* View a sales report
* Search for products
* Save inventory information
* Save sales information
* Load saved information when the program starts
* Validate user input to reduce errors

## 3. REQUIREMENTS

The program requires:

* Python 3
* A computer with a terminal or code editor such as VS Code

No external Python libraries are required.

## 4. HOW TO RUN THE PROGRAM

1. Make sure Python 3 is installed.

2. Open the project folder in VS Code or a terminal.

3. Run the program using:

```bash
python kiosk_manager.py
```

4. Enter the kiosk name and owner's name when requested.

5. Use the menu to select the required operation.

## 5. MAIN MENU

The program provides six options:

1. **View Stock**
   Displays all products, their prices, and available quantities.

2. **Add/Restock a Product**
   Allows the user to add a new product or increase the quantity of an existing product.

3. **Sell a Product**
   Allows the user to sell a product if enough stock is available. The program calculates the total cost and updates the stock.

4. **View Sales Report**
   Displays recorded sales, total revenue, the number of unique products sold, and the best-selling product.

5. **Search Products**
   Allows the user to search for products using part or all of the product name.

6. **Exit**
   Saves the current inventory before closing the program.

## 6. DATA FILES

The program uses two text files to store information.

### inventory.txt

Stores the product name, price, and quantity.

Example:

```text
Bread, 65, 17
Milk, 55, 13
Sugar, 150, 10
```

### sales.txt

Stores each completed sale.

Example:

```text
Milk, 2, 110
Bread, 1, 65
```

## 7. INPUT VALIDATION

The program checks user input before processing it.

For example:

* Menu choices must be numbers from 1 to 6.
* Product names cannot be empty.
* Prices must be valid positive numbers.
* Quantities must be valid positive numbers.
* A product cannot be sold if it does not exist.
* A product cannot be sold when there is not enough stock.
* Empty searches are rejected.

## 8. EXAMPLE

A user can:

* Add 100 bottles of Soda at Ksh 60 each.
* Sell 5 bottles of Soda.
* The program calculates the sale as Ksh 300.
* The Soda stock is reduced by 5.
* The sale is recorded in `sales.txt`.
* The updated inventory is saved when the program exits.

## 9. PROJECT STRUCTURE

The project contains the following files:

```text
kiosk_manager.py
inventory.txt
sales.txt
README.md
```

**kiosk_manager.py**
Main Python program.

**inventory.txt**
Stores inventory data.

**sales.txt**
Stores sales records.

**README.md**
Contains information about the project and how to use it.

## 10. PURPOSE OF THE PROJECT

This project was created to practice Python programming concepts including variables, dictionaries, lists, tuples, sets, loops, conditional statements, file handling, user input validation, and basic data management.
