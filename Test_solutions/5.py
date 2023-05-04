import os
import re


def find_all_files(path, start_path='test'):
    files_paths = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files_paths.append(os.path.join(start_path, item))
        elif os.path.isdir(item_path):
            files_paths.extend(find_all_files(item_path, os.path.join(start_path, item)))
    return files_paths


def parse_file(path):
    emails = []
    with open(path, 'r') as file:
        for line in file.readlines():
            email = re.match(r'\s*[-\w_]+?@[-\w_]+?\.[a-z]+?\s*', line)
            if email:
                emails.append(email.string.strip())
    return emails


def task1():
    # в папке test найти все файлы filenames вывести колличество
    files = find_all_files('test')
    print(f'Найдено файлов:  {len(files)}')


def task2():
    # в папке test найти все email адреса записанные в файлы
    files = find_all_files('test')
    all_emails = []
    for file_path in files:
        emails = parse_file(file_path)
        all_emails += emails
    print('\nВсе найденные email адреса записанные в файлы в папке test:')
    for email in set(all_emails):
        print(f'\t{email}')



def main():
    task1()
    task2()
    # дополнительно: придумать механизм оптимизации 2-й задачи


if __name__ == '__main__':
    main()

    """
    Найдено файлов:  141

    Все найденные email адреса записанные в файлы в папке test:
    	random_email@dancom.org
    	random_email52111@dancom.org
    """
