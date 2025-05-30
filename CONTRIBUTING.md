# What this repository is

This repository contains sources of the Data Visualization in Python course.

# Contributing

We love contributions!
We are happy to see fixes of the existing bugs and tasks and tests mistakes.
The current tasks can be found in the [open issues](https://github.com/jetbrains-academy/data-visualization-course/issues) in the project.
If you have some questions or find bugs or mistakes, please do not hesitate to open new ones.

Please, add a comment to the issue, if you're starting work on it.

If you add some common functionality, e.g. for the test system, it is important to add comments to describe new behaviour.
This will help other developers and users to use them correctly.

## Submitting patches

The best way to submit a patch is to [fork the project on GitHub](https://help.github.com/articles/fork-a-repo/)
and then send us a [pull request](https://help.github.com/articles/creating-a-pull-request/)
to the `main` branch via [GitHub](https://github.com).

If you create your own fork, it might help to enable rebase by default
when you pull by executing
``` bash
git config --global pull.rebase true
```
This will avoid your local repo having too many merge commits
which will help keep your pull request simple and easy to apply.

## Set up the development environment

Besides of the regular [`requirements.txt`](./requirements.txt) file with all necessary requirements,
we also use the file with some development requirements: [`requirements-dev.txt`](requirements-dev.txt).
It contains `ruff` and other packages for the development process.

To set up the development environment, please do the following:
1. Create a new virtual environment:
   ```bash
   python3 -m venv .venv
   ```

2. Activate the virtual environment:
    * For macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```
    * For Windows:
      ```shell
      .venv\Scripts\activate.bat
      ```

3. Install the development requirements:
   ```bash
   pip3 install -r requirements-dev.txt
   ```

4. Install the regular requirements:
   ```bash
   pip3 install -r requirements.txt
   ```

## Search and fix code style issues

We use the [Ruff](https://docs.astral.sh/ruff/) tool as the main static analysis tool.
To search and fix code style issues, 
you need to run the predefined "Fix the code" configuration in PyCharm or execute the following command:
```bash
ruff check --fix; ruff format 
```

## Checklist

Before submitting the pull request, make sure that you can say "YES" to each point in this short checklist:

- You provided the link to the related issue(s) from the repository;
- You made a reasonable amount of changes related only to the provided issues;
- You can explain changes made in the pull request;
- You ran the build locally and verified new functionality/fixed bugs;
- You ran related tests locally (or add new ones) and they passed;
- You don't have code-style problems according to the [GitHub Actions](https://github.com/jetbrains-academy/data-visualization-course/tree/main/.github/workflows)
- You do not have merge conflicts in the pull request.
