from flask import render_template, flash, redirect, session, url_for, request, g 
from flask.ext.login import login_user, logout_user, current_user, login_required 
from app import app, db, lm, oid 
from .forms import LoginForm
from .models import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
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
  @lm.user_loader
  def load_user(id):
    return User.query.get(int(id))