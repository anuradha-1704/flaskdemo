from flask import Flask

# initilize the application
app= Flask(__name__)

@app.route('/')
def hello():
    return "Hello World:"

@app.route('/home')
def home():
    return "Home Page:"

@app.route('/contact')
def contact():
    return "Contact Page:"

if __name__=='__main__':
    app.run()
