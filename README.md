# PROJECT_4__Chess_Tournament

## Project Description

This project is the fourth in the OpenClassrooms - Python Application Developer training program. The objective is to manage chess tournament competitions. The application allows for the creation and management of chess tournaments, including player registration, tournament creation, match management, and result tracking.

## Installation

1. Clone this repository using the command:
   ```bash
   git clone https://github.com/samichelly/PROJECT_4__Chess-Tournament.git

2. Set up a virtual environment and activate it:
   - On macOS/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
3. Install the necessary packages for the application to function properly using the command:
   ```bash
   pip install -r requirements.txt
   ```
4. Navigate to the MVC folder and run the program using the command:
   ```bash
   python main.py
   ```

## Functionality

Upon startup, the menu offers 4 actions:

### 1. View Reports

This option allows you to display a report. There are two main types of reports:
1. View all players registered in the national player database.
2. View previously created tournaments and obtain the following details:
   - View the list of players participating in the tournament.
   - View the details of the rounds and matches of a tournament.

### 2. Add a New Player

This option allows you to create a new player who will be registered in the national database without assigning them to a tournament. A uniqueness check is performed to avoid creating duplicate players.

### 3. Create a Tournament

This option allows you to create a new tournament. You can add players from the national database or add a non-existent player directly to the tournament. This player will also be registered in the national database without any user action.

### 4. Load a Tournament

This option allows you to reload an unfinished tournament in order to continue it. Simply indicate the index of the desired tournament to load.

Sections `3. Create a Tournament` and `4. Load a Tournament` allow you to start the tournament once all players are registered. Once the tournament starts, the user will be asked if they wish to start a new round and enter the match results. At the end of the round, an updated ranking sorted in descending order by score is displayed.

## Generate a flake8-html Report

1. Install flake8 using the following command:
   ```bash
   pip install flake8
   ```
2. Execute the following command:
   ```bash
   flake8 --format=html --htmldir=flake8_report --max-line-length=119
   ```
3. View the report in the `flake8_report` folder.
```
