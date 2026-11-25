# Mission 06 — Git and GitHub

## Objective
Understand version control and learn how Git and GitHub help developers manage and collaborate on projects.

## Work Completed
Studied Git commands, repository management, commits, branches, pushing changes, and Pull Requests.

## Commands/Tools Used

| Command | Purpose |
|---|---|
| `git status` | Checks the working tree |
| `git add .` | Stages changes |
| `git commit -m "message"` | Saves changes as a commit |
| `git log --oneline` | Displays commit history |
| `git branch` | Lists branches |
| `git switch -c update-about` | Creates and switches to a branch |
| `git push` | Uploads commits to GitHub |
| `git pull` | Downloads and integrates remote changes |

## What I Learned

### 1. Git vs GitHub

- **Git:** A version control system that tracks changes in files.
- **GitHub:** An online platform for hosting Git repositories and collaborating with others.

### 2. Basic Git Workflow

The basic workflow is:

1. Edit files.
2. Stage changes using `git add`.
3. Save changes using `git commit`.
4. Upload changes using `git push`.

### 3. Branches

A branch allows developers to work on changes separately without directly modifying the main branch.

Example:
`git switch -c update-about`

This creates a new branch called `update-about` and switches to it.

### 4. Pull Requests

A Pull Request allows developers to propose changes from one branch to another for review before merging.

## Difficulties
Understanding the difference between Git and GitHub and how branches work.

## How I Resolved Them
Learned that Git manages version history locally, while GitHub hosts repositories online. Studied how branches and Pull Requests support collaboration.

## Evidence/Files
- GitHub repository and commit history.
- `update-about` branch and its merged Pull Request.

## Commit Details
This mission documentation was included in commit 2c7a113 on the main branch. Additional updates were included in commit 2c3bdfe on update-about and merged into main.
