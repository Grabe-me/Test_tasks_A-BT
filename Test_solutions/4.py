import json
import re
import sys


"""
        Для корректного запуска скрипта из консоли
    необходимо указать путь к JSON файлу в качестве аргумента.
    
    Например:
              python3 ./4.py test.json
"""


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    # questions = data['game']['rounds'][0]['questions']
    questions = parse_data(data, 'question')
    print(f'\nКоличество вопросов: {len(questions)}')


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    answers = parse_data(data, 'correct_answer')
    print('\nВсе правильные ответы:')
    for answer in answers:
        print(f'\t{answer}')


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    answers_time = parse_data(data, 'time_to_answer')
    print(f'\nМаксимальное время ответа: {max(answers_time)}')


def get_filename(argv_list):
    if len(argv_list) < 2:
        print('ERROR: missing 1 argument (filename)')
    elif re.match(r'.*\.json', f := str(argv_list[1])):
        return f
    else:
        print(f'ERROR: wrong filetype. Only JSON files are allowed')
    return False


def get_data(filename: str):
    with open(filename, 'r') as file:
        json_data = file.read()
        data_dict = json.loads(json_data)
    return data_dict


def parse_data(data: dict, request: str):
    requests = []
    if type(data) == dict:
        for key, value in data.items():
            if key == request:
                requests.append(value)
            if type(value) == dict or type(value) == list:
                requests += parse_data(value, request)
    elif type(data) == list:
        for item in data:
            if type(item) == dict or type(item) == list:
                requests += parse_data(item, request)
    return requests



def main(args):
    if f := get_filename(args):
        data = get_data(f)  # загрузить данные из test.json файла
        count_questions(data)
        print_right_answers(data)
        print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    main(sys.argv)

    """
    Количество вопросов: 5
    
    Все правильные ответы:
            answr
            answr
            qqqqq
            2
            [0, 1]
    
    Максимальное время ответа: 129
    """
