# noxfile.py
import nox
""" Sometimes, you need to pass additional options to pytest, for example to select specific test cases. Change the 
session to allow overriding the options passed to pytest, via the session.posargs variable"""

@nox.session(python=["3.8", "3.7"])
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"] # exclude end-to-end tests from automated testing by passing -m "not e2e" to Pytest
    session.run("poetry", "install", external=True) # we specify external to avoid warnings about external commands leaking into the isolated test environments
    session.run("pytest", *args)