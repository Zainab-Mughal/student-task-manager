# Lab Report - Student Task Manager
**Name:** Zainab Mughal | **Roll No:** FA23-BSE-196 | **Course:** CSC418 DevOps for Cloud Computing

## 1. Git vs GitHub; add, commit and push
Git is a version control system that runs on my computer and records the history of changes to files.
GitHub is an online service that hosts Git repositories and adds collaboration tools such as Issues,
Pull Requests and Actions. `git add` stages changes, `git commit` saves the staged changes as a snapshot
in local history, and `git push` uploads local commits to GitHub.

## 2. Branches, Pull Requests and merge conflicts
Branches let each feature be developed separately without breaking main. Pull Requests let changes be
reviewed and tested before they are merged. A merge conflict happens when two branches change the same
lines of a file differently and Git cannot decide which version to keep.

## 3. fetch vs pull; merge vs rebase
`git fetch` downloads new commits from GitHub without changing my local branch; `git pull` fetches and then
merges them. `git merge` joins two histories and keeps them with a merge commit; `git rebase` replays my
commits on top of another branch to make a straight history, but it rewrites commit IDs.

## 4. How Issues and Actions help a team
Issues record features, bugs and documentation tasks with labels, so work is organised and linked to the
Pull Requests that close it. GitHub Actions runs the tests automatically on every push and Pull Request,
so broken code is caught before it reaches main.

## 5. Difficulty faced and solution
My first push was rejected with "Permission denied" because Windows had saved the login of a different
GitHub account. I removed it with `cmdkey /delete:git:https://github.com` and signed in again with my own
account. I also forgot to commit a change before switching branches, so it was committed on the wrong
branch; I undid it with `git reset HEAD~1`, committed it on the correct branch and force-pushed the
feature branch to remove the wrong commit.
