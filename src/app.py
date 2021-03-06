from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/biografia")
def biografia():
    return render_template('biografia.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')


if __name__ == "__main__":
    app.run(debug=True)