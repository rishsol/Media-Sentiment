from flask import Flask
from Scraper import Scraper

app = Flask(__name__)
s = Scraper()
@app.route('/')
def rankings():
    websites = s.rank()
    return str(websites)

if __name__ == '__main__':
    app.run(debug=True)