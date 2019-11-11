# Heroku Django Classifier Service

A web service that returns predictions from a pre-trained machine learning model.

Load a **TF-IDF vectorizer**, a pickled **MLP Classifier model** and predict a class, based on text passed in url parameters.

## Buildpacks required:

- https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku-community/apt.tgz
- heroku/python

## Features

- Support for numpy, scipy and scikit-learn
- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://chat-classifier.herokuapp.com/), ready to deploy.

Prediction: [link](https://chat-classifier.herokuapp.com/predict_chat/Hi%20product%20question)


## License: MIT
