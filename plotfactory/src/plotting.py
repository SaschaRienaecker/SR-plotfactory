#%%
import string
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def get_figsize(width='thesis', width_fraction=1, height_fraction=None):
    """
    This code ( set_size ) fragment is copied from
    https://jwalton.info/Embed-Publication-Matplotlib-Latex/

    Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
    width_fraction: float, optional
            width_fraction of the width which you wish the figure to occupy
    aspect_r: float, optional
            Aspect ratio, determines the height based on the width. Default is golden ratio.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 452.9679
    elif width == 'TP':
        width_pt = 418.25
    elif width == 'article':
        width_pt = 250.0
    elif width == 'poster':
        width_pt = (2336.0- 200) / 2 # 2 columns
    # elif width == 'beamer':
    #     width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * width_fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    if height_fraction is None:
        # Golden ratio to set aesthetic figure height
        # https://disq.us/p/2940ij3
        height_fraction = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in / width_fraction * height_fraction

    return (fig_width_in, fig_height_in)

def subplots_indexing(axs, hpos=0.5, vpos=1.1, ha='center', va='top', start=0):

    for n, ax in enumerate(axs.flatten()):
        ax.text(hpos, vpos, '({})'.format(string.ascii_lowercase[n + start]), transform=ax.transAxes, ha=ha,
                va=va)
        

def join_axes(axs, sharex=True, sharey=True, remove_ticks=True, remove_xlabels=True, remove_ylabels=True):
    
    if axs.ndim == 1:
        
        if sharex:
            axs[0].get_shared_x_axes().join(*axs)
            
            if remove_ticks:
                for ax in axs[:-1]:
                    ax.set_xticklabels([])
                    
            if remove_xlabels:
                for ax in axs[:-1]:
                    ax.set_xlabel('')
        
        if sharey:
            axs[0].get_shared_y_axes().join(*axs)
            
            if remove_ticks:
                for ax in axs[1:]:
                    ax.set_yticklabels([])
            if remove_ylabels:
                for ax in axs[1:]:
                    ax.set_ylabel('')
       
    elif axs.ndim == 2:
        if sharex:
            axs[0,0].get_shared_x_axes().join(*axs.flatten())
            
            for ax in axs[:-1,:].flat:
                if remove_ticks:
                    ax.set_xticklabels([])
                    
                if remove_xlabels:
                    ax.set_xlabel('')
        if sharey:
            axs[0,0].get_shared_y_axes().join(*axs.flatten())
            for ax in axs[:,1:].flat:
                if remove_ticks:
                    ax.set_yticklabels([])
                    
                if remove_ylabels:
                    ax.set_ylabel('')
    
        

# %%
if __name__ == '__main__':
    
    fig,axs = plt.subplots(1,3)
    # fig,axs = plt.subplots(2,3)
    for ax in axs.flat:
        ax.set_xlabel('xlabel')
        ax.set_ylabel('ylabel')
    join_axes(axs, sharex=True, sharey=True)
#%%
def join_yaxes(ax_left, ax_right, remove_ticks=True):
    ax_right.get_shared_y_axes().join(ax_left,ax_right)
    if remove_ticks:
        ax_right.set_yticklabels([])
        ax_right.set_ylabel('')
        
    
    
def join_xaxes(ax_top, ax_bot, remove_ticks=True):
    ax_top.get_shared_x_axes().join(ax_top,ax_bot)
    if remove_ticks:
        ax_top.set_xticklabels([])
        ax_top.set_xlabel('')
    

def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


def multiline(xs, ys, c, ax=None, **kwargs):

    """Plot lines with different colorings
    https://stackoverflow.com/questions/38208700/matplotlib-plot-lines-with-colors-through-colormap

    Parameters
    ----------
    xs : iterable container of x coordinates
    ys : iterable container of y coordinates
    c : iterable container of numbers mapped to colormap
    ax (optional): Axes to plot on.
    kwargs (optional): passed to LineCollection

    Notes:
        len(xs) == len(ys) == len(c) is the number of line segments
        len(xs[i]) == len(ys[i]) is the number of points for each line (indexed by i)

    Returns
    -------
    lc : LineCollection instance.
    """
    from matplotlib.collections import LineCollection

    # find axes
    ax = plt.gca() if ax is None else ax

    # create LineCollection
    segments = [np.column_stack([x, y]) for x, y in zip(xs, ys)]
    lc = LineCollection(segments, **kwargs)

    # set coloring of line segments
    #    Note: I get an error if I pass c as a list here... not sure why.
    lc.set_array(np.asarray(c))

    # add lines to axes and rescale 
    #    Note: adding a collection doesn't autoscalee xlim/ylim
    ax.add_collection(lc)
    ax.autoscale()
    return lc

def annotate(txt, x=None, y=None, style='horiz', ax=None, **kwargs):
    """Annotate the plot with some text.
    Args:
        txt (str): Text to annotate with.
        x (float): x coordinate of the text.
        y (float): y coordinate of the text.
        style (str, optional): Style of the annotation: 'vert' or 'horiz', default 'horiz'.
        ax (matplotlib.axes.Axes): Axes to annotate on.
        **kwargs: Additional keyword arguments passed to ax.annotate.
    """

    if ax is None:
        ax = plt.gca()
    
    # fontsize = kwargs.get('fontsize', 12)
    # color = kwargs.get('color', 'black')
    
    # if custom_txt is None:
    #     txt = ''

    #     if machine is not None:
    #         txt += machine + ' '
    #     if shot is not None:
    #         txt += str('#' + str(shot))
    #     if time is not None:
    #         txt += f', $t={time:.2f}$s'
    # else:
    #     txt = custom_txt

    # default parameters:


    if style == 'vert':
        # annotate the shot number in the lower right corner verticvally:
        transform = kwargs.get('transform', ax.transAxes)
        x = 1.005 if x is None else x
        y = 0.005 if y is None else y
        va = kwargs.get('va','bottom')
        ha = kwargs.get('ha','left')
        rotation = kwargs.get('rotation', -90)

        kwargs.update({'rotation': rotation, 'ha': ha, 'va': va, 'transform': transform})

        # ax.text(x, y, txt, transform=ax.transAxes, fontsize=fontsize,   
        #                 va='bottom', ha='left', color=color,
        #                 rotation=-90)
        
    elif style == 'horiz':
        # annotate the shot number in the upper right corner horizontally:
        transform = kwargs.get('transform', ax.transAxes)
        x = 1.0 if x is None else x
        y = 1.005 if y is None else y
        va = kwargs.get('va','bottom')
        ha = kwargs.get('ha','right')
        rotation = kwargs.get('rotation', 0)
        kwargs.update({'rotation': rotation, 'ha': ha, 'va': va, 'transform': transform})

    else:
        x = 0.0
        y = 0.0

    ax.text(x,y,txt, **kwargs)


def average_color(color1, color2):
    # Convert matplotlib colors to RGB tuples
    rgb1 = mcolors.to_rgba(color1)[:3]
    rgb2 = mcolors.to_rgba(color2)[:3]
    
    # Calculate component-wise average
    avg_rgb = [(c1 + c2) / 2 for c1, c2 in zip(rgb1, rgb2)]
    
    # Convert back to matplotlib color format
    avg_color = mcolors.to_hex(avg_rgb)
    
    return avg_color

def make_inset(ax,  bbox=[0.01, 0.7, 0.3, 0.3], remove_axis_frame=False, **kwargs):

    transform = kwargs.pop('transform', ax.transAxes)
    

    axins = ax.inset_axes(bbox, transform=transform)
    if remove_axis_frame:
        axins.set_frame_on(False)
        axins.grid(False)
        axins.set_xticks([])
        axins.set_yticks([])
    
    return axins


# %%
if __name__ == '__main__':
    import numpy as np
    from plotfactory import notexposterstyle
    plt.style.use(notexposterstyle)
    fs = get_figsize(width='poster', width_fraction=.25, height_fraction=.25)
    fig, ax = plt.subplots(figsize=fs)
    ax.plot(np.random.rand(10), 'bo-', label='text')
    ax.legend()
    ax.plot(np.random.rand(10), 'rs-')
    ax.set_xlabel('xlabel [unit]')
    ax.set_ylabel('ylabel [unit]')
    plt.tight_layout()
    # fig.savefig('/tmp/test.pdf')

# %%
if __name__ == '__main__':
    ### Average color example 
    
    # Define two matplotlib colors
    color1 = 'blue'
    color2 = 'green'

    # Calculate the average color
    avg_color_result = average_color(color1, color2)

    # Plot the original colors and the average color
    fig, axs = plt.subplots(1, 3, figsize=(8, 3))
    axs[0].imshow([[mcolors.to_rgba(color1)]])
    axs[0].set_title(color1)
    axs[0].axis('off')

    axs[1].imshow([[mcolors.to_rgba(color2)]])
    axs[1].set_title(color2)
    axs[1].axis('off')

    axs[2].imshow([[mcolors.to_rgba(avg_color_result)]])
    axs[2].set_title('Average')
    axs[2].axis('off')

    plt.tight_layout()
    plt.show()

    print(f"Average Color: {avg_color_result}")
    

# %%
