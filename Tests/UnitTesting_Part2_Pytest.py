from Scripts.UnitTesting_Part2 import file_req
import pytest


def test_fn_when_find_file_meet_req():
    assert file_req(r"E:\Wallbox test") == "Executable 1.exe"


def test_fn_when_find_folders_only():
    assert file_req(r"E:\Wallbox test\Folder 2") == "File not found with the mentioned requirements"


def test_fn_when_find_exe_bigger_than_14MB():
    assert file_req(r"E:\Wallbox test\Folder 1\Subfolder 1") == "File not found with the mentioned requirements"
