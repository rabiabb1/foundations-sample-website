from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first-page')
def first_page():
    return render_template('first-page.html', page_title="About CODE")


@app.route('/second-page')
def second_page():
    return render_template('second-page.html', page_title="My Experience at CODE")


@app.route('/contact-page')
def contact_page():
    return render_template('contact-page.html', page_title="Contact Me")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
