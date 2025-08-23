from flask import Flask, render_template

#cохраняем экземплятор класса
app = Flask(__name__)

#@-декоратирующая функция
@app.route('/')
def index():
    context = {
        'title': 'Сайт Рустама | Главная',
    }
    return render_template("index.html", **context)

@app.route('/blog/')
def blog():
    context = {
        'title': 'Сайт Рустама | Блог',
    }
    return render_template("blog.html", **context)

@app.route('/contats/')
def contacts():
    context = {
        'title': 'Сайт Рустама | Контакты',
    }
    return render_template("contacts.html", **context)

if __name__ == '__main__':
    app.run(debug=True)