"""
This is the main program that when you run it, it loads the application main menu
"""

# Import external modules
import config
from FormBuilder import FormBuilder
from MainMenu import MainMenu

# Import libraries
import sqlite3

main_menu = MainMenu()
main_menu.form_display()


# Fetch one record
# fetchone()

# If we ever commit something
# conn.commit()

