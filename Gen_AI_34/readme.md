# Gen_AI_34

Solution presented in file "task.py"

I used dataset available on link https://www.kaggle.com/datasets/jensenbaxter/10dataset-text-document-classification for solution

# Count Vectorizer
- Method for transformation text to dictionary of words and vectors of words frequences for every document for using them in learning of Natural Language Process models

# Structure of dataset
directory with data
        |
        |------ directory with documents
        |------ directory with documents
        |------ directory with documents
        |------ directory with documents
        |______ directory with documents
        ...

# How to use
- I used python@3.10.6
Install it on official website

First of all install requirements
- !pip install -r requirements

Launching of program:
python task.py --a [TYPE OF PATH] [DIRECTORY PATH]

[TYPE OF PATH] - 'a' - absolute path, 'r' - relative path

Example:
```bash
$python task.py --a r data # creates directory data in current directory and saves dataset inside
```
    