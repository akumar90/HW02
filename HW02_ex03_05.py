#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def print_plus():
	print '+',

def print_ceiling():
	print '- - - -',

def skip_ceiling():
	print "       ",

def print_pipe():
	print "|",

def print_line(noOfColumns):
	print_plus()
	for x in range(0,noOfColumns):
		print_ceiling()
		print_plus()

def print_skipped_line(noOfColumns):
	print_pipe()
	for x in range(0,noOfColumns):
		skip_ceiling()
		print_pipe()

def go_to_new_line():
	print 

def draw_grid(noOfRows, noOfColumns):
	
	for x in range(0,noOfRows):
		print_line(noOfColumns)
		go_to_new_line()
		for i in range(0,4):
			print_skipped_line(noOfColumns)
			go_to_new_line()

	print_line(noOfColumns)

# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    print
    draw_grid(2,2)
    print
    draw_grid(4,4)



if __name__ == "__main__":
    main()