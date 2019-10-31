# python-ci
python ci sample project

# CI PYTHON STEPS

Required software:
pip install flake8 pytest pytest-cov

Install project requirements:
* previously: pip freeze > requirements.txt
pip install -f requirements.txt

- Flake8
flake8 --statistics

- Test
pytest -v --cov

- Modify version in VERSION.py file

- Package (from setup.py location)
python setup.py sdist bdist_wheel

# WITH PYB

See goals (pyb -t)

+ pyb install_dependencies
+ pyb
