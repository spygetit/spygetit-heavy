from pywebio import start_server
from pywebio.output import put_button, use_scope, put_row

from designer import main_page as designer_page
from launcher import main_page as launcher_page


def main_page():
    with use_scope("HEADER"):
        put_row([
            put_button("DESIGNER", onclick=designer_page, color="primary"),
            put_button("LAUNCHER", onclick=launcher_page, color="primary")])


def start():
    start_server(main_page, port=8080, debug=True)


if __name__ == "__main__":
    start()
