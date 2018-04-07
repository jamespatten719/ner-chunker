#!/usr/bin/python3
import cgi
import cgitb 
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1>Named Entity Recognition </h1>")
form = cgi.FieldStorage()
if form.getvalue("sentence"):
        sentence = form.getvalue("sentence")
	print("<h1>Hello "+sentence+"! Thanks for using my script!</h1><br />")
print("<form method='post' action='ner.py'>")
print("<p>Please enter a sentence:  <input type='text' name='sentence'/></p>")
print("<input type='submit' value='Submit' />")
print("</form>")
print("</body></html>")
                        



