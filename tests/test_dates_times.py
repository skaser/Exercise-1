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
Tests for date and time exercises
'''

import ex1.dates_times as dts
from datetime import date, time, datetime


def test_last_of_month():
    assert dts.last_of_month(date(2007, 5, 23)) == date(2007, 5, 31)
    assert dts.last_of_month(date(2004, 2, 2)) == date(2004, 2, 29)
    assert dts.last_of_month(date(1900, 2, 2)) == date(1900, 2, 28)


def test_feed_the_gremlin():
    assert dts.feed_the_gremlin(time(23, 59, 59)) == True
    assert dts.feed_the_gremlin(time(0, 0, 1)) == False
    assert dts.feed_the_gremlin(time(6, 29, 59)) == False
    assert dts.feed_the_gremlin(time(6, 30, 0)) == True


def test_how_long():
    answer = "5366 days, 34 minutes, 56 seconds since 1985-04-23 12:00:00"
    answer1 = "5366 days, 34 minutes, 56 seconds until 2000-01-01 12:34:56"
    d1 = datetime(2000, 1, 1, 12, 34, 56)
    d2 = datetime(1985, 4, 23, 12, 0, 0)
    assert dts.how_long(d1, d2) == answer
    assert dts.how_long(d2, d1) == answer1
