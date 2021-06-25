import matplotlib.pyplot as plots
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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


####
### from disasterweets:
def plot_bar_x(df,ylabel, feature,text_ykey):
    # this is for plotting purpose
#     lab=list(df[xlabel].unique())
    index = np.arange(len(ylabel))
    df.plot.bar(color={0: "blue", 1: "cyan"},figsize=(15, 3))
#     plt.grid()
    plt.xlabel(feature, fontsize=15)
    plt.ylabel('count', fontsize=15)
    plt.xticks(index, ylabel, fontsize=15, rotation=45, horizontalalignment='right')
    plt.yticks(fontsize=15, rotation=0, horizontalalignment='right')
    plt.title('Tweet ' + feature + ' analysis', fontsize=15)
    plt.legend(text_ykey,prop={'size': 14})
#     plt.tight_layout()
#     plt.savefig('figures/'+feature +'_analysis.png')
    plt.show()
