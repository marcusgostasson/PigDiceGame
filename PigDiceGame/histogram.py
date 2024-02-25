"""Histogram Class."""
import matplotlib.pyplot as plt


class Histogram:
    """Constructor for histogram."""

    def __init__(self, name, highscore):
        """Attributes."""
        self.name = name
        self.highscore = highscore

    def plot_chart(self):
        """Plotting the high score tabel."""
        plt.bar(self.name.get_name, self.highscore.get_highscore, color='blue')
        plt.title('Highscores')
        plt.xlabel('Namn')
        plt.ylabel('Highscore')
        plt.show()

        histogram = Histogram(name, highscore)
        highscore_chart.plot_chart(histogram)
