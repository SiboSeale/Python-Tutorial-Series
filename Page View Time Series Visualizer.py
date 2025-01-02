import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]

# Draw line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='tab:red')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
           xlabel='Date', ylabel='Page Views')
    fig.savefig('line_plot.png')
    return fig

# Draw bar plot
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])
    fig.savefig('bar_plot.png')
    return fig

# Draw box plot
def draw_box_plot():
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month_name()

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ])
    axes[1].set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')

    fig.savefig('box_plot.png')
    return fig

if __name__ == "__main__":
    import time_series_visualizer
    from unittest import main

    # Test your function by calling it here
    time_series_visualizer.draw_line_plot()
    time_series_visualizer.draw_bar_plot()
    time_series_visualizer.draw_box_plot()

    # Run unit tests automatically
    main(module='test_module', exit=False)
