#!/usr/bin/python3

import re
import pytest
from six import PY2

##################################################################################################
# See readme.txt for how to prepare and run
##################################################################################################

##################################################################################################
#   Following test codes are based on
#       https://medium.com/@AbhijeetKasurde/pytest-how-to-mock-the-built-in-open-d7c6e50e9984
##################################################################################################

@pytest.fixture
def mocker_solaris(mocker):
    # Read a mocked /etc/release file
    mocked_etc_release_data = mocker.mock_open(read_data=" Oracle Solaris 12.0")
    builtin_open = "__builtin__.open" if PY2 else "builtins.open"
    mocker.patch(builtin_open, mocked_etc_release_data)

def check_solaris_version(filename='/etc/release'):
    with open(filename) as f:
        content = f.readlines()
    for line in content:
        m = re.match(r'\s+Oracle Solaris (\d+\.\d+).*', line.rstrip())
        if m:
            return True
    return False

def test_check_solaris_version(mocker_solaris):
    assert check_solaris_version(filename='fakefile')

##################################################################################################
