import pathlib

from advent_of_code_template.definitions import TASKS_DIR
from advent_of_code_template.definitions import CURRENT_YEAR
import os
from markdown import markdown
import webbrowser
import importlib.util
from typing import List
import argparse
import aocd


def parse_args(arguments: List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", "-t", default="0", type=int, help="Which task to display. Default = 0 for all tasks.")
    parser.add_argument("--display", "-d", action='store_true',
                        help="Should the task be displayed in a web browser?")
    parser.add_argument("--visualize", "-vis", action='store_true',
                        help="Should the result be visualized (if supported by task)")
    return parser.parse_args(arguments)


def input_file_exists(task_number: int) -> bool:
    return os.path.exists(os.path.join(TASKS_DIR, 'task%02d/input.txt' % task_number))


def markdown_file_exists(task_number: int) -> bool:
    return os.path.exists(os.path.join(TASKS_DIR, 'task%02d/task.md' % task_number))


def task_exists(task_number: int) -> bool:
    return importlib.util.find_spec('tasks.task%02d' % task_number) is not None


def highest_task_implemented() -> int:
    i = 1
    while task_exists(i):
        i += 1
    return i - 1


def download_input_data(task_number: int) -> List[str]:
    if aocd.cookies.get_working_tokens():
        aocd.cookies.scrape_session_tokens()
    else:
        if not os.environ.get('AOC_SESSION'):
            cookie_file = pathlib.Path('~/.config/aocd/token').expanduser()
            if os.path.exists(cookie_file):
                print('Retrieving session ID from: ', cookie_file)
                with open(cookie_file, 'r') as f:
                    os.environ['AOC_SESSION'] = f.readline().strip()
            else:
                os.environ['AOC_SESSION'] = input('Please provide session ID in order to download the AOC data:')
                print('Saving cookie to: ', cookie_file)
                with open(cookie_file, 'w') as f:
                    f.write(os.environ['AOC_SESSION'])
        print('Downloading input-data for current task.')
    return aocd.get_data(day=task_number, year=CURRENT_YEAR).split('\n')


def get_input_data(task_number: int) -> List[str]:
    file_name = os.path.join(TASKS_DIR, 'task%02d/input.txt' % task_number)
    if not input_file_exists(task_number):
        task_input = download_input_data(task_number)
        with open(file_name, 'w') as f:
            for line in task_input:
                f.write(line)
                f.write('\n')
        return task_input
    else:
        with open(file_name, 'r') as f:
            return f.readlines()


def render_markdown_file(task_number: int):
    file_name = os.path.join(TASKS_DIR, 'task%02d/task.md' % task_number)
    if not markdown_file_exists(task_number):
        raise Exception('file %s not found.' % file_name)
    else:
        html_file_path = os.path.join(TASKS_DIR, 'task%02d/task.html' % task_number)
        if os.path.exists(html_file_path):
            os.remove(html_file_path)
        with open(file_name, 'r') as in_f:
            markdown_file_contents = in_f.read()
        markdown_html = markdown(markdown_file_contents)
        with open(html_file_path, 'w') as out_f:
            url = 'file://' + out_f.name
            out_f.write(markdown_html)
            out_f.close()
        webbrowser.open(url)
