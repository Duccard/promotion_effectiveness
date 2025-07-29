import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import kruskal, mannwhitneyu, shapiro
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from itertools import combinations
from matplotlib.colors import LinearSegmentedColormap
from typing import Optional


def plot_sales_boxplot(df: pd.DataFrame, column: str = "Sales_K") -> None:
    """
    Plot a boxplot of weekly sales using a magma color palette.

    Parameters:
    - df: DataFrame containing the sales data.
    - column: Name of the column representing sales values.
    """
    sns.set_palette("magma", 1)
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title("Boxplot of Weekly Sales (in Thousands)")
    plt.xlabel("Sales (k$)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_promotion_sales_boxplot(df: pd.DataFrame, sales_col: str = "Sales_K") -> None:
    """
    Plot a boxplot showing sales distribution by promotion type.

    Parameters:
    - df: DataFrame containing 'Promotion' and sales data.
    - sales_col: Name of the sales column.
    """
    df = df.copy()
    df["Promotion"] = df["Promotion"].astype(str)

    colors = sns.color_palette("magma", len(df["Promotion"].unique()))
    promotion_levels = sorted(df["Promotion"].unique())
    custom_palette = {level: colors[i] for i, level in enumerate(promotion_levels)}

    plt.figure(figsize=(12, 6))
    ax = sns.boxplot(
        data=df,
        x="Promotion",
        y=sales_col,
        hue="Promotion",
        palette=custom_palette,
        legend=False,
    )

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, fc=custom_palette[level])
        for level in promotion_levels
    ]

    plt.legend(
        legend_handles,
        promotion_levels,
        title="Promotion Type",
        loc="upper left",
        bbox_to_anchor=(1.01, 1),
    )
    plt.title("Sales Distribution by Promotion Type")
    plt.xlabel("Promotion Type")
    plt.ylabel("Weekly Sales (in Thousands)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Plot a heatmap showing the lower triangle of correlations among numeric features.

    Parameters:
    - df: DataFrame containing numeric columns.
    """
    corr = df.select_dtypes(include="number").corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    cmap = LinearSegmentedColormap.from_list(
        "light_magma", ["#fbe9d8", "#e0827c", "#7e1e9c"]
    )

    plt.figure(figsize=(10, 6))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap=cmap,
        linewidths=0.5,
        cbar=True,
        annot_kws={"color": "black"},
    )

    plt.title("Correlation Matrix (Lower Triangle)")
    plt.tight_layout()
    plt.show()


def plot_promotion_violinplot(df: pd.DataFrame, sales_col: str = "Sales_K") -> None:
    """
    Plot a violin plot of sales distribution by promotion type.

    Parameters:
    - df: DataFrame with 'Promotion' and sales data.
    - sales_col: Name of the sales column.
    """
    df = df.copy()
    df["Promotion"] = df["Promotion"].astype(str)

    colors = sns.color_palette("magma", 3)
    custom_palette = {"1": colors[0], "2": colors[1], "3": colors[2]}

    plt.figure(figsize=(12, 6))
    sns.violinplot(
        data=df,
        x="Promotion",
        y=sales_col,
        hue="Promotion",
        palette=custom_palette,
        inner="quartile",
        dodge=False,
    )

    legend_elements = [
        Patch(facecolor=colors[0], label="1"),
        Patch(facecolor=colors[1], label="2"),
        Patch(facecolor=colors[2], label="3"),
    ]
    plt.legend(
        handles=legend_elements,
        title="Promotion Type",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.title("Sales Distribution by Promotion Type (Violin Plot)")
    plt.xlabel("Promotion Type")
    plt.ylabel("Weekly Sales (in Thousands)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_promotion_pointplot(df: pd.DataFrame, sales_col: str = "Sales_K") -> None:
    """
    Plot a point plot showing mean sales with 95% confidence intervals by promotion type.

    Parameters:
    - df: DataFrame with 'Promotion' and sales data.
    - sales_col: Name of the sales column.
    """
    df = df.copy()
    df["Promotion"] = df["Promotion"].astype(str)

    colors = sns.color_palette("magma", 3)
    custom_palette = {"1": colors[0], "2": colors[1], "3": colors[2]}

    plt.figure(figsize=(10, 6))
    sns.pointplot(
        data=df,
        x="Promotion",
        y=sales_col,
        hue="Promotion",
        palette=custom_palette,
        capsize=0.1,
        err_kws={"linewidth": 1.5},
        linestyle="none",
        dodge=False,
    )

    legend_elements = [
        Patch(facecolor=colors[0], label="1"),
        Patch(facecolor=colors[1], label="2"),
        Patch(facecolor=colors[2], label="3"),
    ]
    plt.legend(
        handles=legend_elements,
        title="Promotion Type",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.title("Mean Weekly Sales with 95% Confidence Intervals")
    plt.xlabel("Promotion Type")
    plt.ylabel("Average Weekly Sales (in Thousands)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_overall_and_faceted_pointplots(
    df: pd.DataFrame, sales_col: str = "Sales_K", facet_col: str = "MarketSize"
) -> None:
    """
    Plot overall and faceted point plots for weekly sales by promotion type.

    Parameters:
    - df: DataFrame containing 'Promotion', sales, and facet columns.
    - sales_col: Name of the sales column.
    - facet_col: Name of the column to facet by.
    """
    df = df.copy()
    df["Promotion"] = df["Promotion"].astype(str)

    colors = sns.color_palette("magma", 3)
    custom_palette = {"1": colors[0], "2": colors[1], "3": colors[2]}

    plt.figure(figsize=(14, 6))
    sns.pointplot(
        data=df,
        x="Promotion",
        y=sales_col,
        hue="Promotion",
        palette=custom_palette,
        capsize=0.1,
        err_kws={"linewidth": 1.5},
        dodge=True,
    )

    legend_elements = [
        Patch(facecolor=colors[0], label="1"),
        Patch(facecolor=colors[1], label="2"),
        Patch(facecolor=colors[2], label="3"),
    ]
    plt.legend(
        handles=legend_elements,
        title="Promotion Type",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.title("Overall: Mean Weekly Sales by Promotion Type")
    plt.xlabel("Promotion Type")
    plt.ylabel("Weekly Sales (in Thousands)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    g = sns.catplot(
        data=df,
        kind="point",
        x="Promotion",
        y=sales_col,
        hue="Promotion",
        col=facet_col,
        palette=custom_palette,
        capsize=0.1,
        err_kws={"linewidth": 1.5},
        height=5,
        aspect=1.2,
        legend=False,
    )

    g.set_titles("Market Size: {col_name}")
    g.set_axis_labels("Promotion Type", "Weekly Sales (in Thousands)")

    plt.legend(
        handles=legend_elements,
        title="Promotion Type",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.tight_layout()
    plt.show()


def plot_promotion_by_agegroup(
    df: pd.DataFrame, sales_col: str = "Sales_K", age_col: str = "StoreAge"
) -> None:
    """
    Plot point plots showing sales by promotion type across store age groups.

    Parameters:
    - df: DataFrame with 'Promotion', sales, and age data.
    - sales_col: Name of the sales column.
    - age_col: Name of the column representing store age.
    """
    df = df.copy()

    bins = [0, 5, 10, df[age_col].max()]
    labels = ["Young (≤5)", "Mid (6–10)", "Old (>10)"]
    df["AgeGroup"] = pd.cut(df[age_col], bins=bins, labels=labels, right=True)
    df["Promotion"] = df["Promotion"].astype(str)

    colors = sns.color_palette("magma", 3)
    custom_palette = {"1": colors[0], "2": colors[1], "3": colors[2]}

    g = sns.catplot(
        data=df,
        kind="point",
        x="Promotion",
        y=sales_col,
        hue="Promotion",
        col="AgeGroup",
        palette=custom_palette,
        capsize=0.1,
        err_kws={"linewidth": 1.5},
        height=5,
        aspect=1.2,
        legend=False,
    )

    legend_elements = [
        Patch(facecolor=colors[0], label="1"),
        Patch(facecolor=colors[1], label="2"),
        Patch(facecolor=colors[2], label="3"),
    ]
    plt.legend(
        handles=legend_elements,
        title="Promotion Type",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    g.set_titles("Store Age: {col_name}")
    g.set_axis_labels("Promotion Type", "Weekly Sales (in Thousands)")
    plt.tight_layout()
    plt.show()
