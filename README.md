# BUFpython
Basic Utilities For python

Current Utilities:

Toggleable Variables
usage: 
	from BUFpy import toggleables
	var = Toggleable(value=False)
	print(var.value)#outputs False
	var.toggle()
	print(var.value)#outputs True
	var.t()
	print(var.value)#outputs False
	var.setVal(True)

Logging
usage:
	from BUFpy import logging
	logger = Logger(file, logTime,)
	logger.settings(file="fizzbuzz.log", logTime=False)
	logger.log(level, "fizz, buzz, fizzbuzz")
	#level -1 means "[time][ERROR] : message" will be logged
	#level 0 means "[time][INFO] : message" will be logged
	#level 1 means "[time][WARNING]: message" will be logged
	#if level is a string, "[time][theInputedString] : message" will be logged
