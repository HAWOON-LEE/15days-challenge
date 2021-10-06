from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/weather')
def weather():
   return render_template('weather.html')

@app.route('/tour')
def tour():
   return render_template('tour.html')
   

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)