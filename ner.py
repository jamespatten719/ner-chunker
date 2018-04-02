# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 13:38:02 2018

@author: jamespatten
"""
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
print("Content-type: text/html")
print """
  <!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title>NER CHUNKER</title>
	<style>

	</style>
</head>

<body>
	<p id="ner"></p>
	<script>
	
	var sentence = prompt("Please enter a sentence", "E.g. Sarah works for Deloitte");
	document.getElementById("ner").innerHTML = sentence;
	
	</script> 
</body>
"""
form = cgi.FieldStorage()

import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk import word_tokenize, pos_tag, ne_chunk

if __name__ == "__main__":
    

	sentence = form.getvalue('ner')
	tokens = nltk.word_tokenize(sentence)
	print("tokens = %s" % tokens)

	tagged = nltk.pos_tag(tokens)

	entities = nltk.chunk.ne_chunk(tagged)
	print("entities = %s" % entities)
