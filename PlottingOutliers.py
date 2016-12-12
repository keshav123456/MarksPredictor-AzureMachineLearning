def id_outlier(df):
    ## Create a vector of 0 of length equal to the number of rows
    temp = [0] * df.shape[0]
    ## test each outlier condition and mark with a 1 as required
    for i, y in enumerate(df['Marks']):
        if (y > 99 or y < 65): temp[i] = 1       
    df['outlier'] = temp # append a column to the data frame
    return df

def auto_scatter_outlier(df, plot_cols):
    import matplotlib.pyplot as plt
    outlier = [0,0,1,1] # Vector of outlier indicators
    color = ['DarkBlue','DarkBlue','Red','Red'] # vector of color choices for plot
    marker = ['x','o','o','x'] # vector of shape choices for plot
    for col in plot_cols: # loop over the columns
        fig = plt.figure(figsize=(6, 6))
        ax = fig.gca()
        ## Loop over the zip of the four vectors an subset the data and
        ## create the plot using the aesthetics provided
        for o, c, m in zip(outlier, color, marker):
            temp = df.ix[(df['outlier'] == o)]           
            if temp.shape[0] > 0:                    
                temp.plot(kind = 'scatter', x = col, y = 'Marks' , 
                           ax = ax, color = c, marker = m)                                 
        ax.set_title('Scatter plot of marks vs. ' + col)
        fig.savefig('scatter_' + col + '.png')
    return plot_cols      

def azureml_main(df): 
    import matplotlib
    matplotlib.use('agg')
    ## Define the plot columns
    plot_cols = ["Syllabus"]
    df = id_outlier(df)  # mark outliers       
    auto_scatter_outlier(df, plot_cols) # create plots
    df = df[df.outlier == 1] # filter for outliers
    return df
