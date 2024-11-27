from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clock')
def clock():
    now = datetime.now()
    return render_template('clock.html', datetime=now.strftime('%d/%m/%Y %H:%M:%S'))

if __name__ == '__main__':
    app.run(debug=True)
