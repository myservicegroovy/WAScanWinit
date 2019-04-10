#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from time import strftime
from random import randint,choice
from string import ascii_uppercase, ascii_lowercase

def r_time():
	""" random numbers """
	return randint(0,int(strftime('%y%m%d')))

def r_string(n):
	""" random strings """
	return "".join([choice(ascii_uppercase+ascii_lowercase) for _ in range(0,int(n))])