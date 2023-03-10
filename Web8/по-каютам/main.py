from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def image_mars():
    astronauts = ["Ридли Скотт", "Энди Уир", "Марк Уотни"]
    return render_template("index.html", astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
