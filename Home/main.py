from flask import Flask,render_template
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('default.html')

@app.route('/marks')
def marks():
   webbrowser.open('https://flask-marks.el.r.appspot.com/')
   return render_template('default.html')

@app.route('/fees')
def fees():
   webbrowser.open('https://flask-fees.el.r.appspot.com/')
   return render_template('default.html')

if __name__ == '__main__':
   app.run(port=8001)