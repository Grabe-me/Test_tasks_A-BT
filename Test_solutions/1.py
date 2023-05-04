import os


def black_book(page: int):
    status_code = os.system(f"./black-book -n {page}")
    return True if status_code == 0 else False


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.

    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.

    Уточнение:
        black_box возвращает True, если страница есть в книге
                  возвращает False, если страницы нет в книге.


    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    min_pages = 0
    max_pages = 10_000_000
    while True:
        if min_pages > max_pages:
            min_pages, max_pages = max_pages, min_pages
        diff = max_pages - min_pages
        if diff == 1:
            print(min_pages)
            break
        mid = (max_pages + min_pages) // 2
        if black_book(mid):
            min_pages = mid + 1
        else:
            max_pages = mid - 1


if __name__ == '__main__':
    # тут явно нужен алгоритм
    main()

    "7922400"
