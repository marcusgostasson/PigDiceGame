Pig (Dice game)  🐷
==========================

Pig, även känt som Gris, är ett roligt och enkelt tärningsspel som är perfekt för att spela med familj och vänner. Spelet kräver bara två tärningar och en stark aptit för risktagande! Här är en grundläggande beskrivning av hur det fungerar:

**Spelare:** Två personer mot varandra.

**Målet:** Att nå först till 100 poäng.

**Regler:**

1. Spelaren kastar de två tärningarna.
2. Om spelaren får en etta på någon av tärningarna förlorar de alla poäng som samlats in under rundan och det blir nästa spelares tur.
3. Om spelaren inte får en etta, adderas summan av de två tärningarna till deras poäng för rundan.
4. Spelaren kan välja att antingen kasta tärningarna igen för att öka sin poäng för rundan, eller stanna och lägga till poängen till sin totala poäng för spelet.
5. Om spelaren bestämmer sig för att stanna, övergår kontrollen till nästa spelare.
6. Första spelaren som når den förutbestämda poängsumman vinner spelet.

**Strategi:**

- Risken att fortsätta kasta tärningarna ökar chansen att få en etta och förlora alla poäng för rundan.
- Det är viktigt att avväga risken och belöningen när man bestämmer sig för att fortsätta eller stanna.
- En vanlig strategi är att samla poäng långsamt genom att stanna vid varje säker summa för att undvika att förlora allt i en enda tur.

Pig är ett underhållande spel som kombinerar tur med strategi och är perfekt för alla åldrar!

Lycka till ! 🎲🎲😃

[![Pipeline status](https://gitlab.com/mikael-roos/python-template/badges/main/pipeline.svg)](https://gitlab.com/mikael-roos/python-template/-/pipelines)
[![Documentation Status](https://readthedocs.org/projects/a-python-project-template-codestyle-and-linters-included/badge/?version=latest)](https://a-python-project-template-codestyle-and-linters-included.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Check python version <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a></p> 
--------------------------

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



Python virtual environment <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a></p>
--------------------------

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



Install the dependencies   💾
--------------------------

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



Run the code   🏃
--------------------------

The example program can be started like this.

```
# Execute the main program
python PigDiceGame/main.py
```

All code is stored below the directory `PigDiceGame/`.



Run the validators   🏃
--------------------------

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `PigDiceGame/`.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



Codestyle with black ⚫
--------------------------

You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

```
# Same same, different names
make black
make codestyle
```

Read more on [black](https://pypi.org/project/black/).



Run the unittests   🏃
--------------------------

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



Run parts of the testsuite   🏃
--------------------------

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
```



Remove generated files   🗑️
--------------------------

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```



More targets in the Makefile
--------------------------

The makefile contains more targets, for example these.

* `make pyreverse` to generate class and package diagrams from the code base.
* `make doc` to generate documentation from the code.


