from flask import Flask, render_template, request, jsonify, abort
from SVM_Predict import *

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True


@app.route('/')
def home():
    return render_template("docs.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/api/v0.1a/predict/company/lr', methods=['GET'])
def get_tasks():
    try:
        if 'name' in request.args:
            name = str(request.args['name'])
        else:
            abort(404, description="Invalid URL")

        data = []

        confidence, prediction, dates = stockPredict(future=True, companyName=name, SVM=False, LR=True, confidence_test=True)

        data = [
            {'Company': name,
             'Method': 'Linear Regression',
             'Prediction': prediction,
             'Confidence': confidence,
             'Dates': dates}
        ]

        return jsonify(data)
    except Exception as e:
        abort(404, description="Resource not found")

@app.route('/api/v0.1a/predict/company/svm', methods=['GET'])
def get_tasks():
    try:
        if 'name' in request.args:
            name = str(request.args['name'])
        else:
            abort(404, description="Invalid URL")

        data = []

        confidence, prediction, dates = stockPredict(future=True, companyName=name, SVM=True, LR=False, confidence_test=True)

        data = [
            {'Company': name,
             'Method': 'Linear Regression',
             'Prediction': prediction,
             'Confidence': confidence,
             'Dates': dates}
        ]

        return jsonify(data)
    except Exception as e:
        abort(404, description="Resource not found")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=False)
