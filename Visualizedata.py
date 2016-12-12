def auto_scatter_simple(df, plot_cols):
    import matplotlib.pyplot as plt
    ## Loop over the columns
    for col in plot_cols:
        fig = plt.figure(figsize=(6, 6))
        ax = fig.gca()
        ## simple scatter plot
        df.plot(kind = 'scatter', x = col, y = 'Marks', 
                           ax = ax, color = 'DarkBlue')                          
        ax.set_title('Scatter plot of marks vs. ' + col)
        fig.savefig('scatter_' + col + '.png')
    return plot_cols              

def azureml_main(df): 
    import matplotlib
    matplotlib.use('agg')
    ## Define plot columns
    plot_cols = ["Syllabus"]
    auto_scatter_simple(df, plot_cols) ## Create plots
    return df