# BUFpython
Basic Utilities For python<br/>
<br/>
Below are the current utilities in this package<br/>
<br/>
## Toggleable Variables<br/>
usage: <br/>
&emsp;import BUFpy<br/>
&emsp;var = BUFpy.Toggleable(value=False)<br/>
&emsp;print(var.value)#outputs False<br/>
&emsp;var.toggle()<br/>
&emsp;print(var.value)#outputs True<br/>
&emsp;var.t()<br/>
&emsp;print(var.value)#outputs False<br/>
&emsp;var.setVal(True)<br/>
<br/>
## Logging<br/>
usage:<br/>
&emsp;import BUFpy<br/>
&emsp;logger = BUFpy.Logger(file, logTime,)<br/>
&emsp;logger.settings(file="fizzbuzz.log", logTime=False)<br/>
&emsp;logger.log(level, "fizz, buzz, fizzbuzz")<br/>
&emsp;#level -1 means "[time][ERROR] : message" will be logged<br/>
&emsp;#level 0 means "[time][INFO] : message" will be logged<br/>
&emsp;#level 1 means "[time][WARNING]: message" will be logged<br/>
&emsp;#if level is a string, "[time][theInputedString] : message" will be logged<br/>
