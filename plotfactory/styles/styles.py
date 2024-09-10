import matplotlib.pyplot as plt

def set_marker_cycle():
    from cycler import cycler

    markers = ['o', '^', 's', 'D', 'X', '*', 'H', '<', '8', 'v', 'P']
    # Update the marker cycle
    plt.rcParams.update({
        'axes.prop_cycle': cycler('marker', markers)
    })
    return markers
    
def set_color_cycle(style='default'):
    from cycler import cycler
    
    if style=='default':
        col_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink']
        
    elif style=='OP':
        col_list = ['teal', 'firebrick', 'green', 'blue', 'indigo', 'brown', 'crimson', '#7f7f7f', '#bcbd22', '#17becf', 'red']

    # Update the color cycle
    plt.rcParams.update({
        'axes.prop_cycle': cycler('color', col_list)
    })
    return col_list