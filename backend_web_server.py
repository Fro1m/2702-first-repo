from flask import Flask, render_template
app = Flask(__name__, template_folder='C:/Users/danie/Desktop/wargame')


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('kaki.html')


@app.route('/faction1.html')
def faction1():
    return render_template('faction1.html')


@app.route('/faction2.html')
def faction2():
    return render_template('faction2.html')


@app.route('/faction3.html')
def faction3():
    return render_template('faction3.html')


@app.route('/try', methods=['POST', 'GET'])
def trylol():
    return render_template('trylol.html')


if __name__ == '__main__':
    app.run(debug=True)