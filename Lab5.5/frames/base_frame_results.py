import tkinter as tk
from tkinter import ttk
import abc


class BaseResultsFrame(ttk.Frame, abc.ABC):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # key of params page
        self.params = None

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
        Create buttons to control control type of frame
        :return:
        """
        self.button_container.columnconfigure((0, 1, 2), weight=1)
        exit = ttk.Button(
            self.button_container,
            text='Exit'
        )
        exit.grid(row=4, column=0, sticky='ew')
        exit['command'] = lambda: self.controller.show_frame('main_menu')

        change_params = ttk.Button(
            self.button_container,
            text='Change parameters'
        )
        change_params.grid(row=4, column=1, sticky='ew')
        change_params['command'] = lambda: self.controller.show_frame(self.params)

        try_again = ttk.Button(
            self.button_container,
            text='Try again'
        )
        try_again.grid(row=4, column=2, sticky='ew')
        try_again['command'] = lambda: self.execute()

    @abc.abstractmethod
    def execute(self, **kwargs):
        pass

