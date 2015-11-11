# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''

# Example so that you can see a passing test
def f():
    """
	Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.
def add(a,b):
	"""
    Adds two parameters and returns its sum

    Parameters
    ----------
    a: int or float
        First summand
    b: int or float
        Second summand

    Returns
    -------
    a+b: int or float
        Sum of a and b
    """
	return a+b
	
# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.

def to_tuple(a,b,c):
	"""
    Adds there parameters to a tuple

    Parameters
    ----------
    a: object
        First object to add to tuple
    b: object
        Second object to add to tuple
	c: object
		Third object to add to tuple

    Returns
    -------
	(a,b,c)
        Tuple of a and b and c
    """
	return (a,b,c)

# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.
def check5(n):
	"""
    Checks if given parameter is greater than 5

    Parameters
    ----------
    n: int or float
        Number to check

    Returns
    -------
    True or False
        Returns True if parameter is greater than 5, False if not
    """
	if n > 5:
		return True
	else:
		return False

# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second
def check_n(i,n):
	"""
    Checks if given parameter i is greater than parameter n

    Parameters
    ----------
    i: int or float
        First number to check
	n: int or float
		Second number to check

    Returns
    -------
    True or False
        Returns True if parameter i is greater than n, False if not
    """
	if i > n:
		return True
	else:
		return False


#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.
def check_list(list,n):
	"""
    Checks if elements in a list is greater than parameter n

    Parameters
    ----------
    list: list
        List of numbers
	n: int or float
		Number to compare

    Returns
    -------
	result: list of int or float
        Returns a list of elements that are greater than n
    """
	result = [x >= n for x in list]
	return result

# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.
def check_list_nth(list,n,step):
	"""
    Checks if elements in a list is greater than parameter n, but uses a step width

    Parameters
    ----------
    list: list
        List of numbers
	n: int or float
		Number to compare
	step: int
		Step width between elements to check

    Returns
    -------
	result: list of int or float
        Returns a list of elements that are greater than n, with given step width
    """
	result = [x >= n for x in list[0::step]]
	return result

# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.
def add_new_list(l,x):
	"""
    Adds parameter x to list, without changing the original given list

    Parameters
    ----------
    l: list
        List to which object is added
	x: object
		Object to add to the given list
	
    Returns
    -------
	newl: list
        Returns the list with added object x
    """
	newl = l.copy()
	newl.append(x)
	return newl

# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(list,nth=2):
	"""
    Removes every nth element of a list

    Parameters
    ----------
    l: list
        List from which a object is deleted
	nth: int
		Every nth element which is deleted
	
    Returns
    -------
	newl: list
        Returns the list with deleted object/s
    """
	newl = list.copy()
	del newl[0::nth]
	return newl

# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values
def search_n(list,x):
	"""
    Searches a list for element x

    Parameters
    ----------
    list: list
        List in which is searched for element x
	x: object
		Object which is searched for in list
	
    Returns
    -------
	tuple
        Returns a tuple with found variable and its index or None,None if nothing is found
    """
	if x in list:
		return(list.index(x), x)
	else:
		return(None,None)

################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.
def args_to_dict(a,b,c):
	"""
    Writes three arguments to dictionary

    Parameters
    ----------
    a: object
        First object to add to dictionary
    b: object
        Second object to add to dictionary
	c: object
		Third object to add to dictionary
	
    Returns
    -------
	dictionary
        Returns a dictionary with keys 0 to 2 and given values a,b,c
    """
	return {0:a,1:b,2:c}

# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*args):
	"""
    Writes three arguments to dictionary

    Parameters
    ----------
    *args: objects
		Given objects to add to dictionary
	
    Returns
    -------
	d: dictionary
        Returns a dictionary with keys 0 to n and given values n
    """
	d = {}
	i = 0
	for arg in args:
		d[i] = arg
		i+=1
	return d
	
# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.
def lists_to_dict(keys,values):
	"""
    Creates a dictionary out of two list

    Parameters
    ----------
    keys: list
		List with keys for the dictionary
	values: list
		List with values for the dictionary
	
    Returns
    -------
	dictionary
        Returns a dictionary with keys and values from their respective lists
    """
	return dict(zip(keys,values))
	
# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.
def search_list(a,b):
	"""
    Searches list a for all elements of b

    Parameters
    ----------
    a: list
		List in which is searched
	b: list
		List of values which are searched for
	
    Returns
    -------
	dictionary
        Returns a dictionary with found elements, empty dictionary if nothing is found
    """
	d = {}
	for x in a:
		if x in b:
			d[a.index(x)] = x
	return d
			
# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(d,string):
	"""
    Searches list a for all elements of b

    Parameters
    ----------
    d: dict
		Dictionary of which string elements are taken out
	string: str
		Separator string which is used
	
    Returns
    -------
	str
        Returns string of found strings, empty string if no string is found
    """
	output = ' '
	for x in d.values():
		if type(x) == str:
			output += x + string
	return output[1:len(output)-1]
	
# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(l):
	"""
    Classifies types of variables out of a list

    Parameters
    ----------
    l: list
		List of which variables are taken out
		
    Returns
    -------
	d: dict
        Returns dictionary with respective types of variables found, empty dict if empty list was given
    """
	list_i = []
	list_s = []
	list_o = []
	for x in l:
		if type(x) == int:
			list_i.append(x)
		elif type(x) == str:
			list_s.append(x)
		else:
			list_o.append(x)		
	return {'int': list_i,'str': list_s,'others': list_o}