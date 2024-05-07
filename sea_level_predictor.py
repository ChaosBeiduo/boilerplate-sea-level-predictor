import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    def draw_plot():
    df = pd.read_csv('datas\epa-sea-level.csv')
    
    plt.figure(figsize=(12, 8))

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    
    x_pre = np.arange(df['Year'].min(), 2051)
    y_pre = res.slope * x_pre + res.intercept
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)
    plt.plot(x_pre, y_pre)
    
    df_new = df[df['Year'] >= 2000]
    
    x = df_new['Year']
    y = df_new['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    
    x_pre = np.arange(df_new['Year'].min(), 2051)
    y_pre = res.slope * x_pre + res.intercept
    
    plt.plot(x_pre, y_pre)
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
