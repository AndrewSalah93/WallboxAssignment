# WallboxAssignment

Description

This project is an answer for wallbox assignment for QA Software Engineer vacancy.

As required in the task, this project was written in Python. It consists of TWO main packages.

1. wallbox: The package that contains the solution to the functions required in Part 1 (Unit Testing)
for each function a .py file is written.
2. tests: The package that contains the tests for validating the functions' solutions in wallbox package 
equivalent to each part using PyTest as a testing framework.
3. resources: This folder contains the resources needed to test 2nd function in Unit Testing Part.

wallbox package:

1. part1.py: A function that given 2 vectors of integers finds the first repeated number.
2. A function that given a path of the file system finds the first file that meets the
following requirements
a. The file owner is admin
b. The file is executable
c. The file has a size lower than 14*2^20
3. A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
minimum quantity of permutations so that the sequence ends interspersed. For
example, given the sequence 0,1,1,0 how many changes are needed so that the
result is 0,1,0,1

tests package:

1. test_part1.py: It contains the tests for part1.py
2. test_part2.py: It contains the tests for part2.py
3. test_part3.py: It contains the tests for part3.py

* Python 3.10 is used along with pytest 7.1.2