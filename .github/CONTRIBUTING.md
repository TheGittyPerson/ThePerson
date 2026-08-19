# Contributing Guidelines

###### How to Contribute to _ThePerson_

## 👋 Greetings!

Thanks for considering contributing to this open-source project! Both beginners 
and experts are very welcome here.

This is meant to be a relatively casual repository, so please have fun and 
let your creativity loose.

---

## Table of Contents

- [✨ Contributions You Can Make](#contributions-you-can-make)
- [📐 Requirements](#requirements)
- [🧑‍💻 Code Guidelines](#code-guidelines)
- [📋 Tasks](#tasks)
- [🧭 Pull Request Guidelines](#pull-request-guidelines)
- [🚦 Opening Issues](#opening-issues)
  - [🐛 Reporting Bugs](#reporting-bugs)
  - [☝️ Suggesting Features](#suggesting-features)
- [🏡 TheTown](#thetown-)
- [🤖 AI-Assisted Contributions](#ai-assisted-contributions)
- [🧰 Making Your First Contribution](#making-your-first-contribution)

---

## Contributions You Can Make

There are many ways you can contribute: 
- [Completing tasks](#tasks)
- [Making your own tasks][issue #144]
- [Joining TheTown](#thetown-)
- [Suggesting or adding a feature](#suggesting-features)
- [Finding and reporting bugs](#reporting-bugs)
- Reformatting, refactoring, or enhancing code
- Improving documentation
- [Participating in discussions][discussions]
- Helping to review or give feedback to pull requests or issues
- ...and more!

Any addition to the project will be very much appreciated, even small or minor 
ones.

[🔼 TOC](#table-of-contents)

## Requirements

- **Python 3.12 or above** (recommended)
- A recognized IDE / code editor, for example:
  - Visual Studio Code (with a proper linter or code analyzer installed)
  - JetBrains IDEs (👑 **PyCharm**, IntelliJ, WebStorm, etc.)
  - Eclipse / Xcode / Zed / Cursor / ...
  - **NOT** the GitHub web editor or a basic text editor.
  - **NOT** IDLE or Vim/Neovim.

[🔼 TOC](#table-of-contents)

---

## Code Guidelines

Follow [PEP 8] as much as possible:

Key things to keep in mind include:
- **Line lengths** (try to keep lines **below 80 characters**; PEP 8 says 79 but
  both work)
- **Naming conventions** (module, variable, class, and function names)
  - `variable_must_be_named_like_this`
  - `functions_too`
  - `also_modules`
  - `ClassesMustBeNamedLikeThis`
- **Docstring and comments formatting**
- **Line separations** (2 blank lines around classes and functions, etc.)
- **Order of import statements** (standard → third-party → local)

Try to also stay consistent with existing code styles and formats already in 
the repo.

[🔼 TOC](#table-of-contents)

---

## Tasks

Some issues will be opened in the [Issues] page on GitHub, labeled `task`. 

**If you are interested in completing a task**: 
1. Make sure you give the instructions in the task description a proper read.
2. **Leave a comment requesting assignment for the issue**.
3. Wait for a thumbs-up from a maintainer.
4. Follow the steps above to create a fork and PR with your changes.
5. Code away!

You can also make your own tasks! Check out [Issue #144] for more info.

> Click [HERE][avail-tasks] to see available tasks (link filtered for pinned 
> tasks or open tasks with no assignees)

[🔼 TOC](#table-of-contents)

---

## Pull Request Guidelines

1. Create a fork of [repository].
2. Clone the forked repository to your local machine.
3. Create a new branch with a meaningful name (include the type of change 
   followed by a slash; use hierarchical branch naming).

   | Prefix           | Description                                    |
   |------------------|------------------------------------------------|
   | `bugfix`/`fix`   | Bug fix (minor, not urgent)                    |
   | `hotfix`         | Urgent, critical fix                           |
   | `feature`        | New feature/functionality                      |
   | `ui`             | Affects user interface only                    |
   | `docs`           | Documentation only                             |
   | `format`/`style` | Formatting fixes                               |
   | `refactor`       | Code improvements that do not affect behaviour |
   | `test`           | Changes to test files                          |
   | `experiment`     | Temporary, experimental code; playground       |
   | `mix`            | A combination of different fixes/changes       |
   | `misc`           | Other; miscellaneous                           |

   - e.g.) `feature/feature-name`, `fix/issue-12`
   
4. Make and commit your changes.
   - Commit messages should be in the imperative tone without a period.
     - e.g.: `Add test files`, `Fix this function`, `Update README`
5. Push commits to GitHub (if you have made changes locally on your machine).
6. Create and submit a pull request.

[🔼 TOC](#table-of-contents)

## Opening Issues

**We highly recommend [opening an issue][issues]** before creating a 
pull request. This is to ensure all ideas are discussed properly before 
implementation and to minimize AI-generated pull requests.

### Reporting Bugs

To report a bug:
1. On the repository on GitHub, go to the [Issues] tab.
2. Select "New issue".
3. **Choose "Bug report" as the template**.
4. Describe the issue thoroughly, using the template as a guide
5. Submit the issue.

### Suggesting Features

To suggest a feature:
1. On the repository on GitHub, go to the [Issues] tab.
2. Select "New issue".
3. ** Choose "Feature request" as the template**
4. Describe the feature thoroughly, using the template as a guide.
5. Submit the issue.

Or, add a comment under a [discussion][discussions] describing the feature.

[🔼 TOC](#table-of-contents)

## TheTown 🏡

In the root directory of this repo, you will see `the_town.py`. Add yourself 
as a `Person` instance to be part of TheTown!

Pull request steps:
1. Fork and clone this repository
2. **Create a new branch** using the special prefix `town`. Name the branch 
   `town/add-<yourname>`.
    - Replace `<yourname>` with your name, e.g., `town/add-morpheus`
    - This is only if you're adding your `Person` instance. Otherwise, choose a 
      descriptive branch name that describes your changes (it still has to 
      start with `town/`).
3. Commit your changes and push to your remote fork.
4. Open a pull request
5. Await approval

You can also open a PR to update, change, or remove any of the code **you** 
added previously.

[🔼 TOC](#table-of-contents)

## AI-Assisted Contributions

AI tools can be helpful during development, and contributors are allowed to use
them as **assistive tools**. However, this project does **not accept 
contributions that are noticeably and mostly AI-generated**.

Pull requests that appear to be:
- primarily AI-generated (including PR descriptions or comments),
- created by a bot/automated account,
- or lacking human oversight
will be **closed without merging**.

[🔼 TOC](#table-of-contents)

## Making Your First Contribution

If you're new here or are not familiar with contributing to repositories on 
GitHub, here are some links with information that might help:

- https://docs.github.com/get-started/exploring-projects-on-github/contributing-to-a-project
- https://docs.github.com/get-started/exploring-projects-on-github/contributing-to-open-source
- https://github.com/firstcontributions/first-contributions

[🔼 TOC](#table-of-contents)

[repository]: https://github.com/TheGittyPerson/ThePerson
[issues]: https://github.com/TheGittyPerson/ThePerson/issues
[issue #144]: https://github.com/TheGittyPerson/ThePerson/issues/144
[avail-tasks]: https://github.com/TheGittyPerson/ThePerson/issues/views/12892
[discussions]: https://github.com/TheGittyPerson/ThePerson/discussions
[pep 8]: https://peps.python.org/pep-0008/
