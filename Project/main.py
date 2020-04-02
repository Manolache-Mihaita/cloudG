import logging
import db_controller as db
from flask import Flask, render_template, request, Response
from wtforms import Form, TextAreaField, TextField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "1310a7d075f989192b9bb7c69ab6b043"


# noinspection PyDeprecation
'''class MainForm(Form):
    name = TextField('Name:', validators=[validators.DataRequired()])

    @app.route("/", methods=['GET', 'POST'])
    def mainPage():
        form = MainForm(request.form)
        name = ""
        print(form.errors)
        if request.method == 'POST':
            name = request.form['name']
        print(name)

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('main.html', form=form)

    @app.errorhandler(500)
    def server_error(e):
        logging.exception('An error occurred during a request.')
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    @app.errorhandler(404)
    def server_error(e):
        logging.exception('Accessed resource that doesnt exist!')
        # TODO: 404 message maby ?
        # return """
        # SOME 404 message
        # """.format(e),
        return render_template("404.html")
'''

@app.before_first_request
def create_table_translations():
    db.create_table_translations()
    #tst = db.insert_translation("en", "ro", "hello", "salut")


@app.route("/", methods=["GET"])
def index():
    translations = db.get_all_translations()

    return render_template(
        "home.html", translations=translations
    )

@app.route("/home", methods=["GET"])
def home():
    translations = db.get_all_translations()

    return render_template(
        "home.html", translations=translations
    )

@app.route("/translations", methods=["GET"])
def translate():
    translations = db.get_all_translations()

    return render_template(
        "translations.html", translations=translations
    )

@app.route("/text-to-speech", methods=["GET"])
def text_to_speech():
    translations = db.get_all_translations()

    return render_template(
        "text_to_speech.html", translations=translations
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
