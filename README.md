Pig (Dice game)  🐷
==========================

Pig, is a fun and simple dice game perfect for playing with family and friends. The game requires only two dice and a strong appetite for risk-taking! Here is a basic description of how it works:

**Player:** Two people against each other.

**The goal:** To reach 100 points first.

**Rules:**

1. The player rolls the two dice.
2. If the player rolls a one on any of the dice, they lose all points collected during the round and it is the next player's turn.
3. If the player does not roll a one, the sum of the two dice is added to their score for the round.
4. The player can choose to either roll the dice again to increase their score for the round, or stay and add the score to their total score for the game.
5. If the player decides to stay, control passes to the next player.
6. First player to reach 100 points wins the game.

**Strategy:**

- The risk of continuing to roll the dice increases the chance of getting a one and losing all points for the round.
- It is important to weigh the risk and reward when deciding to continue or stay.
- A common strategy is to accumulate points slowly by stopping at each safe sum to avoid losing everything in a single turn.

Good luck, let´s go! 🎲🎲😃

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

# Activate on Linux / Mac
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


