[![CircleCI](https://circleci.com/gh/aguilarjose11/PyTestWorkout/tree/master.svg?style=svg)](https://circleci.com/gh/aguilarjose11/PyTestWorkout/tree/master)

PyTestWorkout
==============

pytest learning repository.
----------------------------

This repository contains code I wrote while learning pytest and CircleCI integration. __feel free to check this out for your own interest.__

### Libraries used in this project:

> flake8

> PyTest

> pytest-cov

> venv

Check out the './requirements.txt' for more info.

# local build.

* run flake.

'''shell
python -m flake8 --exclude=.\venv --ignore=E501 --statistics
'''

* run pytest.

'''shell
python -m pytest --cov={modules}, ...
'''
> ''{modules}'' - to replace with tested modules. remove if unnecessary.
