"""
everything below is google cloud stuff - > no MIM-code, yet!
"""

# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging

from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, TextField, validators, StringField, SubmitField

#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Claudiu unde e tema la cloud :( ?'
#
#
# @app.errorhandler(500)
# def server_error(e):
#     logging.exception('An error occurred during a request.')
#     return """
#     An internal error occurred: <pre>{}</pre>
#     See logs for full stacktrace.
#     """.format(e), 500
#
#
# if __name__ == '__main__':
#     # This is used when running locally. Gunicorn is used to run the
#     # application on Google App Engine. See entrypoint in app.yaml.
#     app.run(host='127.0.0.1', port=8080, debug=True)
# # [END gae_flex_quickstart

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "1310a7d075f989192b9bb7c69ab6b043"


# noinspection PyDeprecation
class MainForm(Form):
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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
