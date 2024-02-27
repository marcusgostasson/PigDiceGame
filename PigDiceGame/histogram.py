"""Histogram."""
import matplotlib.pyplot as plt
from PigDiceGame import Highscore


class Histogram:
    """Histogram Class."""

    def __init__(self, names, highscores):
        """Initialize the histogram."""
        self.names = names
        self.highscores = highscores

    def plot_chart(self):
        """Plot the high score table."""
        sorted_data = sorted(zip(self.names, self.highscores), key=lambda x: x[1], reverse=True)
        sorted_names, sorted_highscores = zip(*sorted_data)

        fig, ax = plt.subplots()
        bars = ax.bar(sorted_names, sorted_highscores, color='skyblue', edgecolor='black', alpha=0.7)

        ax.set_title('Highscores')
        ax.set_xlabel('Name')
        ax.set_ylabel('Highscore')

        ax.grid(axis='y', linestyle='--', alpha=0.5)

        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

        plt.xticks(rotation=45)
        plt.tight_layout()  
        plt.show()


high_score_and_name = Highscore()
names, highscores = high_score_and_name.get_name_and_highscore


histogram = Histogram(names, highscores)
histogram.plot_chart()
