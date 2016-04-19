from flask import Flask, render_template, abort
import os
import codecs
import markdown

app = Flask(__name__)

@app.route('/')
def index():
	flist = os.listdir('articles')
	return render_template('index.html', flist = flist)

@app.route('/a/<file_name>')
def article(file_name):
	try:
		fin = codecs.open('articles/'+file_name, mode='r', encoding='utf-8')
	except IOError:
		return abort(404)
	html = markdown.markdown(fin.read())
	fin.close()
	return render_template('article.html', html = html)

if __name__ == '__main__':
	app.run(debug=False)