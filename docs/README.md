---
  You are expected to design, code, and present to the class a programming
  project that has a purpose (solves a real problem) for a real life user.


# Summer Project

## Introduction

Our Project is a **Stock Market Prediction tool** that utilises `Machine Learning` algorithms in models such as `Linear Regression` and `Support Vector Machine` in order to forecast the Stock Market changes for a certain period of time in the future.   
  
Users would be anyone over the age of **18,** attempting to _build_ or to _improve_ their **financial portfolio.** _****_Our tool will aid them in **investing** and **buying** shares from companies as well allowing them to maximise the profits and minimise their losses. It also allows more inexperienced users to attain an understanding of the movement of the **Stock Market** allowing them to make informed decisions about their future.

## Distribution

Our aims are to develop the tool as an _Official Python Package_ and upload it to [`PyPi`](https://pypi.org/) as an open-source package for use all around the world. Through this, we can make our project much more accessible and also increase its development by decreasing possible bugs through user engagement with platforms such as [`Github`](https://github.com/) allowing users to make [`Issues`](https://github.com/ARU300/SummerProject/issues) and [`Pull Requests`](https://github.com/ARU300/SummerProject/pulls) which can aid the development of the tool. We want to allow for multiple different **algorithms** to be used through the use of multiple **function** and **iteration** to make the results as accurate and reliable as possible. We will release the project in iteration ranging from`v0.1a` to `v2.1`+ using [`Github`](https://github.com/ARU300/SummerProject/releases) release system and will package and make public each major update, _i.e. one with  a major bug fix or a new version such as `v3.0.`_

## Integration

The users are people interested in **finance** or the **economy** and our tool can be easily integrated into websites using the [`Django`](https://www.djangoproject.com/)  or [`Flask`](https://flask.palletsprojects.com/en/1.1.x/) framework for Python or in applications on desktop using **C++** or mobile through **Java** and/or **Swift**. Another alternative would be to develop a `RESTful API` with `Flask` _\(which has been made\)_ and then integrating this with a [`NodeJS`](https://nodejs.org/en/) application on the [`Electron`](https://www.electronjs.org/) framework using `AJAX` requests in Back-End in order to transfer the data to a modern-looking **GUI** or application.

{% page-ref page="code/api.md" %}

## Releases

{% hint style="warning" %}
This may not be entirely up-to-date. For download, reference the [PyPi site](https://pypi.org/project/Summer-Project/) or the [Github site](https://github.com/ARU300/SummerProject/releases).
{% endhint %}

{% tabs %}
{% tab title="v2.2a" %}
## \*\*\*\*[**RTFD**](https://github.com/ARU300/SummerProject/releases/tag/v2.2a)\*\*\*\*

\_\_[_ARU300_](https://github.com/ARU300) _released this 8 hours ago ·_ [_4 commits_](https://github.com/ARU300/SummerProject/compare/v2.2a...master) _to master since this release_

* [Pre-Release](https://github.com/ARU300/SummerProject/commit/60ff49acceed82964c0e6351cc8b1c63307620b0)

 Another release for RTFD, updating the `mkdocs.yml`.
{% endtab %}

{% tab title="v2.1" %}
## [ReadTheDoc](https://github.com/ARU300/SummerProject/releases/tag/v2.1)

[_ARU300_](https://github.com/ARU300) _released this 9 hours ago ·_ [_7 commits_](https://github.com/ARU300/SummerProject/compare/v2.1...master) _to master since this release_

* [Release](https://github.com/ARU300/SummerProject/commit/0d4740826fbe26904b1ce0c8344eb5dbe418eeaf)

Added a `.readthedocs.yml` and a `mkdir.yml` in order to integrate support with the ReadTheDocsSite.

Documentation is now live on [Read The Docs](https://summerproj.readthedocs.io/en/master/).
{% endtab %}

{% tab title="v2.0" %}
##  [LSTM](https://github.com/ARU300/SummerProject/releases/tag/2.0)

 [_ARU300_](https://github.com/ARU300) _released this yesterday ·_ [_21 commits_](https://github.com/ARU300/SummerProject/compare/2.0...master) _to master since this release_

* [Release](https://github.com/ARU300/SummerProject/commit/fd1ded4debf9277d065e2025c1ce42a43b8eb8df)

Since `v1.0` we have developed a new method of Stock Market Prediction using the `Keras` libraries `LSTM` Model.

The `API` has also been updated to include these changes.

The next **major** update will entail document changes and maybe a deployment to `repl.it` or `Heroku`.
{% endtab %}

{% tab title="v1.0" %}
##  [API Prediction](https://github.com/ARU300/SummerProject/releases/tag/v1.0)

[_ARU300_](https://github.com/ARU300) _released this on 26 Jul ·_ [_32 commits_](https://github.com/ARU300/SummerProject/compare/v1.0...master) _to master since this release_

* [Release](https://github.com/ARU300/SummerProject/commit/869a91b313fa1e39cce38c4b170807620e0cc216)

## First Release!

Since `v0.1a`, we have made a few developments in terms of software.

### Errors

We have been ironing out errors in the code and making sure that the `Linear Regression` and `Support Vector Machine` algorithms work as expected.

### New Additions

We have developed an API and website in `Flask` that runs on `https:\\localhost:5000`. The API can be used to output the predictions.

### Future Development

We are going to integrate an `LSTM` algorithm + some other algorithms and iteration to find the best prediction possible. This is expected to be our `v2.0` release. The `v1.X` updates may mainly include website changes and documentation changes.
{% endtab %}

{% tab title="v0.1a" %}
## [Stock Analysis](https://github.com/ARU300/SummerProject/releases/tag/v1.0-alpha)

\_\_[_ARU300_](https://github.com/ARU300) _released this on 5 Jul ·_ [_32 commits_](https://github.com/ARU300/SummerProject/compare/v1.0-alpha...master) _to master since this release_

* [Pre-Release](https://github.com/ARU300/SummerProject/commit/869a91b313fa1e39cce38c4b170807620e0cc216)

## Stock Anlaysis

### What works?

**Disclaimer:** The project has only been active for around 2 days with under 12hrs of work.

* `Stock,py` works with a function named `getStock`. By entering the 'companyName' you can retrieve the stocks and a plot for the stocks from the previous year. \*\(To plot the results set the parameter 'plot' to true and 'mavgPlot' to true as well in order to plot the _Moving Average_ as well.
* `SVM Predict.py` does work, however in pre-release `v0.1-alpha` it is not yet a function however it shall be in the `v1.0` release.
* `Predict.py` does not work and will need to be improved and fixed.
{% endtab %}
{% endtabs %}

## Legal

Our project is licensed under the [**GNU General Public License v3.0**](https://github.com/ARU300/SummerProject/blob/master/LICENSE)**.**

> Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

