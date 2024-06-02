from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['1', '2', '3']


# представления, как в Django, которые вызывает пользователь через веб-сервер
@app.route("/about/<path:username>") # можем указать свою переменную, в которую может писать пользователь
def hello_world(username):
    #path = получаем оставшиеся путь
    print(url_for('hello_world', username=username)) #возвращаем url адрес, куда перешел пользователь сейчас
    return render_template('index.html', title="Про Flask", menu=menu, username=username)


if __name__ == '__main__':
    app.run(debug=True)
