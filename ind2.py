# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import click
import json
import os.path


def add_worker(staff, surname, name, number, date_obj):
    staff.append(
        {
            'surname': surname,
            'name': name,
            'number': number,
            'date_obj': date_obj,
        }
    )

    return staff


def display_workers(staff):
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} | {:^20} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)

        for idx, worker in enumerate(staff, 1):
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} | {:^20} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('number', ''),
                    str(worker.get('date_obj', '')),
                )
            )
        print(line)

    else:
        print("Список пуст.")


def save_workers(file_name, staff):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_workers(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


@click.command()
@click.argument('command')
@click.argument('filename')
@click.option('--surname', help='The surname')
@click.option('--name', help='The name')
@click.option('--number', help='The number')
@click.option('--date.obj',  help='The date')
def main(command, filename, surname, name, number, date_obj):
    is_dirty = False
    if os.path.exists(filename):
        workers = load_workers(filename)
    else:
        workers = []

    if command == "add":
        workers = add_worker(
            surname,
            name,
            number,
            date_obj
        )
        is_dirty = True
    elif command == "display":
        display_workers(workers)
    if is_dirty:
        save_workers(filename, workers)


if __name__ == "__main__":
    main()