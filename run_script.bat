@echo off
REM Navigate to the directory where your project is located
cd E:\Projects\open_cart_project

REM Activate the virtual environment
call .venv\Scripts\activate

REM Run pytest with your marker
pytest -m flow

REM Pause the script so you can see any errors
pause