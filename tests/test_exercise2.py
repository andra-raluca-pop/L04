import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_at_5():
    assert is_passing(5) == True


# bug report 2
def test_r2_is_valid_password_at_8_characters(): 
    assert is_valid_password("12345678") == True


# bug report 3
def test_r3_clamp_at_high():
    assert clamp(10, 1, 5) == 5
