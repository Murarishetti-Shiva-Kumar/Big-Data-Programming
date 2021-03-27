from flask import Flask, render_template, send_file
import queries

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/hello.html')
def hello_world():
    return render_template('hello.html')

@app.route('/first.html')
def first():
    return render_template('first.html')


@app.route('/first.png')
def first_plot():
    graph_1 = queries.get_query1()
    return send_file(graph_1, mimetype='image/png', cache_timeout=0)

if __name__ == '__main__':
    app.run()
