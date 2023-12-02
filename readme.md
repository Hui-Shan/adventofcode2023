# Advent of code 2023
## pre-commit instructions
1. Add [.flake8](.flake8) and [.pre-commit-config.yaml](.pre-commit-config.yaml) files to the root folder, updating rev values if necessary.
2. Run the following commands to set up:
```commandline
pre-commit install

# to run hooks on all existing files
pre-commit run --all-files

# to clean cache
pre-commit clean
```
