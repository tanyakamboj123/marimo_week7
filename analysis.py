import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    #Email :21f3000745@ds.study.iitm.ac.in
    return mo, np, plt


@app.cell
def _(mo):
    # Create a slider to select the number of points
    n_points = mo.ui.slider(10, 100, value=50, label="Number of points")
    n_points  # Display the slider
    return (n_points,)

@app.cell
def _(mo):
    mo.md(
        """
    Dynamic Output
    The current number of points selected is 50.
    This markdown updates automatically when the slider value changes.
    """
    )
    return
@app.cell
def _(n_points, np, plt):
    # Generate random data based on the slider value
    # This cell automatically re-executes when n_points.value changes
    x = np.random.rand(n_points.value)
    y = np.random.rand(n_points.value)

    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Scatter plot with {n_points.value} points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.gca()  # Return the current axes to display the plot
    return


@app.cell
def _(mo, n_points):
    # Dynamic markdown output based on the slider value
    mo.md(f"""
    # Dynamic Output

    The current number of points selected is **{n_points.value}**.

    This markdown updates automatically when the slider value changes.
    """)
    return

if __name__ == "__main__":
    analysis.run()
