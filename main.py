from flask import Flask, render_template

#cохраняем экземплятор класса
app = Flask(__name__)

#@-декоратирующая функция
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/blog/')
def blog():
    return render_template("blog.html")

@app.route('/contats/')
def contacts():
    return render_template("contacts.html")

if __name__ == '__main__':
    app.run(debug=True)