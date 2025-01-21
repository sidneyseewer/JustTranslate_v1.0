import kivy
from enum import Enum
kivy.require('2.1.0') # replace with your current kivy version !

from functions import *
from top_bars import TopBarMenu, TopBarSubMenu

from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

languages = [
    ('de', 'Deutsch'),
    ('fr', 'Français'),
    ('es', 'Espanol'),
    ('ru', 'Russki')
    ]
app_name = "JustTranslate"
class MainPage(Screen):
    """The main screen with clickable buttons."""
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Top bar with app name, settings, and help
        top_bar = TopBarMenu(app_name)
        layout.add_widget(top_bar)

        # Main content with four buttons
        button_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        for i in range(len(languages)):
            button = Button(text=languages[i][1], size_hint=(1, 1/len(languages)))
            button.bind(on_press=lambda x, idx=i: self.go_to_subpage(idx))
            button_layout.add_widget(button)
        
        layout.add_widget(button_layout)
        self.add_widget(layout)

    def go_to_subpage(self, idx):
        language_code = languages[idx][0]
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = language_code

class LanguagePage(Screen):
    """A sub-page that allows input like a messaging app."""
    def __init__(self, language_index, **kwargs):
        super(LanguagePage, self).__init__(**kwargs)
        self.translator = Translator(language=languages[language_index][0])

        layout = BoxLayout(orientation='vertical')

        # Top bar with back button, title, and settings
        top_bar = TopBarSubMenu(languages[language_index][1])
        top_bar.back_button.bind(on_press=self.go_back)
        layout.add_widget(top_bar)

        # Scrollable text input area (like a chat view)
        scroll_view = ScrollView(size_hint=(1, None), size=(self.width, 400))
        self.chat_log = BoxLayout(orientation='vertical')
        self.chat_log.bind(minimum_height=self.chat_log.setter('height'))
        scroll_view.add_widget(self.chat_log)
        layout.add_widget(scroll_view)

        # Input box at the bottom
        self.text_input = TextInput(hint_text="...", size_hint_y=None, height=50, multiline=False)
        self.text_input.bind(on_text_validate=self.send_message)
        layout.add_widget(self.text_input)

        self.translator.bind(on_translation_complete=self.on_translation_complete)
        
        self.add_widget(layout)

    def go_back(self, _sender_instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main_page'

    def send_message(self, _sender_instance):
        message = self.text_input.text
        if message:
            # Add the message to the chat log
            self.chat_log.add_widget(Label(text=message, height=40))
            translated_text = self.translator.translate(message)
            self.chat_log.add_widget(Label(text=translated_text, height=40))
            self.translator.speak(translated_text)
            # Clear input
            self.text_input.text = ''

    def on_translation_complete(self, _instance, translated_text):
        """Called when translation is complete."""
        # Add the translated message to the chat log
        label = Label(text=translated_text, height=40)
        self.chat_log.add_widget(label)

        # Create a "§" button to speak the translated message
        replay_button = Button(text="§", size_hint_x=None, width=50)
        replay_button.bind(on_press=lambda x: self.translator.speak(translated_text))
        self.chat_log.add_widget(replay_button)

class MyApp(App):
    def build(self):
        # Setup screen manager
        sm = ScreenManager()
        # Add main page
        sm.add_widget(MainPage(name="main_page"))
        # Add sub-pages
        for i in range(len(languages)):
            language_code = languages[i][0]
            sm.add_widget(LanguagePage(language_index=i, name=language_code))
        return sm

if __name__ == '__main__':
    MyApp().run()