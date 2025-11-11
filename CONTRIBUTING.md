# What this repository is

This repository contains the source materials for the Data Visualization with Python course.

# Contributing

We love contributions!
We're happy to see fixes for existing bugs, improvements to tasks, and corrections of test mistakes.
The current tasks can be found in the [open issues](https://github.com/jetbrains-academy/data-visualization-course/issues) of the project.
If you find bugs, mistakes, or have questions, please do not hesitate to open a new issue.

Before starting work on an issue, please add a comment.

If you add any new functionality — such as for the test system — be sure to include comments explaining the new behavior.
This will help other developers and users understand and use it correctly.

## Submitting patches

The best way to submit a patch is to [fork the project on GitHub](https://help.github.com/articles/fork-a-repo/)
and then send us a [pull request](https://help.github.com/articles/creating-a-pull-request/)
to the `main` branch via [GitHub](https://github.com).

If you create your own fork, we recommend setting up Git to enable rebase by default when you pull.
You can do this by running:
``` bash
git config --global pull.rebase true
```
This will reduce the number of merge commits in your local repository,
helping to keep your pull request clean and easy to review.

## Set up the development environment

In addition to the regular [`requirements.txt`](./requirements.txt) file, which lists all necessary dependencies,
we also provide a file with some development requirements: [`requirements-dev.txt`](requirements-dev.txt).
It includes tools such as `ruff` and other packages for the development process.

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
To search for and fix code style issues,
you can either run the predefined "Fix the code" configuration in PyCharm or execute the following command manually:
```bash
ruff check --fix; ruff format 
```

## Checklist

Before submitting your pull request, ensure you can confirm "YES" to each of the following points:

- You have provided a link to the related issue(s) from the repository.
- You made a reasonable number of changes related only to the provided issues.
- You can explain the changes made in your pull request.
- You ran the build locally and verified the new functionality or fixes.
- You ran related tests locally (or added new ones), and they passed.
- Your code has no style issues, as verified by [GitHub Actions](https://github.com/jetbrains-academy/data-visualization-course/tree/main/.github/workflows)
- Your pull request does not contain any merge conflicts.
