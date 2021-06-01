import matplotlib.pyplot as plots
import seaborn as sns
import pandas as pd 

def exploratory_plots(df,keys_to_plot, id_key,y_key):
    fig, axes = plt.subplots(pairs_to_display,2 , sharex=True, figsize=(16,8))
    fig.suptitle('Exploratory plots')

    counter_even=-1
    counter_odd=-1
    for plot_no in range(len(keys_to_plot)):
        kn=keys_to_plot[plot_no]
        if (plot_no % 2) == 0:
            counter_even+=1
            pos1=0
            pos2=counter_even
        else:
            counter_odd+=1
            pos1=1
            pos2=counter_odd
        print(pos1,pos2)
        sns.scatterplot(ax=axes[pos2,pos1],x=df[df.keys()[id_key]], y=df[df.keys()[kn]], hue=df.keys()[y_key],data=df)
        axes[pos2,pos1].set_title(df.keys()[id_key]+'vs '+df.keys()[kn])
