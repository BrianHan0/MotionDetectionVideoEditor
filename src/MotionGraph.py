import matplotlib.pyplot as plt

def GraphMotionPlot(motion_levels):
    plt.plot(motion_levels)
    plt.title('Motion Graph')
    plt.xlabel('Frame')
    plt.ylabel('Amount of Motion')
    plt.show()


def plot_combined_motion_graph(motion_levels, boundaries):
    plt.plot(motion_levels, label='Motion Level')
    for boundary in boundaries:
        plt.axvline(x=boundary, color='r', linestyle='--', label='Video Boundary' if boundary == boundaries[0] else None)

    plt.title('Combined Motion Graph for Multiple Videos')
    plt.xlabel('Frame')
    plt.ylabel('Amount of Motion')
    plt.legend()
    plt.show()