import pathlib
import os
import time
import sys


def picker():
    option = 0
    while True:
        try:
            option = int(input(
                "Please select an operation...\n[1] Remove headers from all files of a type within a directory.\n[2] "
                "Merge header files with data files.\n[3] Exit\n\n\n"))
            if not 0 < int(option) < 4:
                print("Choose one of the provided options.")
            else:
                break
        except ValueError as e:
            print("Please only use one of the provided numbers.")
    return option


def breaker():
    string_split = input("Input string to split: ").lower().replace(" ",
                                                                    "")  # Takes given hex delimiter, converts to lowercase and strips all whitespace
    file_type = input("Please enter the file type to modify: ").strip()  # Takes a filetype to modify
    # Adds a period to the beginning of the provided filetype if one is not already present
    if not file_type.startswith("."):
        file_type = "." + file_type
    target_dir = os.getcwd()  # Gets the directory the script lives in
    target_req = input(
        "Please enter the target directory, leave blank to use the script's current location: ")  # Takes input from user regarding where to look for files in
    # If user provided a target directory switch from current directory to given directory
    if len(target_req) > 1:
        target_dir = target_req

    for active_file in pathlib.Path(target_dir).glob(
            '*' + file_type):  # Looks at every file in given folder ending with the given file type
        try:
            with open(active_file, "rb") as from_file, open(
                    str(active_file).rsplit(".", 1)[0] + "_audited." + str(active_file).rsplit(".", 1)[1],
                    "wb") as to_file:  # Opens up current file as a binary file, along with a new file that takes the original file and modifys it
                bytes_to_audit = from_file.read().hex()  # Reads the file as a hex object
                bytes_to_audit = bytes_to_audit.split(string_split)  # Splits hex object based on delimited
                bytes_to_audit = "".join(
                    bytes_to_audit[1:])  # Readds everything after hex delimiter to the delimiter itself
                bytes_to_audit = string_split + bytes_to_audit
                to_file.write(bytes.fromhex(bytes_to_audit))  # Writes new hex object as a bytes object to file
                print(str(active_file).rsplit(os.path.sep)[
                          -1] + " was successfully pruned.")  # Prints out the name of the file pruned
        except Exception as e:
            print("Unable to break {0} from file: {1} due to error: {2}".format(string_split, active_file,
                                                                                e))  # Error message in case something goes awry


while True:
    option = picker()
    if option == 1:
        breaker()

# print("Audit process complete. Exiting in 10 seconds...")
# time.sleep(10)
# sys.exit()
