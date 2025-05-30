🚗 Car Dealership CLI App (Python + SQLAlchemy ORM)
A terminal-based car management system built in Python using SQLAlchemy ORM and SQLite (or PostgreSQL). This app allows users to manage cars via a command-line interface.

🧾 Overview
This is a CLI (Command Line Interface) application that helps manage a simple car dealership database. Users can add , list , search , update , and delete car records from the terminal.

It was developed as part of the Phase 3 Final Project at Moringa School.

🛠 Requirements
To run this project, you'll need:

✅ Python 3.8+
✅ pip or pipenv installed
✅ SQLite (default) or PostgreSQL (optional)

📦 Python Packages Used
click – For building the CLI
sqlalchemy – For ORM and database interaction
rich – For styled terminal output (optional but recommended)
psycopg2-binary – Only if using PostgreSQL

📁 Folder Structure

car_cli_project/
│
├── car_cli/
│   ├── __init__.py
│   ├── cli.py         # Main CLI commands
│   ├── models.py      # SQLAlchemy ORM models
│   └── database.py    # Database setup and connection
│_setup.py    
├── seed.py            # Adds sample data to the DB
├── Pipfile            # Virtual environment config
└── README.md          # You're here!

🧰 Installation

 1. Clone the repo:
bash 
git clone https://github.com/macharia80/car-cli-project.git 
cd car-cli-project

2. Create and activate virtual environment
pip install pipenv
pipenv shell

3. Install dependencies
pipenv install click rich sqlalchemy psycopg2-binary
N/B IF USING POSTGRESQL , MAKE SURE ITS RUNNING AND CONFIGURED PROPERLY
N/B ensure your cd all the work and cd again hence install pip install -e  if u dont it will bring errors
🚀 How to Run
Step 1: Seed the Database
bash
python seed.py OR python3 seed.py
This creates the database file (car.db for SQLite) and adds sample data.

Step 2: Run the CLI App
From the root directory:
python3 -m car_cli.cli list-cars

you should see ouput like this:
Toyota Camry (2022), Color: Blue
Honda Civic (2021), Color: Red
Ford F-150 (2020), Color: Black
Tesla Model S (2023), Color: White
...

🧪 Available Commands

Command,Description
list-cars,Lists all cars in the system
add-car [make] [model] [year] [color],Adds a new car to the system
search-by-make [make],Searches cars by make
update-car [id] [make] [model] [year] [color],Updates an existing car
delete-car [id],Deletes a car by ID

Example Usage:
python3 -m car_cli.cli add-car Tesla ModelX 2024 Silver
python3 -m car_cli.cli search-by-make Toyota
python3 -m car_cli.cli update-car 1 Honda Accord 2023 White
python3 -m car_cli.cli delete-car 1

💡 Tips
Use python3 -m car_cli.cli --help to see full usage instructions.
If using SQLite , the database file will be created automatically as car.db.
If using PostgreSQL , update the engine string in database.py with your credentials.
🔐 Fix PostgreSQL Connection Issues
If you get:
fe_sendauth: no password supplied

Update your engine string in database.py
engine = create_engine("postgresql://username:your_password@localhost/car_db")
N/B ensure you replace username and your_password with your actual PostgreSQL credentials.
    Then set your PostgreSQL password
    bash
    sudo -i -u postgres
psql
ALTER USER macharia WITH PASSWORD 'your_password';
\q
exit

Or switch SQLITE for simplicity 
bash
engine = create_engine("sqlite:///car.db")

Feature,Status
Terminal-based CLI Interface,✅
Display Car Data in Terminal,✅
SQLite / PostgreSQL Integration,✅
ORM Usage (SQLAlchemy),✅
Proper Package Structure,✅
Use of Lists / Tuples / Dictionaries,✅
CRUD Operations,✅

Story,Status
"As a user, I should be able to view a list of all cars stored in the database so that I can see available vehicles.",✅
"As a user, I should be able to add a new car entry through the CLI so that it gets saved permanently in the database.",✅
"As a user, I should be able to search for cars by make or model so that I can find specific entries quickly from the database.",✅
"As a user, I should be able to update a car record.",✅
"As a user, I should be able to delete a car record.",✅

📌 Troubleshooting
🔒 PostgreSQL Authentication Failed?
Update your engine string in database.py:
engine = create_engine("postgresql://USERNAME:your_password@localhost/car_db")

Make sure to set the password in POSTGRESQL
bash
sudo -i -u postgres
psql
ALTER USER username WITH PASSWORD 'your_password';
\q

🐍 ModuleNotFoundError: No module named 'car_cli'
Make sure you’re in the correct directory:

bash
cd ~/moringa-school-work/phase-3-project/car_cli_project

and run:
python3 -m car_cli.cli list-cars

Or directly:
python3 car_cli/cli.py list-cars

📦 Optional: View SQLite File
If using SQLite, inspect the database directly:

bash
sqlite3 car.db
SELECT * FROM cars;

😁😁😁☆*: .｡. o(≧▽≦)o .｡.:*☆
Enjoying using the CLI? Let me know if you have any questions or need further assistance! 😊
 
 my email is mrmachariaorsam@gmail.com

 Happy coding code nerds
