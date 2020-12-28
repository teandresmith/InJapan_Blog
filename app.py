'This Python File uses Flask to render web pages'

from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def home():
    '''This function renders the home web page'''
    return render_template('home.html')


@app.route('/about')
def about():
    '''This function renders the about me web page'''
    return render_template('about.html')


@app.route('/resources/web_resources')
def web_resources():
    '''This function renderes the Resources web page'''
    return render_template('web_resources.html')


@app.route('/resources/common_phrases')
def common_phrases():
    '''This function renders the common phrases web page'''
    return render_template('common_phrases.html')

@app.route('/blog')
def blog():
    '''This function renders the blog web page'''
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)