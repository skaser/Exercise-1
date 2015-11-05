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
Module for testing the student created functions
'''

import ex1.functions as func


def test_f():
    assert func.f() == 'success'


def test_add():
    assert func.add(12, 2) == 14
    assert func.add(8, -5) == 3
    assert func.add(-5, 8) == 3
    assert func.add(-5, -8) == -13
    assert func.add(28.23, 11.77) == 40.0


def test_to_tuple():
    assert func.to_tuple('one', 2, 3) == ('one', 2, 3)
    assert func.to_tuple(['t', 'a'], 2, 3) == (['t', 'a'], 2, 3)


def test_check5():
    assert func.check5(9)
    assert not func.check5(5)
    assert not func.check5(2)


def test_check_n():
    assert func.check_n(9, 7)
    assert not func.check_n(5, 5)
    assert func.check_n(2, 1)


def test_check_list():
    l = [1, 3, 4, 5, 34, 67, -34, -4]
    assert func.check_list(l, 5) == [False, False,
                                     False, True,
                                     True, True,
                                     False, False]


def test_check_list_nth():
    l = [1, 3, 4, 5, 34, 67, -34, -4]
    assert func.check_list_nth(l, 5, 3) == [False, True, False]
    assert func.check_list_nth(l, 5, 2) == [False, False, True, False]
    assert func.check_list_nth(l, 5, 1) == [False, False,
                                            False, True,
                                            True, True,
                                            False, False]


