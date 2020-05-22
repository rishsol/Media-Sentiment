from flask import Flask, render_template
from Scraper import Scraper
from flask_apscheduler import APScheduler

app = Flask(__name__)

s = Scraper()
s.parse()
websites = s.rank()
ranked = [list(websites[0])[0], list(websites[0])[6]]

def repeat():
    s.parse()
    websites = s.rank()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', websites=websites, ranked=ranked)

if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(func=repeat, trigger='interval', id='repeat', seconds=86400) #repeat everyday
    scheduler.start()
    app.run(debug=True)