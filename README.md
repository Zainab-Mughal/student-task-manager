# Student Task Manager

A Python console application for managing student tasks, developed to practise
a complete Git and GitHub workflow (CSC418 - DevOps for Cloud Computing).

Project status: In Progress (Testing phase started)

## Features
- Add tasks (empty titles are rejected)
- Display all tasks with their status
- Mark a task as completed using its ID
- Delete a task using a valid ID
- Automated unit tests with GitHub Actions CI

## Setup
```
git clone https://github.com/Zainab-Mughal/student-task-manager.git
cd student-task-manager
```
Requires Python 3.10 or later. No external packages are needed.

## Usage
```
python main.py
```
Choose an option from the menu (1-5).

## Running Tests
```
python -m unittest discover -s tests -v
```

## Project Structure
```
task_manager.py      Core logic
main.py              Console interface
tests/               Unit tests
docs/user-guide.md   User guide
.github/workflows/   CI workflow
```

## Author
Zainab Mughal (FA23-BSE-196)

## License
MIT
