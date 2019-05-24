# Define the interactive plot for symbol
def interactive_plot_symbol(dataframe, symbol, date, x, y):
    I = (dataframe.date >= date[0]) & (dataframe.date <= date[-1]) & (dataframe.symbol == symbol)
    ax = dataframe.loc[I,:].plot(x=x, y=y, legend=False)



# Define the interactive plot for sector
def interactive_plot_sector(dataframe, sector, date, x, y):
    I = (dataframe.date >= date[0]) & (dataframe.date <= date[-1]) & (dataframe.sector == sector)
    ax = dataframe.loc[I,:].plot(x=x, y=y, legend=False)