# betag

Label data easily!

## Installation
```
pip install betag
```

## Usage
### Single choice data set labelling
```
usage: betag choice [-h] --source SOURCE --target TARGET --labels LABELS path

positional arguments:
  path             Path to the *csv file to label

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  Name of the column or columns (comma separated) to be labelled
  --target TARGET  Name of the column to store labels to
  --labels LABELS  Comma separated labels
```

## Running locally
```bash
poetry run betag
```

## Development setup

### Install pre-commits
```bash
pre-commit install
```