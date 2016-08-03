from collections import OrderedDict
from applicant_model import Applicant
from interviewslot_model import InterviewSlot
import os


# Clears the terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# This is the main loop, which handles the sub menu choices.
def applicant_menu_loop():
    """Applicant"""
    choice = None

    while choice != '0':
        print("Enter '0' to exit to main menu.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Menu number: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

"""
This section defines the sub menu choices.
"""


def get_applicant_data():
    """My application data """
    app_code = input("Enter your application code: ")
    for applicant in Applicant.select().where(Applicant.application_code == app_code):
        print(applicant)


def get_interview_details():
    """My personal interview data"""
    app_code = input("Enter your application code: IT ISN'T WORKING!")
    for interview in InterviewSlot.select().where(InterviewSlot.applicant == app_code):
        print("\nSchool: {}\nDate and time of the interview: {}\nMentor: {}\n".format(
              interview.school_name, interview.date_time, interview.mentor))


# This library allows you to choose an operation.
menu = OrderedDict([
    ('1', get_applicant_data),
    ('2', get_interview_details)
])
