---
description: This is where I will explain the function and code behind the API file.
---

# API

We used the `Flask` library in **Python** to develop a basic API. There are currently no **Auth** headers and the customisation of the API via **headers** is being developed.

{% hint style="warning" %}
This `API` is a **Work In Progress.** Although it provides basic functionality some responses may be much slower than others and the error messages may not be as informative as needed. 
{% endhint %}

## Initial Code

{% tabs %}
{% tab title="Python" %}
{% code title="api.py" %}
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
{% endcode %}
{% endtab %}
{% endtabs %}

This is the main code that creates the `Flask` app and handles **basic errors**.

The rest of the code is used to develop the API `GET` methods that will be presented here.

{% api-method method="get" host="https://localhost:5000/api/v0.1a/stocks/" path="lr/?name={name}" %}
{% api-method-summary %}
Linear Regression
{% endapi-method-summary %}

{% api-method-description %}
Integrates a `Linear Regression` Model
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="name" type="string" required=true %}
This parameter defines the **name** of the company you are searching for.
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
This is a **successful** response and return all the values from the functions.
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Company': name, // Company Name
 'Method': 'Linear Regression',
 'Prediction': prediction, // Array of prediction
 'Confidence': confidence, // r^2 Confidence Score
 'Dates': dates // Array of dates for prediction
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
The **URL** is missing the `?name=` arguement.
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Error': 'Invalid URL',
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
The name given has returned an error. Usually this is to do with the name being _invalid and a common misspelling._
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Error': 'Resource not found. Check your spelling.'
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://localhost:5000/api/v0.1a/stocks/" path="svm/?name={name}" %}
{% api-method-summary %}
Support Vector Machine
{% endapi-method-summary %}

{% api-method-description %}
Integrates a `Support Vector Machine` Model
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="name" type="string" required=true %}
This paramater defined the **name** of the company you are searching for.
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Successful!
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Company': name, // Company Name
 'Method': 'Linear Regression',
 'Prediction': prediction, // Array of prediction
 'Confidence': confidence, // r^2 Confidence Score
 'Dates': dates // Array of dates for prediction
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Missing an arguement
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Error': 'Invalid URL',
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
Incorrect Company Name
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Error': 'Resource not found. Check your spelling.'
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://localhost:5000/api/v0.1a/stocks/" path="lstm/?name={name}" %}
{% api-method-summary %}
LSTM
{% endapi-method-summary %}

{% api-method-description %}
Integrates an `LSTM` model
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="name" type="string" required=true %}
The name of the company you are searching for.
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Successful! 
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Company': name, // Company Name
 'Method': 'Linear Regression',
 'Prediction': prediction, // Array of prediction
 'Confidence': confidence, // r^2 Confidence Score
 'Dates': dates // Array of dates for prediction
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Missing an arguement
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="JSON" %}
```cpp
{
 'Error': 'Invalid URL',
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
Name is incorrect
{% endapi-method-response-example-description %}

{% tabs %}
{% tab title="C++" %}
```cpp
{
 'Error': 'Resource not found. Check your spelling.'
}
```
{% endtab %}
{% endtabs %}
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% hint style="danger" %}
The `LSTM API` can be slow due to the time taken for the Python function to run. **Refreshing the page** will only make this worse.
{% endhint %}

