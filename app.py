from flask import Flask, render_template
from Scraper import Scraper

app = Flask(__name__)

s = Scraper()
websites = s.rank()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', websites=websites)

if __name__ == '__main__':
    app.run(debug=True)