# January 7, 2024
# This is my test to package management with poetry
## I'm @LeoGaller
---
## Glossary
- **Modules**: If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules.
- **built-in modules**: Modules that are availale within the Python Language installation
- **Dependency**:  When your Python code relies on external modules, you can say that these packages are dependencies of your project.
- **pyproject.toml**: It’s a configuration file standard that was defined in [PEP 518](https://peps.python.org/pep-0518/)

---
## Steps performed
1. Create a pyenv virtualenv to isolate it.  ```bash: pyenv activate poetry-test```
2. Activate the virtualenv ```bash: pyenv activate poetry-test```
3. Create a new [poetry project](https://realpython.com/dependency-management-python-poetry/#create-a-new-poetry-project)<br>
    3.1 Poetry automatically normalizes package names for you. To have more control over creating the package name, you can use the --name option to name it differently than the project folder: ```$ poetry new rp-poetry --name realpoetry```<br>
    3.2 If you prefer to store your source code in an additional src/ parent folder, then Poetry lets you stick to that convention by using the --src flag ```poetry new --src rp-poetry```
4. Use the ```pyproject.toml``` file. Documentation of it [here](https://python-poetry.org/docs/pyproject/)




---
## References:
* https://realpython.com/dependency-management-python-poetry/
