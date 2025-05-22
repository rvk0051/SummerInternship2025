# 1. Git scans the .gitignore file(s) in your project when you run commands like git status, git add, or git commit.

# 2. Git uses pattern matching (wildcards like *, **, /) to check if a file or folder path matches any rule in .gitignore.

# 3. If a file matches a pattern and is not already tracked, Git excludes it from its list of tracked files. That means:

#   i. It doesn’t show up in git status as untracked.

#   ii. git add . skips it.

#   iii. It won’t be committed.

