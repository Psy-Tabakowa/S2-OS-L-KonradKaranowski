import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


from ..base_frame_choose_params import BaseChooseParamsFrame


class ChooseFrameAlg2(BaseChooseParamsFrame):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, controller, **kwargs)

        # create variables
        self.num_of_blocks = tk.IntVar(value=50)
        self.num_of_requests = tk.IntVar(value=50)

        # create title
        self.create_title('Access to disk simulation')
        # create entries
        self.create_entries()

    def create_entries(self):
        self.container.columnconfigure((0, 1), weight=1)
        num_of_blocks_label = ttk.Label(
            self.container,
            text='Enter number of blocks: '
        )
        num_of_blocks_label.grid(row=0, column=0, sticky='ew')
        num_of_blocks_entry = tk.Entry(
            self.container,
            textvariable=self.num_of_blocks,
            width=10
        )
        num_of_blocks_entry.grid(row=1, column=0, sticky='ew')

        num_of_requests_label = ttk.Label(
            self.container,
            text='Enter number of requests:'
        )
        num_of_requests_label.grid(row=0, column=1, sticky='ew')
        num_of_requests_entry = tk.Entry(
            self.container,
            textvariable=self.num_of_requests,
            width=10
        )
        num_of_requests_entry.grid(row=1, column=1, sticky='ew')

        # blank line
        blank = ttk.Label(self.container)
        blank.grid(row=3, column=0, columnspan=2, sticky='ew', pady=40)

    def execute(self):
        if self.validate():
            self.controller.execute_access_to_disk(
                self.num_of_blocks.get(),
                self.num_of_requests.get()
            )
        else:
            tkinter.messagebox.showinfo('Error', 'Enter correct values, a == b')

    def validate(self):
        requests = self.num_of_requests.get()
        blocks = self.num_of_blocks.get()
        if type(requests) != int or requests <= 0:
            return False
        if type(blocks) != int or blocks != requests:
            return False
        return True

    def show_summary(self):
        self.controller.show_frame('summary2')