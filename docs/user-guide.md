# User Guide - Student Task Manager

## Starting the application
Run `python main.py` from the project folder. A menu with five options appears.

## Menu options
1. **Add task** - Enter a title. Blank titles are rejected with an error message.
2. **Display tasks** - Lists every task as `[ID] Title - Pending/Done`.
3. **Complete task** - Enter the task ID. Invalid or already-completed IDs show an error.
4. **Delete task** - Enter the task ID. The task is removed if the ID exists.
5. **Exit** - Closes the application.

## Example session
    Choose an option: 1
    Enter task title: Prepare viva
    Task added: [1] Prepare viva - Pending

## Notes
Tasks are stored in memory only and are cleared when the program exits.
