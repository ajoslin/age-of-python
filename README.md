age-of-python:develop
=====================

### How to run the current version

* Right now, there is no main file. There are only test cases.
* To test, you'll need to download py.test with `pip install pytest` 
* Then run `py.test -v` in the `src` directory.  Add lots of your own test cases for your own functionality and make sure the tests work!
* View logs for your tests in the `logs` folder.

### Development Instructions 

This is the develop branch.

If you want to work on a new feature, first switch to the develop branch: `git checkout develop`. Then create a new branch for your feature: `git checkout -b my-new-feature`. Checking out a new branch while on the develop branch will create your new branch as a child of `develop`.

Or if a branch for something exists and you want to switch to it: `git checkout existing-branch`

To push a branch you're on, do: `git push origin my-branch`

To pull changes from a branch, do: `git fetch origin the-branch-name`, then `git merge origin/the-branch-name`.

Send me a pull request if you have cool changes you pushed.