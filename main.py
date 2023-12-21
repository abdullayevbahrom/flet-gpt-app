import flet as ft
import openai
import time

openai.api_key = "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"


def main_style() -> dict:
    return {
        "width": 420,
        "height": 500,
        "bgcolor": "#141518",
        "border_radius": 10,
        "padding": 15,
    }

def prompt_style() -> dict:
    return {
        "width": 420,
        "height": 45,
        "border_color": "white",
        "cursor_color": "white",
        "content_padding": 10,
    }

class MainContentArea(ft.Container):
    def __init__(self) -> None:
        super().__init__(**main_style())
        self.chat = ft.ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True,
        )

        self.content = self.chat

class Prompt(ft.TextField):
    def __init__(self) -> None:
        super().__init__(**prompt_style())

def main(page: ft.Page) -> None:
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"

    main = MainContentArea()
    prompt = Prompt()

    page.add(
        ft.Text(value="Python ChatGPT - Flet App", size=28, weight="w800"),
        main,
        ft.Divider(height=6, color="transparent"),
        prompt,
    )

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
