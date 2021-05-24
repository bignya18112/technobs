from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/blogs")
def blog():

    return render_template('blog.html')


@app.route("/tools")
def tools():

    return render_template('tools.html')

@app.route("/contact")
def contact():

    return render_template('contact.html')

@app.route("/blogs/trialpost")
def trialpost():

    return render_template('trialpost.html')

app.run(debug=False, host='0.0.0.0')