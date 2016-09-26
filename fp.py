#!/usr/bin/python

from flask import Flask, render_template
import random
import occupation

app = Flask(__name__)

@app.route('/')
def initialize():
	return "Go to /occupations"

@app.route('/occupations')
def init():
	return render_template("template.html",title="Occupations Table",l=occupation.dic,occ=occupation.occ) 
	
if __name__ == '__main__':
	print "hello"
	app.run()


 