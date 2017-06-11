from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar

app.secret_key = "ABC"

# YOUR ROUTES GO HERE

JOB_SELECTION = ['Software Engineer', 'QA Engineer', 'Product Manager']
# JOB_SELECTION = {
#     'dev': 'Software Developer',
#     'qa': 'QA Engineer',
#     'pm': 'Product Manager'
# }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/application-form')
def application_form():
    return render_template('application-form.html', job_selection=JOB_SELECTION)


@app.route('/application-success')
def application_success():

    first_name = request.args.get('firstname')
    last_name = request.args.get('lastname')
    salary = request.args.get('salary')
    job = request.args.get('job')
    # job = JOB_SELECTION[request.args.get('job')]

    return render_template('application-response.html', first_name=first_name,
                           last_name=last_name, salary=salary, job=job)

# def format_currency(value):
#     return "${:,.2f}".format(float(value))

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
