
#author = "James <jamespatten1996@gmail.com>"

import pandas as pd
from flask import Flask
from flask import Flask, flash, redirect, url_for, render_template, request, session, abort
import os
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug import secure_filename
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
#from ner import chunker

def chunker(sentence):
	if __name__ == "__main__":
		tokens = nltk.word_tokenize(sentence)
		print("tokens = %s" % tokens)
		tagged = nltk.pos_tag(tokens)
		entities = nltk.chunk.ne_chunk(tagged)
		print("entities = %s" % entities)
		return entities

app = Flask(__name__)
app.config.from_object(__name__)
#server = Server(app.wsgi_app)
#server.serve()

@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['sentence']
        print(sentence)
        results = chunker(sentence)
        return render_template('results.html', results=results, sentence=sentence)
    else:
        return render_template('index.html')
	
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
	
