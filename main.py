import flet as ft
from openai import OpenAI
import time

client = OpenAI(api_key="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")

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
        "content_padding": 10,
        "cursor_color": "white",
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

class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str) -> None:
        self.name: str = name
        self.message: str = message
        self.text = ft.Text(self.message)
        super().__init__(spacing=4)
        self.controls=[ft.Text(self.name, opacity=0.6), self.text]

class Prompt(ft.TextField):
    def __init__(self, chat: ft.ListView) -> None:
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        self.chat: ft.ListView = chat
    
    def animate_text_output(self, name:str, prompt: str):
        word_list: list = []
        msg = CreateMessage(name, prompt)
        self.chat.controls.append(msg)
        
        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)
    
    def user_output(self, prompt):
        self.animate_text_output(name="Me", prompt=prompt)
    
    def gpt_output(self, prompt):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": prompt}]
        )
        response = response.choices[0].message.content.strip()
        self.animate_text_output(name="ChatGPT", prompt=response)
        
    
    def run_prompt(self, event):
        text = event.control.value
        self.value = ""
        self.update()        
        
        self.user_output(prompt=text)
        self.gpt_output(prompt=text)
        
        

def main(page: ft.Page) -> None:
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"

    main = MainContentArea()
    prompt = Prompt(chat=main.chat)

    page.add(
        ft.Text(value="Python ChatGPT - Flet App", size=28, weight="w800"),
        main,
        ft.Divider(height=6, color="transparent"),
        prompt,
    )

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
