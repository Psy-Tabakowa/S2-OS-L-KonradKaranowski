from execution_manager import ExecutionManager
from config import Config
from methods import EqualAllocationMethod, ProportionalAllocateMethod,\
    DumbMethod, SphereAllocationMethod


import numpy as np
from matplotlib import pyplot as plt


METHODS = [
    EqualAllocationMethod,
    ProportionalAllocateMethod,
    DumbMethod,
    SphereAllocationMethod
]


def simulate(n: int):
    print(f'Simulation for {n} trials:')
    history = []
    for i in range(n):
        manager = ExecutionManager(Config.AVAILABLE_PAGES)
        processes = manager.setup_processes(Config.NUM_OF_PROCESSES,
                                            Config.LEN_OF_PROCESSES,
                                            Config.MIN_FRAMES,
                                            Config.MAX_FRAMES)
        history.append(manager.execute_all(METHODS, processes, plot=False))
        print(f'{i+1}/{n}')
    methods = []
    for i in range(len(METHODS)):
        methods.append([hist[i] for hist in history])
    summarize(methods)


def plot_results(param, par_name, met_names):
    colors = ['orange', 'red', 'green', 'blue']
    met_names = [f'{name}:\n{param[i]}' for i, name in enumerate(met_names)]
    plt.bar(met_names, param, color=colors)
    plt.title(par_name)
    plt.show()


def summarize(methods):
    means = []
    stds = []
    vars = []
    meds = []
    mins = []
    maxs = []
    parameters = [mins, maxs, means, meds, stds, vars]
    names = ['Minima', 'Maxima', 'Means', 'Medians', 'Standard Deviations', 'Variances']
    method_names = [method.get_name(method) for method in METHODS]

    for method, name in zip(methods, method_names):
        print('======================\n')
        mean = np.mean(method)
        std = round(np.std(method), 2)
        var = round(np.var(method), 2)
        med = np.median(method)
        print(f'{name}\n')
        print(f'Mean: {mean}')
        print(f'Standard deviation: {std}')
        print(f'Variance: {var}\n')
        print(f'Maximum: {max(method)}')
        print(f'Minimum: {min(method)}')
        print(f'Median: {med}\n')
        means.append(mean)
        stds.append(std)
        vars.append(var)
        meds.append(med)
        maxs.append(max(method))
        mins.append(min(method))

    for param, nam in zip(parameters, names):
        plot_results(param, nam, method_names)


if __name__ == '__main__':
    simulate(1000)
