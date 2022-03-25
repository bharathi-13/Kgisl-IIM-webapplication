from flask import Flask, render_template, url_for

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/index.html')
def index ():
    return render_template('index.html')

@app.route('/register.html')
def register ():
    return render_template('register.html')

@app.route('/login.html')
def login ():
    return render_template('login.html')

@app.route('/about.html')
def about ():
    return render_template('about.html')

@app.route('/contact.html')
def contact ():
    return render_template('contact.html')

@app.route('/engagement.html')
def engagement ():
    return render_template('engagement.html')

if __name__ == '__main__':
    app.run(debug=True)