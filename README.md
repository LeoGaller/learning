# Continuous Self Improvement - Python SE

A brief description of your project.

## Table of Contents
- [Installation](#installation)
- [Characteristics](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation
### Very Important
**Before installing any packages, make sure to update your operating system.**


Install needed software:
1. [Install PyEnv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. [Install poetry](https://python-poetry.org/docs/#installation)

## Characteristics

- We use Pyenv to set the local version of python to 3.8.0 and have a second version available 3.7.7
- Tests should have their own folder
- The file `__init__.py` is empty and serves to declare the test suite as a package.

## Features

- Dependency management with Poetry
- Consuming a REST API with Requests
- PyTest
- Unit Tests
- Linting
-

## Important concepts
1. The file __init__.py is empty and serves to declare the test suite as a package. While this is not strictly necessary, 
it allows your test suite to mirror the source layout of the package under test, even when modules in different parts of
the source tree have the same name. Furthermore, it gives you the option to import modules from within your tests package.
2. Test Fixture == Test Context ==> In the context of software a test fixture (also called "test context") is used to set 
up system state and input data needed for test execution.
3. Coverage: It monitors your program, noting which parts of the code have been executed, then analyzes the source to 
identify code that could have been executed but was not. Coverage measurement is typically used to gauge the 
effectiveness of tests. It can show which parts of your code are being exercised by tests, and which are not.
Install it with the pytest-cov plugin, which integrates Coverage.py with pytest.
4. Automate tests in multiple unvironments. Nox == is a command-line tool that automates testing in multiple Python 
environments, similar to tox. Unlike tox, Nox uses a standard Python file for configuration.
5. Unit tests should be fast, isolated, and repeatable. The unittest.mock standard library allows you to replace parts 
of your system under test with mock objects. You should generally have a single assertion per test case, because more 
fine-grained test cases make it easier to figure out why the test suite failed when it does.
   1. *Tests for a feature or bugfix should be written before implementation. This is also known as “writing a failing 
   test". The reason for this is that it provides confidence that the tests are actually testing something, and do not 
   simply pass because of a flaw in the tests themselves.*
   2. The mock_requests_get fixture is now used by two test modules. You could move it to a separate module and import 
   from there, but Pytest offers a more convenient way: Fixtures placed in a conftest.py file are discovered 
   automatically, and test modules at the same directory level can use them without explicit import.
   3. Using fakes: Fake implementations are a good alternative to mock objects, which can be too forgiving when faced 
   with wrong usage, and too tightly coupled to implementation details of the system under test (witness the 
   mock_requests_get fixture).
6. Linting is the process of analyzing source code for potential errors, stylistic issues, or other problems that could 
impact the quality, readability, or functionality of the code. It is typically performed by specialized tools called 
linters, which parse and examine code to detect issues like syntax errors, improper formatting, unused variables, or 
code that does not adhere to specified coding standards.


## Contributing

Guidelines for contributing.

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Updated by [L2 Analytics](https://l2-analytics.com) - feel free to contact me!

## Acknowledgments

- Thanks to God for energy.
- Thanks Claudio Jolowicz for creating it.

## Important 
- [Choose a License](https://choosealicense.com/)
- Replace `hypermodern-python` with the name of your own repository, to avoid a name collision on 
PyPI.
- A virtual environment gives your project an isolated runtime environment, consisting of a specific
 Python version and an independent set of installed Python packages. This way, the dependencies of 
 your current project do not interfere with the system-wide Python installation, or other projects 
 you’re working on.
- For using nox you must create the noxfile.py at the root folder of the project and the pytest and pytest-cov
must be installed using pip in the local environment.
-- Nox recreates the virtual environments from scratch on each invocation (a sensible default). You can speed things up 
by passing the --reuse-existing-virtualenvs (-r) option
- Linting with [Flake8](https://flake8.pycqa.org/en/latest/)

## Reference
1. [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
2. [Hypermodern Python 02 Testing](https://cjolowicz.github.io/posts/hypermodern-python-02-testing/)
3. [Hypermodern Python 03 Linting](https://cjolowicz.github.io/posts/hypermodern-python-03-linting/)

## Support Knowledge
1. https://docs.pytest.org/en/latest/explanation/fixtures.html
2. https://coverage.readthedocs.io/en/7.6.1/
3. https://nox.thea.codes/en/stable/
4. [Using Fakes] https://cjolowicz.github.io/posts/hypermodern-python-02-testing/#:~:text=your%20terminal%20emulator).-,Using,-fakes

## Where to restart?
---> [Here](https://cjolowicz.github.io/posts/hypermodern-python-03-linting/#:~:text=in%20later%20sections.-,Code%20formatting%20with%20Black,-The%20next%20addition)