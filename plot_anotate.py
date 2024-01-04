import matplotlib.pyplot as plt


def plot(height, width, colors, h, w):
    x = width
    y = height
    colors = colors

    aspect_ratio = w / h
    w = 6
    h = w / aspect_ratio

    fig, ax1 = plt.subplots(figsize=(w, h))
    fig2, ax2 = plt.subplots(figsize=(w, h))
    fig3, ax3 = plt.subplots(figsize=(w, h))

    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(3):
                if k == 0:
                    ax1.plot(x[i], y[j], marker='s', markersize=2, color=(1, 0, 0), linestyle='none')
                    ax1.annotate(text=f'{round((colors[j][i][k]), 2)}', xy=(x[i], y[j]))
                elif k == 1:
                    ax2.plot(x[i], y[j], marker='s', markersize=2, color=(0, 1, 0), linestyle='none')
                    ax2.annotate(text=f'{round((colors[j][i][k]), 2)}', xy=(x[i], y[j]))
                else:
                    ax3.plot(x[i], y[j], marker='s', markersize=2, color=(0, 0, 1), linestyle='none')
                    ax3.annotate(text=f'{round((colors[j][i][k]), 2)}', xy=(x[i], y[j]))

    for i in range(3):
        if i == 0:
            ax1.set_title('Red plot')
            ax1.set_xlabel('Width')
            ax1.set_ylabel('Height')
        elif i == 1:
            ax2.set_title('Green plot')
            ax2.set_xlabel('Width')
            ax2.set_ylabel('Height')
        else:
            ax3.set_title('Blue plot')
            ax3.set_xlabel('Width')
            ax3.set_ylabel('Height')

    plt.show()
