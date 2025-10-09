# Gen_AI_34

Solution presented in file "task.py"

I used dataset available on link https://www.kaggle.com/datasets/jensenbaxter/10dataset-text-document-classification for solution

## Count Vectorizer
- Method for transformation text to dictionary of words and vectors of words frequences for every document for using them in learning of Natural Language Process models

## TF-IDF Vectorizer
- Method for transformation texts to matrix of words and documents where each word has its own TF-IDF metric for each document


## Structure of dataset
directory with data <br>
        |<br>
        |------ directory with documents<br>
        |------ directory with documents<br>
        |------ directory with documents<br>
        |------ directory with documents<br>
        |______ directory with documents<br>
        ...<br>

## How to use
- I used python@3.10.6
Install it on official website

First of all install requirements
- !pip install -r requirements.txt

Launching of program:
python task.py --t [TYPE OF PATH] [DIRECTORY PATH]

[TYPE OF PATH] - 'a' - absolute path, 'r' - relative path

Example:
```bash
$python task.py --t r data # creates directory data in current directory and saves dataset inside
```

if you want see output in file out.txt:
```bash
$python task.py --t r data > out.txt # creates directory data in current directory and saves dataset inside and translate standard output into out.txt
```
    
## Results

out.txt contain results

Я считаю, что метрика Tf-IDF более показательна и решает больше задач связанных с NLP. Даже без попыток ввести стоп-слова она убрала слово "the" с лидирующих позиций, чего не сделал глупый CountVectorizer. Так же TF-IDFVectorizer выделил действительно ключевые слова в топ-5. Слова связаны с программным обеспечением, компьютерами и ПО для шпионажа. В CountVectorizer можно увидеть лишь одно слово в топ-5. 

Всё это благодаря тому, что Tfidf смотрит на наличие слова во всех документах(IDF), что позволяет ей дать слову более верную оченку в рамках конкретного по сравнению с остальными. Всё познаётся в сравнении)))