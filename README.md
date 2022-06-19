## How to run the code 🏃‍♂️
### Installation 🔧

You will need to install [Poetry](https://python-poetry.org/) to install project's dependencies

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```

Locate where Poetry is installed

```bash
whereis poetry
```

Copy and replace poetry's path to this line and added it at the end of the `.bashrc` file

```bash
export PATH="$HOME/.poetry/bin:$PATH"
```

## Installing project's dependencies 📚

Enter into project's root folder and run:

```bash
poetry install
```
It should create a `.venv` folder, generating a virtual enviroment with all project's dependencies

## How to run locally ⚙️

* Clone the repository
```bash
$ git clone https://github.com/Arkemix30/calculadora-ir-nicaragua-api.git
```

* To run the project, you need to activate the virtual environment.
For that, you can run this command:
```bash
$ poetry shell
```

* And finally, to run the server:
```bash
$ python main.py
```

## Authors ✒️

* **Enmanuel Silva** - [Arkemix](https://github.com/Arkemix30)

---
⌨️ with ❤️ by [Arkemix30](https://github.com/Arkemix) 😊
