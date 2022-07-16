import os
from pathlib import Path
import pytest


def file_req(directory):
    """
    This function searches a specific path to find the first file which meet the following requirements:
    1. The file owner is admin
    2. The file is executable
    3. The file size is lower than 14*2^20 (14MB)

        Parameter(s):
             directory (str): The path to search the required file in it

        Return(s):
              path (str): The file name which meets the requirements
              "File not found with the mentioned requirements": in case the directory does not contain any file
              meeting the requirements
    """
    list_of_files = os.listdir(directory)
    found = False
    for path in list_of_files:
        path_formatted = Path(directory + "\\" + path)
        is_file_executable = os.path.isfile(path_formatted) and path.find(".exe") != -1
        is_file_has_admin = os.access(path_formatted, os.X_OK) and os.access(path_formatted, os.R_OK) and os.access(
            path_formatted, os.W_OK)
        is_file_size_less_than_14MB = path_formatted.stat().st_size < 14680064
        if is_file_executable and is_file_has_admin and is_file_size_less_than_14MB:
            found = True
            break
    if found:
        return path
    else:
        return "File not found with the mentioned requirements"


# The following functions are used to test the implementation of file_req()
def test_fn_when_find_file_meet_req():
    assert file_req(r"E:\Wallbox test") == "Executable 1.exe"


def test_fn_when_find_folders_only():
    assert file_req(r"E:\Wallbox test\Folder 2") == "File not found with the mentioned requirements"


def test_fn_when_find_exe_bigger_than_14MB():
    assert file_req(r"E:\Wallbox test\Folder 1\Subfolder 1") == "File not found with the mentioned requirements"
