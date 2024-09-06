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

## Contributing

Guidelines for contributing.

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [L2 Analytics](https://l2-analytics.com) - feel free to contact me!

## Acknowledgments

- Thanks to God for inspiration.

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

## Reference
1. [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
2. [Hypermodern Python 02 Testing](https://cjolowicz.github.io/posts/hypermodern-python-02-testing/)
3. 

## Support Knowledge
1. https://docs.pytest.org/en/latest/explanation/fixtures.html
2. https://coverage.readthedocs.io/en/7.6.1/
3. https://nox.thea.codes/en/stable/