import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


from ..base_frame_choose_params import BaseChooseParamsFrame


class ChooseFrameAlg1(BaseChooseParamsFrame):

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, controller, **kwargs)

        # create variables
        self.num_of_processes = tk.IntVar(value=15)
        self.phase_len_down = tk.IntVar(value=3)
        self.phase_len_up = tk.IntVar(value=10)

        # create title
        self.create_title('Access to processor simulation')
        # create entries
        self.create_entries()

    def create_entries(self):
        num_processes_label = ttk.Label(
            self.container,
            text='Enter number of processes: '
        )
        num_processes_label.grid(row=1, column=0)
        num_processes_entry = tk.Entry(
            self.container,
            textvariable=self.num_of_processes,
            width=10
        )
        num_processes_entry.grid(row=2, column=0)

        phase_len_down_label = ttk.Label(
            self.container,
            text='Enter minimal length of process:'
        )
        phase_len_down_label.grid(row=1, column=1)
        phase_len_down_entry = tk.Entry(
            self.container,
            textvariable=self.phase_len_down,
            width=10
        )
        phase_len_down_entry.grid(row=2, column=1)

        phase_len_up_label = ttk.Label(
            self.container,
            text='Enter max length of process: '
        )
        phase_len_up_label.grid(row=1, column=2)
        phase_len_up_entry = tk.Entry(
            self.container,
            textvariable=self.phase_len_up,
            width=10
        )
        phase_len_up_entry.grid(row=2, column=2)

        # blank line
        blank = ttk.Label(self.container)
        blank.grid(row=3, column=0, columnspan=3, sticky='ew', pady=40)

    def execute(self):
        if self.validate():
            self.controller.execute_access_to_processor(
                self.num_of_processes.get(),
                self.phase_len_down.get(),
                self.phase_len_up.get()
            )
        else:
            tkinter.messagebox.showinfo('Error', 'Enter correct values')

    def validate(self):
        processes = self.num_of_processes.get()
        phase_down = self.phase_len_down.get()
        phase_up = self.phase_len_up.get()
        if type(processes) != int or processes <= 0:
            return False
        if type(phase_down) != int or phase_down <= 0:
            return False
        if type(phase_up) != int or phase_up < phase_down:
            return False
        return True

    def show_summary(self):
        self.controller.show_frame('summary1')
