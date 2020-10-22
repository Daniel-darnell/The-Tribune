from flask import render_template
from app import app


#Views 
@app.route('/')
def index():
    
    '''
    A view root function that returns the index page and its data
    '''
    message = 'Hello World'
    return render_template('index.html', message = message)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    A view news page function that returns the news details and its data
    '''
    return render_template('news.html', id = news_id)