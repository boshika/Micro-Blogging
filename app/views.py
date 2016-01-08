from app import app

@app.route('/')
@app.route('/index')
def index():
  user = { 'nickename' : 'Boshika'}
  return render_template('index.html',
                           title='Home',
                           user=user)