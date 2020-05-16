import tkinter as tk
from tkinter import ttk
import abc


class BaseChooseParamsFrame(ttk.Frame, abc.ABC):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # container for title
        self.title_container = tk.Frame(self, bd=10, relief='groove')
        self.title_container.pack(side='top', fill='x', expand=True)
        # container for entries
        self.container = tk.Frame(self, bd=10, relief='groove')
        self.container.pack(side='top', fill='both', expand=True)
        # container for buttons
        self.button_container = tk.Frame(self, bd=10, relief='groove')
        self.button_container.pack(side='top', fill='x', expand=True)
        self.create_buttons()

    def create_title(self, text):
        """
        Create title for page
        :param text: text to show
        :return:
        """
        title = ttk.Label(
            self.title_container,
            text=text,
            font=40
        )
        title.config(anchor='center')
        title.pack(side='top', fill='both', expand=True)

    def create_buttons(self) -> None:
        """
        Create buttons to control ChooseParams' type of frame
        :return:
        """
        self.button_container.columnconfigure((0, 1, 2), weight=1)
        go_back_button = ttk.Button(
            self.button_container,
            text='Back'
        )
        go_back_button.grid(row=4, column=0, sticky='ew')
        go_back_button['command'] = lambda: self.controller.show_frame('main_menu')

        summarize_button = ttk.Button(
            self.button_container,
            text='Show summary'
        )
        summarize_button.grid(row=4, column=1, sticky='ew')
        summarize_button['command'] = lambda: self.show_summary()

        run_button = ttk.Button(
            self.button_container,
            text='Run'
        )
        run_button.grid(row=4, column=2, sticky='ew')
        run_button['command'] = lambda: self.execute()

    @abc.abstractmethod
    def create_entries(self):
        pass

    @abc.abstractmethod
    def show_summary(self):
        pass

    @abc.abstractmethod
    def validate(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass
