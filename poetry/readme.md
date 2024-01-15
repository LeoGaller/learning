# January 7, 2024
# This is my test to package management with poetry
## I'm @LeoGaller
---
## Glossary
- **Modules**: If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules.
- **built-in modules**: Modules that are availale within the Python Language installation
- **Dependency**:  When your Python code relies on external modules, you can say that these packages are dependencies of your project.
- **pyproject.toml**: It’s a configuration file standard that was defined in [PEP 518](https://peps.python.org/pep-0518/)
- **[tool.poetry.dependencies] vs [tool.poetry.dev-dependencies]**: Differentiating between project dependencies and development dependencies prevents installing requirements that a user doesn’t need to run the program. The development dependencies are only relevant for other developers of your package who want to run tests with pytest and make sure the code is properly formatted with black. When users install your package, they only install requests with it.

---
## Steps performed
1. Create a pyenv virtualenv to isolate it.  ```bash: pyenv activate poetry-test```
2. Activate the virtualenv ```bash: pyenv activate poetry-test```
3. Create a new [poetry project](https://realpython.com/dependency-management-python-poetry/#create-a-new-poetry-project)<br>
    3.1 Poetry automatically normalizes package names for you. To have more control over creating the package name, you can use the --name option to name it differently than the project folder: ```$ poetry new rp-poetry --name realpoetry```<br>
    3.2 If you prefer to store your source code in an additional src/ parent folder, then Poetry lets you stick to that convention by using the --src flag ```poetry new --src rp-poetry```
4. Use the ```pyproject.toml``` file. Documentation of it [here](https://python-poetry.org/docs/pyproject/)
5. Working with Python Poetry using a virtual env.<br>
5.1. Checking if there are no Virtual environments already configured to a project ```poetry env list```<br>
5.2. ```poetry env use python3``` With this command, you’re using the same Python version that you used to install Poetry. `As you can see, Poetry constructed a unique name for your project’s environment. The name contains the project name and the Python version. The seemingly random string in the middle is a hash of your parent directory. With this unique string in the middle, Poetry can handle multiple projects with the same name and the same Python version on your system. That’s important because, by default, Poetry creates all your virtual environments in the same folder`
6. Declare the dependencies
7. Install dependencies using Poetry
    - ```poetry add pandas```
    - ```poetry add requests```
    - Specifying that a dependency is a development dependency. ```poetry add black -D``` **The --dev option is deprecated, use the** `--group dev` **notation instead**


---
## References:
* https://realpython.com/dependency-management-python-poetry/
