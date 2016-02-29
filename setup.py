from setuptools import setup

install_requires = []

tests_requires = [
    'mock',
    'flake8',
    'coverage'
    ]

packages = ['blackjack']

setup(
    name="BlackJack",
    version="0.1",
    py_modules=["blackjack"],
    install_requires=install_requires,
    tests_require=tests_requires,
    packages=packages,
)
