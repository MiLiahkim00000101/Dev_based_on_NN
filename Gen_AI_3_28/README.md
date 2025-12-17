# Gen_AI_28

Solution presented in file "main.py"

Highly reccomended to use Google colab for executing this code it was tested only there. Also requirement list is too long to load only for your virtual environment, but you can be sure it works.

# Task
1. Receive user's interests
2. Generate 3 reccomendation with justification
3. Sort and number on relevation
4. Add genre and author
5. Save as json
 	
# Solution

I used ```Qwen/Qwen3-4B-Instruct-2507``` from ```transformers``` as chat bot because it's instruct model support system prompt. In system prompt described output format so answer is JSON file which firstly parsed by ```re.search(...)``` and dump in file ```results_{answer_id}.json``` using library ```json```.

## Stages:

1. Text Generation by ```Qwen/Qwen3-4B-Instruct-2507``` -> ```generated_text```

2. Parsing of answer using ```re.search(r'\{.*\}', generated_text, re.DOTALL)```

3. If JSON format in answer found it saves in ```file resuts_{ans_id}.json``` 
    else saves raw model's output in file ```results_raw_{ans_id}.txt```
    where ```ans_id``` is number of answer

# Interface

Terminal
Launch of file ```main.py``` will ask you: "Введите ваши интересы: "
You're typing your interests and program will follow instructions from ```Solution/Stages/3``` 
If you want to end chat type ```STOP```

# Example

## Terminal experience
```
Введите ваши интересы: польза генеративного ии

✅ JSON успешно сохранен в файл 'results_0.json'
Введите ваши интересы: история академгородка

✅ JSON успешно сохранен в файл 'results_1.json'
Введите ваши интересы: Венчурный синдикат Coion

✅ JSON успешно сохранен в файл 'results_2.json'
Введите ваши интересы: STOP
```

## File status after example

### results_0.json
```{
  "recommendation_1": {
    "name": "Генеративный ИИ: что это и как он работает",
    "author": "Александр Смирнов",
    "genre": "Наука и технологии",
    "justification": "Книга объясняет основы генеративного ИИ на доступном языке, показывает его применение в реальной жизни и потенциал для будущего развития технологий.",
    "relevance": 95
  },
  "recommendation_2": {
    "name": "Искусственный интеллект: от теории к практике",
    "author": "Мария Кузнецова",
    "genre": "Наука и технологии",
    "justification": "Практическое руководство по пониманию и использованию ИИ, включая генеративные модели, для начинающих и профессионалов.",
    "relevance": 85
  },
  "recommendation_3": {
    "name": "Будущее цифрового мира: роль ИИ в обществе",
    "author": "Дмитрий Петров",
    "genre": "Философия и социология",
    "justification": "Рассматривает этические и социальные аспекты развития генеративного ИИ, что важно для понимания его влияния на человека и общество.",
    "relevance": 75
  }
}```

### results_1.json
```{
  "recommendation_1": {
    "name": "История академгородка",
    "author": "Александр Панфилов",
    "genre": "Научно-популярная литература",
    "justification": "Книга подробно рассказывает о создании и развитии Академгородка — уникального научного и образовательного центра в Сибири, что может заинтересовать тех, кто любит истории инноваций и научного прогресса.",
    "relevance": 95
  },
  "recommendation_2": {
    "name": "Сибирские научные легенды",
    "author": "Виктор Козлов",
    "genre": "История науки",
    "justification": "Книга содержит интересные факты и истории о ключевых ученых, которые работали в Академгородке, что дополняет понимание культурного и научного наследия региона.",
    "relevance": 85
  },
  "recommendation_3": {
    "name": "Развитие научной инфраструктуры в Сибири",
    "author": "Елена Морозова",
    "genre": "Образовательная литература",
    "justification": "Представляет систематический взгляд на формирование научных центров в Сибири, включая Академгородок, и подходит для тех, кто интересуется образовательными проектами.",
    "relevance": 70
  }
}```

### results_2.json is regretfully empty but after several years maybe not :)


