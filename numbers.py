#!/usr/bin/python
"""Accepts a number from a form."""

import cgi
form = cgi.FieldStorage()
print("Content-Type: text/plain\n")
try:
  n = form[’number’].value
  print("your number is " + n)
except KeyError:
  print("please enter a number")
