import tkinter as tk
from typing import Dict, List, Tuple


from scrollable_frame import ScrollableFrame


def draw_all(histories: List[Dict[str, int]], deficiencies: List[Tuple[str, int]],
             names: List[str], frame: tk.Frame):
    """
    Draw all history
    :param histories: list of histories
    :param deficiencies:  list of rewounds
    :param names: names of algorithms
    :param frame: main frame
    :return:
    """
    for history, deficience, name in zip(histories, deficiencies, names):
        label = tk.Label(frame, text=name)
        label.pack(pady=(5, 5), expand=True, fill='x', side='top')
        new_frame = tk.Frame(frame)
        new_frame.pack(pady=(10, 10), expand=True, fill='x', side='top')
        draw_(history, deficience, new_frame)


def draw_(history: Dict[str, int], deficience: Tuple[str, int], frame: tk.Frame):
    """
    Draw one frame
    :param history: list of histories
    :param deficience:  list of rewounds
    :param frame: frame to put in
    :return:
    """
    # drawing label for counting
    for i in range(len(history['frame1'])):
        label = tk.Label(
            frame,
            text=str(i + 1),
            bg='gray',
            borderwidth=2,
            relief='raised',
            height=2,
            width=5
        )
        label.grid(row=0, column=i + 1)
    for i, (key, d_frame) in enumerate(zip(history.keys(), deficience), 1):
        # frame label
        frame_label = tk.Label(
            frame,
            bg='gray',
            borderwidth=2,
            relief='raised',
            text=key,
            height=2,
            width=8
        )
        frame_label.grid(row=i, column=0)
        for j, ref_value in enumerate(history[key], 1):
            color = 'lightblue'
            for dfc in deficience:
                if dfc[0] == key and dfc[1] == j - 1:
                    color = 'orange'
            if ref_value == 0:
                text = None
            else:
                text = ref_value
            label = tk.Label(
                frame,
                text=text,
                bg=color,
                borderwidth=2,
                relief='raised',
                height=2,
                width=5
            )
            label.grid(row=i, column=j)
    # final label
    label = tk.Label(
        frame,
        text=str(f'Rewound: {len(deficience)}'),
        borderwidth=2,
        relief='raised',
        height=2,
        width=10
    )


def get_windows(width: int, history: List[Dict[str, int]], deficiencies: List[Tuple[str, int]], names: List[str]) -> tk.Tk:
    """
    Create tkinter window
    :param width: length of processes
    :param history: list of histories
    :param deficiencies: list of rewounds
    :param names: names of algorithms
    :return:
    """
    # creating root
    root = tk.Tk()
    wd = str(width * 50)
    root.geometry(f'{wd}x500')
    # main frame of app
    main_frame = ScrollableFrame(root)
    main_frame.pack(expand=True, fill='both')
    # drawing all history in canvas
    draw_all(history, deficiencies, names, main_frame.frame)
    return root
