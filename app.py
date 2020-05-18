from flask import Flask, render_template
from Scraper import Scraper
from flask_apscheduler import APScheduler

app = Flask(__name__)

s = Scraper()
s.parse()
websites = s.rank()

def repeat():
    s.parse()
    websites = s.rank()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', websites=websites)

if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(func=repeat, trigger='interval', id='repeat', seconds=86400)
    scheduler.start()
    app.run(debug=True)