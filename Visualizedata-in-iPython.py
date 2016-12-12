## Numeric columns
plot_cols = ["% syllabus","% marks"]
 
## Create pair-wise scatter plots         
def auto_pairs(plot_cols, df):
    import matplotlib.pyplot as plt
    from pandas.tools.plotting import scatter_matrix
    fig = plt.figure(figsize=(12, 12))
    fig.clf()
    ax = fig.gca()
    scatter_matrix(df[plot_cols], alpha=0.3, 
               diagonal='kde', ax = ax)
    return 'Done'           

## Define columns for making a conditioned histogram
plot_cols2 = ["Year",
              "Month",
              "Subject Difficulty",
              "Teacher",
              "Workload before",
              "% syllabus",
              "Subject",
              "% marks"]

## Function to plot conditioned histograms
def cond_hists(df, plot_cols, grid_col):
    import matplotlib.pyplot as plt
    import pandas.tools.rplot as rplot
    ## Loop over the list of columns
    for col in plot_cols:
        ## Define figure
        fig = plt.figure(figsize=(14, 4))
        fig.clf()
        ax = fig.gca()
        ## Setup plot and grid and plot the data
        plot = rplot.RPlot(df, x = col, 
                                  y = '.') 
        plot.add(rplot.TrellisGrid(['.', grid_col]))
        plot.add(rplot.GeomHistogram())
        ax.set_title('Histograms of ' + col + ' conditioned by ' + grid_col + '\n')
        plot.render()
    return grid_col        


## Create boxplots of data
def auto_boxplot(df, plot_cols, by):
    import matplotlib.pyplot as plt
    for col in plot_cols:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        df.boxplot(column = col, by = by, ax = ax)
        ax.set_title('Box plots of ' + col + ' by ' + by)
        ax.set_ylabel(col)
    return by    

