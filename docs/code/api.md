# API

We used the `Flask` library in **Python** to develop a basic API. There are currently no **Auth** headers and the customisation of the API via **headers** is being developed.

This `API` is a **Work In Progress.** Although it provides basic functionality some responses may be much slower than others and the error messages may not be as informative as needed. 

## Initial Code

```python
from flask import Flask, render_template, request, jsonify, abort
from Stock_Analysis.Predict import stockPredict

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True


@app.route('/')
def home():
    return render_template("docs.html")


@app.errorhandler(404)
def page_not_found(e):
    # return render_template('404.html'), 404
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    # return render_template('500.html'), 500
    return jsonify(error=str(e)), 500
```

This is the main code that creates the `Flask` app and handles **basic errors**.

The `LSTM API` can be slow due to the time taken for the Python function to run. **Refreshing the page** will only make this worse.
