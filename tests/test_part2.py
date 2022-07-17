from .context import wallbox
from wallbox.part2 import file_req
import pytest

# The following functions are used to test the implementation of file_req()


def test_fn_when_find_file_meet_req():
    assert file_req(r".\references") == "Executable 2.exe"


def test_fn_when_find_folders_only():
    assert file_req(r".\references\Folder 2") == "File not found with the mentioned requirements"


def test_fn_when_find_exe_bigger_than_14MB():
    assert file_req(r".\references\Folder 1\Subfolder 1") == "File not found with the mentioned requirements"
