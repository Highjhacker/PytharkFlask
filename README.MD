![Imgur](https://i.imgur.com/ysh3akS.png)

# PytharkFlask

A Pythark example based on Flask, allowing us to search for delegates.

## Built with
- [Python](https://www.python.org/)
- [PythArk](https://github.com/Highjhacker/pythark/)
- [Flask](http://flask.pocoo.org/)

## Installation

The first step is to clone this repository : 
```shell
$ git clone https://github.com/Highjhacker/PytharkFlask.git
```

Then go inside the cloned repository and create a virtualenvironment([How to create a VirtualEnvironment](http://virtualenv.readthedocs.io/en/stable/))
```shell
$ cd PytharkFlask
$ virtualenv venv 
# Or if you want to specify a python version
$ virtualenv -p python3.6 venv # If python3.6 is a correct command
```
When the virtualenv is created, all you need to do is to install the dependencies from the requirements.txt file
```shell
pip install -r requirements.txt
```
When the dependencies are installed, you need to export some variables for Flask
```shell
$ export FLASK_APP=run.py
# The differents configurations are inside the config.py file
$ export APP_SETTINGS=config.DevelopmentConfig
```

And you should be ready to run it
```
$ flask run
```

## TODOS

## Authors

- Jolan Beer - Highjhacker

## License

PytharkFlask is under MIT license. See the [LICENSE file](https://github.com/Highjhacker/PytharkFlask/blob/master/LICENSE) for more informations.
