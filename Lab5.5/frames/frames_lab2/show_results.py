from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg


from frames.base_frame_results import BaseResultsFrame


class ResultFrameAlg2(BaseResultsFrame):

    def __init__(self, container, controller, queues, cylinders, names, previous, **kwargs):
        super().__init__(container, controller, **kwargs)

        # variables for times and names
        self.names = names
        self.cylinders = cylinders
        self.queues = queues

        # store prevoious params
        self.previous = previous

        # params key
        self.params = 'alg2_params'

        # create title
        self.create_title('Access to disk simulation results')

        # create dummy canvas
        self.create_canvas()

    def create_canvas(self):
        figure = Figure(figsize=(3, 3), dpi=100)
        ax1 = figure.add_subplot(221)
        ax2 = figure.add_subplot(222)
        ax3 = figure.add_subplot(223)
        ax4 = figure.add_subplot(224)
        figure.subplots_adjust(hspace=0.4)

        axes = [ax1, ax2, ax3, ax4]
        colors = ['red', 'blue', 'green', 'purple']
        x = [i + 1 for i in range(self.previous[0])]

        for ax, queue, color, name, total in zip(axes, self.queues, colors, self.names, self.cylinders):
            ax.set_title(f'{name}, total rewound: {total}')
            ax.plot(queue, x, marker='x', color=color)
            ax.set_xticks([])
            ax.set_yticks([])

        canvas = FigureCanvasTkAgg(figure=figure, master=self.container)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def execute(self):
        self.controller.execute_access_to_disk(*self.previous)
