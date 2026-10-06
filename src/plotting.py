"""Shared plotting helpers and colour palette for the market value notebook."""

import matplotlib.pyplot as plt
import seaborn as sns

# Light-to-dark green palette used by the Plotly maps and the scatter plot
GREEN_SCALE = [
    "#f2f9e6", "#e6f2cc", "#c9e5a1", "#b2e67d", "#99e24b",
    "#80db28", "#66d31c", "#4dc810", "#33c40b", "#1fb500",
    "#009900", "#007700", "#004d00",
]


def plot_missing_values(df):
    """Heatmap of missing values: one column per feature, one row per player."""
    plt.figure(figsize=(16, 9))

    sns.heatmap(df.isnull(),
                cmap='rocket',
                cbar=False,
                yticklabels=False)

    plt.title("Visualisation des valeurs manquantes", fontsize=18)
    plt.xlabel("Colonnes", fontsize=14)
    plt.ylabel("Observations", fontsize=14)
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()


def plot_count_bars(counts, category_col, ylabel):
    """Horizontal bar chart of player counts per category.

    ``counts`` must contain the category column ``category_col`` and a
    ``Nombre`` column with the number of players in each category.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=counts,
        y=category_col,
        x="Nombre",
        hue=category_col,
        palette=sns.color_palette("Greens", n_colors=len(counts))[::-1],  # Reversed gradient
        dodge=False,
        legend=False
    )

    plt.xlabel("Nombre d'occurrences")
    plt.ylabel(ylabel)
    plt.title("Effectif de chaque catégorie de position")
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    plt.show()
