import pathlib
import os

string_split = input("Input string to split: ").lower().strip()  # Takes given hex delimiter, converts to lowercase and strips all whitespace
file_type = input("Please enter the file type to modify: ").strip()  # Takes a filetype to modify
# Adds a period to the beginning of the provided filetype if one is not already present
if not file_type.startswith("."):
  file_type = "." + filetype
target_dir = os.getcwd()  # Gets the directory the script lives in
target_req = input("Please enter the target directory, leave blank to use the script's current location: ")  # Takes input from user regarding where to look for files in
# If user provided a target directory switch from current directory to given directory
if len(target_req) > 1:
	target_dir = target_req

for active_file in pathlib.Path(target_dir).glob('*' + file_type.strip()):  # Looks at every file in given folder ending with the given file type
	try:
		with open(active_file, "rb") as from_file, open(str(active_file).rsplit(".",1)[0] + "_audited." + str(active_file).rsplit(".",1)[1], "wb") as to_file:  # Opens up current file as a binary file, along with a new file that takes the original file and modifys it
			bytes_to_audit = from_file.read().hex()  # Reads the file as a hex object
			bytes_to_audit = bytes_to_audit.split(string_split)  # Splits hex object based on delimited
			bytes_to_audit = string_split + "".join(bytes_to_audit[1:])  # Readds everything after hex delimiter to the delimiter itself
			to_file.write(bytes.fromhex(bytes_to_audit))  # Writes new hex object as a bytes object to file
	except Exception as e:
		print("Unable to break {0} from file: {1} due to error: {2}".format(string_split, active_file, e))  # Error message in case something goes awry