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
class PLOT_LABEL(object):
    def __init__(self,legend_labels,x_axis_title,y_axis_title,x_label,title_str,output_file_name,save_image):
        self.legend_labels= legend_labels
        self.x_axis_title= x_axis_title
        self.y_axis_title=y_axis_title
        self.x_label=x_label
        self.title_str=title_str
        self.output_file_name=output_file_name
        self.save_image=save_image


def plot_bar_x(df,PLOT_LABEL_instance):
    df.plot.bar(color={0: "blue", 1: "cyan"},figsize=(15, 3))

    #axis ticks
    index = np.arange(len(PLOT_LABEL_instance.x_label))
    plt.xticks(index,PLOT_LABEL_instance.x_label, fontsize=15, rotation=45, horizontalalignment='right')
    plt.yticks(fontsize=15, rotation=0, horizontalalignment='right')

    #axis and plot titles
    plt.xlabel(PLOT_LABEL_instance.x_axis_title, fontsize=15)
    plt.ylabel(PLOT_LABEL_instance.y_axis_title, fontsize=15)
    plt.title(PLOT_LABEL_instance.title_str, fontsize=15)

    plt.legend(PLOT_LABEL_instance.legend_labels,prop={'size': 14})
#     plt.grid()
#     plt.tight_layout()
    if PLOT_LABEL_instance.save_image=='ON':
        plt.savefig(PLOT_LABEL_instance.output_file_name)
    plt.show()
