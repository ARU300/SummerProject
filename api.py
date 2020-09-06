from flask import Flask, render_template, request, jsonify, abort
from StockAnalysis.Predict import stockPredict

app = Flask(__name__, template_folder='templates') #, static_folder='C:\\Users\\athavan\\Documents\\Projects\\Summer\\SummerProject\\templates')
app.config["DEBUG"] = True


@app.route('/')
def home():
    return render_template("Summer Project.html")


@app.errorhandler(404)
def page_not_found(e):
    #return render_template('404.html'), 404
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    #return render_template('500.html'), 500
    return jsonify(error=str(e)), 500

@app.route('/api/v0.1a/stocks/lr/', methods=['GET'])
def get_lr():
    try:
        if 'name' in request.args:
            name = str(request.args['name'])
        else:
            abort(404, description="Invalid URL")

        data = []

        confidence, prediction, dates = stockPredict(future=True, companyName=name, SVM=False, LR=True, LSTM=False, confidence_test=True, plot_stockPredict=False)

        data = [
            {'Company': name,
             'Method': 'Linear Regression',
             'Prediction': prediction,
             'Confidence': confidence,
             'Dates': dates}
        ]

        return jsonify(data)
    except Exception as e:
        print(e)
        abort(404, description="Resource not found. Check your spelling.")

@app.route('/api/v0.1a/stocks/svm/', methods=['GET'])
def get_svm():
    try:
        if 'name' in request.args:
            name = str(request.args['name'])
        else:
            abort(404, description="Invalid URL")

        data = []

        confidence, prediction, dates = stockPredict(future=True, companyName=name, SVM=True, LR=False, LSTM=False, confidence_test=True)

        data = [
            {'Company': name,
             'Method': 'Linear Regression',
             'Prediction': prediction,
             'Confidence': confidence,
             'Dates': dates}
        ]

        return jsonify(data)
    except Exception as e:
        print(e)
        abort(404, description="Resource not found. Check your spelling.")
        
@app.route('/api/v0.1a/stocks/lstm/', methods=['GET'])
def get_lstm():
    try:
        if 'name' in request.args:
            name = str(request.args['name'])
        else:
            abort(404, description="Invalid URL")

        r1 = [
            {
                'Disclaimer': 'Please be patient. This may take a while...'
            }
        ]
        
        #yield jsonify(r1)
        
        data = []

        confidence, prediction, dates = stockPredict(future=True, companyName=name, SVM=False, LR=False, LSTM=True, confidence_test=True, plot_stockPredict=False)

        data = [
            {'Company': name,
             'Method': 'LSTM',
             'Prediction': prediction,
             'Confidence': confidence,
             'Dates': dates}
        ]

        return jsonify(data)
    except Exception as e:
        print(e)
        abort(404, description="Resource not found. Check your spelling.")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=False)
