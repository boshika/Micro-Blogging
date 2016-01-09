from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = { 'nickname' : 'Boshika'}
  posts = [
      {
            'author': {'nickname': 'John'},
            'body' : 'Living in LA!'
      },
      {
            'author': {'nickname': 'Von'},
            'body' : 'Living in SF!'
      },
      {
            'author': {'nickname': 'Jim'},
            'body' : 'Living in NOLA!'
      }
  ]
  return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)