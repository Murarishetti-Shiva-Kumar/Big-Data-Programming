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


# @app.route('/second.html')
# def second():
#     return render_template('second.html')
#
#
# @app.route('/second.png')
# def second_plot():
#     graph_2 = queries.get_query2()
#     return send_file(graph_2, mimetype='image/png', cache_timeout=0)


@app.route('/third.html')
def third():
    return render_template('third.html')


@app.route('/third.png')
def third_plot():
    graph_3 = queries.get_query3()
    return send_file(graph_3, mimetype='image/png', cache_timeout=0)


# @app.route('/fourth.html')
# def fourth():
#     return render_template('fourth.html')
#
#
# @app.route('/fourth.png')
# def fourth_plot():
#     graph_4 = queries.get_query4()
#     return send_file(graph_4, mimetype='image/png', cache_timeout=0)

@app.route('/sixth.html')
def sixth():
    return render_template('sixth.html')


@app.route('/sixth.png')
def sixth_plot():
    graph_6 = queries.get_query6()
    return send_file(graph_6, mimetype='image/png', cache_timeout=0)


@app.route('/seventh.html')
def seventh():
    return render_template('seventh.html')


@app.route('/seventh.png')
def seventh_plot():
    graph_7 = queries.get_query7()
    return send_file(graph_7, mimetype='image/png', cache_timeout=0)


@app.route('/eighth.html')
def eighth():
    return render_template('eighth.html')


@app.route('/eighth.png')
def eighth_plot():
    graph_8 = queries.get_query8()
    return send_file(graph_8, mimetype='image/png', cache_timeout=0)


@app.route('/ninth.html')
def ninth():
    return render_template('ninth.html')


@app.route('/ninth.png')
def ninth_plot():
    graph_9 = queries.get_query9()
    return send_file(graph_9, mimetype='image/png', cache_timeout=0)


# @app.route('/tenth.html')
# def tenth():
#     return render_template('tenth.html')
#
#
# @app.route('/tenth.png')
# def tenth_plot():
#     graph_10 = queries.get_query10()
#     return send_file(graph_10, mimetype='image/png', cache_timeout=0)


# @app.route('/eleven.html')
# def eleven():
#     return render_template('eleven.html')
#
#
# @app.route('/eleven.png')
# def eleven_plot():
#     graph_11 = queries.get_query11()
#     return send_file(graph_11, mimetype='image/png', cache_timeout=0)


@app.route('/twelve.html')
def twelve():
    return render_template('twelve.html')


@app.route('/twelve.png')
def twelve_plot():
    graph_12 = queries.get_query12()
    return send_file(graph_12, mimetype='image/png', cache_timeout=0)


@app.route('/thirteen.html')
def thirteen():
    return render_template('thirteen.html')


@app.route('/thirteen.png')
def thirteen_plot():
    graph_13 = queries.get_query13()
    return send_file(graph_13, mimetype='image/png', cache_timeout=0)


@app.route('/fourteen.html')
def fourteen():
    return render_template('fourteen.html')


@app.route('/fourteen.png')
def fourteen_plot():
    graph_14 = queries.get_query14()
    return send_file(graph_14, mimetype='image/png', cache_timeout=0)


# @app.route('/fifteen.html')
# def fifteen():
#     return render_template('fifteen.html')
#
#
# @app.route('/fifteen.png')
# def fifteen_plot():
#     graph_15 = queries.get_query15()
#     return send_file(graph_15, mimetype='image/png', cache_timeout=0)


# @app.route('/sixteen.html')
# def sixteen():
#     return render_template('sixteen.html')
#
#
# @app.route('/sixteen.png')
# def sixteen_plot():
#     graph_16 = queries.get_query16()
#     return send_file(graph_16, mimetype='image/png', cache_timeout=0)


@app.route('/seventeen.html')
def seventeen():
    return render_template('seventeen.html')


@app.route('/seventeen.png')
def seventeen_plot():
    graph_17 = queries.get_query17()
    return send_file(graph_17, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run()
