"""Histogram."""
import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Histogram:
    """Histogram Class."""

    def __init__(self):
        """Initialize the histogram."""

    def plot_chart(self, high_score):
        """Plot the high score table."""
        names, values = high_score.get_name_and_highscore()

        if not names and not values:
            print("The list is empty")
        else:
            fig, ax = plt.subplots()
            bars = ax.bar(names, values, color='skyblue',
                          edgecolor='black', alpha=0.7)

            ax.set_title('Highscores')
            ax.set_xlabel('Name')
            ax.set_ylabel('Highscore')

            ax.grid(axis='y', linestyle='--', alpha=0.5)

            for bar_ in bars:
                height = bar_.get_height() + 1
                ax.annotate(f'{height}',
                            xy=(bar_.get_x() + bar_.get_width() / 2, height),
                            xytext=(0, 3),
                            textcoords="offset points",
                            ha='center', va='bottom')

            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
