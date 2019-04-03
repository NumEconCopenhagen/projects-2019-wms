### Dataproject
##### Created by: Mads-Emil Granzow, Waldemar Shuppli and Sofie Juel

This project examines historical daily price data for stocks in the US in the period 2015-01-02 - 2019-01-02. Data is obtained by using an API for IEX to retrieve data on daily close values as well as sector on each of the individual stocks. 

To get an overview of the individual stocks data manipulation is performed and summary statistics are calculated. The data includes 8.715 stocks and 1.007 observations (days) for each individual stock. Further, most stocks represent the sector: 'financial services'.

The data has been retrieved using the `iexfinance` module. Because the retrieval of all 8.715 stocks has some runtime, the initial datasets `df_close.csv` and `df_ticker.csv` has been attached to the hand-in. `df_close.csv` contains the closing prices for all the listed stocks for the available trading period. `df_ticker.csv` contains some additional background information on each stock - e.g. sector. With these dataframes loaded, the notebook can be run from the `Data-manupulation` section. DO NOT RUN the data load-in section.

Next a number of descriptive plots as well as interactive plots are created to identify differences in close prices and returns across period, sector and the individual stocks. These can be manipulated with to see the price movement and returns for any desired stocks and/or sectors.

This notebook can also function as a starting point to testing many finanical econometrics models empirically including the classical time-series models for single stocks, portfolio theory, CAPM etc.








