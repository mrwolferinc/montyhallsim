# Contributing

This guide will show you how to contribute to the [montyhallsim](https://github.com/mrwolferinc/montyhallsim) GitHub repository.

## Before You Begin

Before contributing to montyhallsim, it is assumed that you know Python and Git. If not, then there are various online tutorials available to help you.

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Git Tutorial](https://help.github.com/en/github/using-git)

## Cloning montyhallsim

The first step in contributing to montyhallsim is by cloning its repository onto your local file system.

1. Install [Python](https://www.python.org/downloads/)
2. Install [Git](https://git-scm.com/downloads)
3. Fork montyhallsim
4. Start a console application of your choice
5. Change into the directory of your choice
6. Clone the forked repository

   ```bash
   $ git clone https://github.com/[yourgithubusername]/montyhallsim.git
   ```

7. Go into the montyhallsim directory

   ```bash
   $ cd montyhallsim
   ```

If you do everything correctly, then you should be able to start making changes to montyhallsim's repository from your computer.

> **Note:** If you already have Python and/or Git installed on your computer, then you can skip steps 1, 2, or both.

## Making Changes

When you decide to make changes to the repository, start with the following:

1. Update your local repo

   ```bash
   $ git pull https://github.com/mrwolferinc/montyhallsim.git
   $ git push
   ```

2. Make a new branch from the main branch

   ```bash
   $ git checkout main
   $ git branch [yourchangesbranch]
   $ git checkout [yourchangesbranch]
   ```

3. Add your changes to your commit.
4. Push the changes to your forked repository.
5. Open a Pull Request.

## Important Notes

- Do not include any build files in your commit as they will be ignored.
- Not all new features will need a new test. Smaller, simpler features could be incorporated into an existing test. Bigger, more complex features may be asked to add a test demonstrating the feature.
- If you modify existing code, run relevant tests to check if they didn't break.
- If some issue is relevant to a patch or feature, please mention it with a hash (e.g. \#2416) in a commit message to get cross-reference in GitHub.
- Once done with a patch or feature, do not add more commits to a feature branch.
- Create separate branches per patch or feature.
- If you make a pull request but it's not actually ready to be pulled into the main branch then please [convert it to a draft](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/changing-the-stage-of-a-pull-request#converting-a-pull-request-to-a-draft).

This project is currently contributed via everyone's spare time. Please keep in mind that it may take some time for the appropriate feedback to get to you. If you are unsure about adding a new feature, it might be better to ask first to see whether other people think it's a good idea.
