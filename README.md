# Learning Dashboard

A beginner portfolio project that combines **SQL**, **Python** and **HTML/CSS/JavaScript** into a working interactive dashboard.

## Why I built this
I’m still new to programming outside of SQL. Right now I’m actively learning **HTML, CSS, JavaScript, and Python** and I wanted to take on a challenge that included all of them together.  

This project took me time and effort to build piece by piece. SQL came more naturally to me but Python and the web parts were a challenge. Even though I understand the code, I am still learning how to assemble the code. I couldn’t have done this from memory or without help but I worked through it step by step, typed everything out myself, debugged along the way and in the process I started to see the **big picture of how these moving pieces fit together**.  

I see this project as a milestone: not because I’m fluent yet, but because I proved to myself that I can connect tools across the stack and actually make something real. I set goals often and this is one of my current goals, to be able to write this with no assistance and from memory.

## Features
- **SQLite database** (`data/dashboard.db`) with:
  - `study_sessions` (date, topic, minutes)
  - `applications` (company, role, stage, date)
- **Python scripts** (`scripts/`):
  - `build_db.py`: builds the database from schema + seed data
  - `export_json.py`: runs SQL queries and writes results to `web/data.json`
- **Dashboard website** (`web/`):
  - Weekly study minutes (bar chart)
  - Study minutes by topic (horizontal bar chart)
  - Application stages (doughnut chart)

## Development process
I built and ran this project entirely from the command line using **PowerShell** on Windows together with **VS Code** and **Git**.  

- Created folders and files with PowerShell (`mkdir`, `ni`)  
- Ran Python scripts with `python scripts/build_db.py` and `python scripts/export_json.py`  
- Served the website locally using `python -m http.server`  
- Used Git in PowerShell to add, commit, and push changes to GitHub  

This was my first time keeping everything inside a terminal workflow and it helped me understand how developers typically work with projects step by step.

## 🚀 How to View the Dashboard


1. Install Python (if not already installed)  
   - Download from https://www.python.org/downloads/  
   - On Windows, check “Add Python to PATH” during install  

2. Download or clone this project  
   - If you’re not using Git, click the green “Code → Download ZIP” button on GitHub, then unzip the folder  
   - Or with Git:  
    ``` git clone https://github.com/ReginaHaley/learning-dashboard.git  ```
    ``` cd learning-dashboard  ```

3. Create the database  
   From the project folder (learning-dashboard), run:  
     ```python scripts/build_db.py  ```
   This will create ```data/dashboard.db  ```

4. Export the data for the website  
   Still in the project folder, run:  
    ``` python scripts/export_json.py  ```
   This will create ``` web/data.json  ```

5. Start the local web server  
   Change into the web folder and start Python’s built-in server:  
   ```cd web  ```
  ``` python -m http.server 8000  ```

6. Open the dashboard in your browser  
   Go to: http://localhost:8000  
   You’ll see an interactive dashboard with three charts:  
   - Weekly study minutes  
   - Minutes by topic  
   - Application stages  

7. Stop the server when finished  
   In the terminal window running the server, press Ctrl + C  

