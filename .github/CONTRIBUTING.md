# Contributing to this project

## 👋 Hello!

Thanks for considering contributing to this open-source project! Both beginners 
and experts are very welcome here.

This project is purely for entertainment purposes, so do have fun and spill 
your creativity.

If you want to contribute to The Person, I advise you to take your time to read 
these Contribution Guidelines.

---

## 📝 Table of Contents

- [✨ Contributions You Can Make](#-contributions-you-can-make)
- [🚦 Opening Issues](#-opening-issues)
  - [🐛 Reporting Bugs](#-reporting-bugs)
  - [☝️ Suggesting Features](#-suggesting-features)
- [🧭 Pull Request Guidelines](#-pull-request-guidelines)
  - [⚠️ THINGS TO KEEP IN MIND](#-things-to-keep-in-mind)
- [📋 Task Issues](#-task-issues)
- [🧑‍💻 Code Guidelines](#-code-guidelines)
- [🤖 AI-Assisted Contributions](#-ai-assisted-contributions)
- [🧰 Making Your First Contribution](#-making-your-first-contribution)

---

## ✨ Contributions You Can Make

There are many ways you can contribute: Adding a feature, fixing code, 
finding and reporting bugs, improving documentation, and more!

Any addition to the project will be very much appreciated, even small ones.

---

## 🚦 Opening Issues

**We highly recommend [opening an issue][repo-issues]** before creating a 
pull request. This is to ensure all changes are discussed properly (and you 
don't waste your time creating a PR that ends up getting closed). 

This is also to prevent automatically-generated pull requests created by 
automated bot accounts that usually come with low effort and minimal engagement.

### 🐛 Reporting Bugs

To report a bug:
1. On the repository on GitHub, go to the [Issues][repo-issues] tab.
2. Select "New issue"
3. **Template selection: Choose "Bug report"**
4. Describe the issue thoroughly, using the template as a guide
   - If your issue description severely lacks information, maintainers may 
     close it.
5. Submit the issue.

### ☝️ Suggesting Features

To suggest a feature:
1. On the repository on GitHub, go to the [Issues][repo-issues] tab.
2. Select "New issue"
3. **Template selection: Choose "Feature request"**
4. Describe the feature thoroughly, using the template as a guide
    - If your issue description severely lacks information, maintainers may 
      close it.
5. Submit the issue.

...or add a comment under a [discussion][repo-disc] describing the feature.

---

## 🧭 Pull Request Guidelines

(NOTE: Read "[Opening Issues](#-opening-issues)" first if you plan on adding an 
enhancement to the project or fixing a bug)

1. Create a fork of [the repository][repo]
2. Clone the forked repository to your local machine
3. Create a new branch with a meaningful name (include the type of change 
   followed by a slash; use hierarchical branch naming)

   | Prefix       | Description                                    |
   |--------------|------------------------------------------------|
   | `bugfix`     | Bug fix (minor, not urgent)                    |
   | `hotfix`     | Urgent, critical fix                           |
   | `feature`    | New feature/functionality                      |
   | `ui`         | Affects user interface only                    |
   | `docs`       | Documentation only                             |
   | `format`     | Formatting fixes                               |
   | `refact`     | Code improvements that do not affect behaviour |
   | `wip`        | Work in progress                               |
   | `experiment` | Temporary, experimental code; playground       |
   | `mix`        | A combination of different fixes/changes       |
   | `misc`       | Other (not recommended)                        |

   - e.g.) `feature/feature-name`, `fix/issue-12`
   
4. Make and commit your changes
   - Commit messages should be in the imperative tone without a period
     - e.g.: `Add test files`, `Fix attribute assignments`, `Update 
     documentation`
5. Push commits to GitHub (if you have made changes locally on your machine)
6. Create and submit a pull request
7. Request a review from a maintainer

We will likely need to discuss the changes you make and apply some tweaks 
and polishes before approval.

You should receive a notification/email once your changes have been merged 
onto the main branch of this project.

### ⚠️ THINGS TO KEEP IN MIND
- **Rebase > Merge**: When updating a branch, **always use a rebase** and 
  resolve conflicts. This is to keep commit history nice and linear. The 
  only time you should see a merge commit is when your pull request is 
  merged into upstream `main`.
- **Avoid working directly on `main`**; always create a new branch on your fork.
- To avoid **conflicts, always** remember to update your local fork 
  (`git pull`) before working.
- If you forgot to update your fork before working, run `git pull --rebase` 
  and resolve conflicts (if any).
  - If you run into any trouble during conflict resolution, or are not sure 
    how to resolve a conflict, tag a maintainer/reviewer in an appropriate 
    issue or PR comments section, or in a [Discussion][repo-disc], for help.
- If you ever need to force-push, use `--force-with-lease` to prevent losing 
  any work.
- Minimize how much code you touch outside what you are working on; change 
  only what you are focusing on doing and avoid changing others' code.

## 📋 Task Issues

Some issues will be opened in the [Issues tab][repo-issues] on GitHub, labeled 
`task`. 

**If you are interested in completing a task**: 
1. Make sure you give the instructions in the task description a proper read
2. **Leave a comment requesting assignment under the issue**
3. Wait for a thumbs-up from a maintainer
4. Follow the steps above to create a fork and PR with your changes
5. Start coding!

**When writing the pull request**:
- Start the title the PR with `TASK: `.
- In your PR description, **ensure you use an issue-closing keyword phrase:**

```markdown
# TASK: Title of task (#123)

This is a description of the task completed. 
Blah blah blah.

Closes #123
```

Where `#123` is the issue number.

Other issue-closing keywords you can use:
* close
* closes
* closed
* fix
* fixes
* fixed
* resolve
* resolves
* resolved

### Note

Each task issue is labeled with its approximate difficulty level.

To ensure fair distribution of tasks amongst contributors, **please 
try to complete tasks labeled with your level of coding experience only** 
(everyone should have a chance to contribute)

## 🧑‍💻 Code Guidelines

Here are **3 rules** you should remember when writing code:

> `1.` Styling matters

Writing properly styled and formatted code ensures your code can be easily 
read and understood by everyone.

For Python code, follow [PEP 8][pep-8].

Key things to keep in mind include:
- **Line lengths** (try to keep line **below 80 characters**; PEP 8 says 79 but 
  whichever works)
- **Naming conventions** (module, variable, class, and function names)
  - `variable_must_be_named_like_this`
  - `functions_too`
  - `also_modules`
  - `ClassesMustBeNamedLikeThis`
- **Docstring and comments formatting**
- **Line separations** (2 blank lines around classes and functions, etc.)
- **Order of import statements** (standard → third-party → local)

Take a look at existing code on the repo to get an idea of the code style.

If you are unfamiliar with PEP 8, please [give it a quick read][pep-8].

===============================================

> `2.` Always assume the user is stupid

Special cases (almost) always exist. Make sure you take into account as many 
input possibilities as you can, even those that anyone in the right mind would 
never think of.

===============================================

> `3.` Don't be boring

Give your code some _personality_. Avoid dull, flavorless code. You can even 
add a little joke comment if your code starts to look sleep-inducing.

## 🤖 AI-Assisted Contributions

AI tools can be helpful during development, and contributors are allowed to use 
them as **assistive tools**. However, this project does **not accept fully 
automated or mass-generated contributions**.

When submitting a pull request:
- **A human must be responsible** for the work submitted.
- **You must personally review, understand, and test** any code you submit.
- AI may be used for **suggestions, debugging help, or small improvements**, 
  but not for generating entire pull requests automatically.
- **Bulk or automated PRs created by bots or scripts are not accepted**.
- Contributors must be able to **explain their changes and respond to review 
  feedback**.

Pull requests and issues that appear to be:
- fully AI-generated, 
- automatically submitted to many repositories,
- or lacking human oversight
may be **closed without merging**.

If you used AI assistance, please disclose it briefly in your PR description.

## 🧰 Making Your First Contribution

If you're new here or are not familiar with contributing to repositories on 
GitHub, here are some links with information that might help:

- https://docs.github.com/get-started/exploring-projects-on-github/contributing-to-a-project
- https://docs.github.com/get-started/exploring-projects-on-github/contributing-to-open-source
- https://github.com/firstcontributions/first-contributions

[repo]: https://github.com/TheGittyPerson/ThePerson
[repo-issues]: https://github.com/TheGittyPerson/ThePerson/issues
[repo-disc]: https://github.com/TheGittyPerson/ThePerson/discussions
[coc]: /.github/CODE_OF_CONDUCT.md
[pep-8]: https://peps.python.org/pep-0008/
