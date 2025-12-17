from transformers import pipeline
from torch import torch
import json
import re

model="Qwen/Qwen3-4B-Instruct-2507"

def import_model(model_name: str):
    """Возвращает pipeline"""
    pipe = pipeline("text-generation", model=model_name)
    return pipe

def generate_answer(prompt, pipe):
    messages = [
        {"role": "system", "content": '''Ты умный ассистент, помогающий составлять рекомендации по чтению.
                Твоя задача принять список рекомендаций и вернуть его в формате JSON:
                {
                    "recommendation_1": {
                        "name": "Преступление и наказание",
                        "author": "Федор Достоевский",
                        "genre": "Роман",
                        "justification": "Здесь то, почему эта книга заинтересует пользователя",
                        "relevance": 100
                    },
                    "recommendation_2": {
                        "name": "Название книги",
                        "author": "Автор книги",
                        "genre": "Жанр книги",
                        "justification": "Обоснование рекомендации",
                        "relevance": 80
                    },
                    "recommendation_3": {
                        "name": "Название книги",
                        "author": "Автор книги",
                        "genre": "Жанр книги",
                        "justification": "Обоснование рекомендации",
                        "relevance": 60
                    }
                }
                Твоя задача вернуть только JSON'''
        },
        {"role": "user", "content": prompt},
    ]


    generated_text = pipe(messages, max_new_tokens=1000)[0]["generated_text"][2]["content"]

    return generated_text

def save_json(generated_text, ans_id):
    # Ищем JSON в выводе
    json_pattern = r'\{.*\}'
    matches = re.search(json_pattern, generated_text, re.DOTALL)

    if matches:
        json_str = matches.group()
        #   print("Извлеченный JSON:")
        #   print(json_str)
        
        # Парсим JSON
        data = json.loads(json_str)
        
        # Сохраняем в файл
        with open(f'results_{ans_id}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ JSON успешно сохранен в файл 'results_{ans_id}.json'")
        #   print("\nСодержимое файла:")
        #   print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print("❌ JSON не найден в выводе модели")
        # Сохраняем сырой текст для отладки
        with open(f'results_raw_{ans_id}.txt', 'w', encoding='utf-8') as f:
            f.write(generated_text)
        print(f"Сырой вывод сохранен в 'results_raw_{ans_id}.txt'")
    
  


def main():
    model="Qwen/Qwen3-4B-Instruct-2507"

    ans_id = 0

    pipe = import_model(model)

    while (prompt := str(input("Введите ваши интересы: "))) != "STOP":

        generated_text = generate_answer(prompt, pipe)

        save_json(generated_text, ans_id)

        ans_id += 1


    del pipe
    torch.cuda.empty_cache()

if __name__ == "__main__":
    main()