# napredni-algoritmi-i-strukture-podataka
Repozitorij za predmet Napredni Algoritmi i Strukture Podataka. Repo for laboratory exercises. 

Za setupiranje VSC-a koristio sam:
    https://code.visualstudio.com/docs/python/python-tutorial

Kreiranje virtual environmenta:
    1) Create and activate the virtual environment
    Virtual environment creation for Windows
        py -3 -m venv .venv
        .venv\scripts\activate

    2) Select your new environment by using the Python: Select Interpreter command from the Command Palette.

    3) Install the packages
        python -m pip install matplotlib

    4) Deactivate venv
        just type in terminal: deactivate

For git users
    https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde
    Run pip freeze > requirements.txt to place the dependencies in a text file to be committed.
    Freezing reads all the installed dependencies and then produces a text file with the name of
    the dependency and the installed version number.