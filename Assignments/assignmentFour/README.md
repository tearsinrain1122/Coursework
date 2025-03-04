## Assignment Four
### Introduction
This is the directory for my fourth assignment.  

### My Chosen API/Database scenario :shirt:

I chose to make a simple database consisting of one table that represents the stock information for a small `clothes_shop`
(this could later be scaled up to include other tables using the `item_id` as a foreign key, such as 
an item description table). I then built a console app that enables the user to:
- View the full `stock_list` table (i.e., view all items and their stock level)
- Delete an item 
- Update an item's stock level
- Add a new item  

### Requirements :computer:
#### Downloads 

The following modules will need to be installed before running any files:
- `flask`
- `mysql-connector-python`
- `tabulate`
- `requests`
- `json`

> [!NOTE]
> These packages are also listed in the [requirements.txt](requirements.txt) file in this directory.  

#### Input requirements

A [config.py](config.py) file has been included to input your MySQL credentials, including declared variables for
`HOST` (generally `localhost`), `USER` (generally `root`) and `PASSWORD`. Please fill in these details before 
using the app, otherwise the database connection will not be successful.

>[!CAUTION]
> Ensure your password and other sensitive credentials have been deleted if sharing the code 
> publicly.

### Using the app :computer_mouse:
#### Order to run files
1. Run the MySQL code in the file [clothes_shop.sql](clothes_shop.sql) in MySQL Workbench to create the database `clothes_shop`,
and input sample data values into the `stock_room` table.
3. Run the [app.py](app.py) file to connect to `Flask`.
4. While the [app.py](app.py) file is still running, run the [main.py](main.py) file - this will
then run the front-end of the app in the console.

#### Inputting data into the app
1. You will first be greeted by a Welcome screen, then prompted to select an option A-D, each of which
links to one of the four actions listed in section [My Chosen API/Database scenario](https://github.com/tearsinrain1122/CFG-Assignments/blob/assignment-4-APIs/assignmentFour/README.md#my-chosen-apidatabase-scenario-shirt) above.
2. If you do not select a valid option (single letter A-D), the program will automatically end and you will be required
to re-run the file and try again.
3. Any item IDs and stock numbers that you are asked to input should be typed as integers. If an item ID that is input
does not correspond to any item in stock, you will continue to be prompted for a different ID. 
4. If an integer is not input for the stock number, the program will stop running and an error message will be displayed. 
In this scenario, again, re-run the file and ensure you input the correct data type when prompted.
