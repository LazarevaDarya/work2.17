# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import argparse
import json
import os.path
import sys
from datetime import date


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


def main(command_line=None):
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="The data file name"
    )

    parser = argparse.ArgumentParser("workers")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new worker"
    )
    add.add_argument(
        "-s",
        "--surname",
        action="store",
        required=True,
        help="The worker`s surname"
    )
    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        help="The worker`s name"
    )
    add.add_argument(
        "-z",
        "--number",
        action="store",
        required=True,
        help="The year of zodiac"
    )
    add.add_argument(
        "-d",
        "--date_obj",
        action="store",
        required=True,
        help="The year of date_obj"
    )

    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all workers"
    )

    args = parser.parse_args(command_line)

    is_dirty = False
    if os.path.exists(args.filename):
        workers = load_workers(args.filename)
    else:
        workers = []

    if args.command == "add":
        add_worker(
            workers,
            args.surname,
            args.name,
            args.number,
            args.date_obj
        )
        is_dirty = True

    elif args.command == "display":
        display_workers(workers)

    if is_dirty:
        save_workers(args.filename, workers)


if __name__ == "__main__":
    main()

