from my_functions import WORKING_WITH_FILE
from my_functions import FILE_NAME
from my_functions.files import read_file
from my_functions.files import write_file


def read_data():
    if WORKING_WITH_FILE:
        return read_file(FILE_NAME)


def write_data(my_wardrobe):
    if WORKING_WITH_FILE:
        write_file(FILE_NAME, my_wardrobe)
