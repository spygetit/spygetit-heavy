from pywebio import *


def main_page():
    name = input.input("what's your name")
    output.put_text("hello", name)


def start():
    start_server(main_page, port=8080, debug=True)
