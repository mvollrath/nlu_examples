NLU Examples
------------

### Basic

An example of an extremely primitive neural network NLU classifier made with [Keras](https://keras.io/).

The purpose of this example is to demonstrate a supervised machine learning NLU in a setting limited enough that a working network can be solved with pencil and paper.

To run this example in Docker, use `run_basic.sh`.  Sources are in `examples/basic`.

### Rasa

An example of intent classification and entity extraction with [Rasa NLU](https://github.com/RasaHQ/rasa_nlu).

The purpose of this example is to demonstrate a full-featured NLU implementation stack from training data to web front-end.  A web form recognizes requests for food and random numbers in a given range.

For example, it will recognize "i want some pizza" as a food craving (for pizza) and "random number between 1 and 100" as a random number request (between 1 and 100, inclusive).

To run this example in Docker, use `run_rasa.sh`.  The application will be listening on <http://localhost:8080>.  Sources and training data are in `examples/rasa`.

### [Slides](https://docs.google.com/presentation/d/1gHRVUvyYcAvfx4dyoTU-zh3Msf5o-HqYvtL5ilP3djM/edit?usp=sharing)
