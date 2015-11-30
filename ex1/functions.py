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
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.
def add(x,y):
    return x + y
# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.
def to_tuple(x, y, z):
    mytup = x, y, z
    return mytup
# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.
def check5(x):
    if x > 5:
        return True
    else:
        return False

# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second
def check_n(x, n):
    if x > n:
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
def check_list(numlist, num):
    for i in range (len(numlist)):
        if numlist[i] >= num:
            numlist[i] = True
        else:
            numlist[i] = False
    return numlist
# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.
def check_list_nth(numlist, num, nth):
    newlist = []
    for i in range (0, len(numlist), nth):
        if numlist[i] >= num:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.
def add_new_list(l, x):
    newlist = l.copy()
    newlist.append(x)
    return newlist
# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(l, nth=2):
    newlist = l.copy()
    del newlist[0::nth]
    return newlist
# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values
def search_n(l, x):
        if x in l:
            i = l.index(x)
            return i, l[i]
        else:
            return None, None
################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.
def args_to_dict(x,y,z):
    mydict = {0 : x, 1 : y, 2 : z}
    return mydict
# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*x):
    mydict = {}
    i = 0
    for y in x:
        mydict[i] = y
        i = i + 1
    return mydict
# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.
def lists_to_dict(keys,values):
    mydict = dict(zip(keys,values))
    return mydict
# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.
def search_list(x,y):
    mydict = {}
    for i in range (len(y)):
        j = search_n(x, y[i])
        if j[0] != None:
            temp = {j[0]:j[1]}
            mydict.update(temp)
    return mydict

# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(dic,sep):
    mystr = ''
    for value in dic.values():
        if isinstance(value, str):
            mystr = mystr + value + sep
    return mystr[:-1]
# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(l):
    x = []
    y = []
    z = []
    for value in l:
        if isinstance(value, int):
            x.append(value)
        elif isinstance(value, str):
            y.append(value)
        else:
            z.append(value)
    mydict = {'int' : x, 'str' : y, 'others' : z}
    return mydict
