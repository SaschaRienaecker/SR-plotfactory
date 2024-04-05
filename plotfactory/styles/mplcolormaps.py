def bipolar_cm(lutsize=256, n=0.333, interp=[]):
    """
    lutsize : int
        The number of elements in the colormap lookup table. (Default is 256.)
    n : float
        The gray value for the neutral middle of the colormap.  (Default is
        1/3.)
        The colormap goes from cyan-blue-neutral-red-yellow if neutral
        is < 0.5, and from blue-cyan-neutral-yellow-red if neutral > 0.5.
        For shaded 3D surfaces, an `n` near 0.5 is better, because it
        minimizes luminance changes that would otherwise obscure shading cues
        for determining 3D structure.
        For 2D heat maps, an `n` near the 0 or 1 extremes is better, for
        maximizing luminance change and showing details of the data.
    interp : str or int, optional
        Specifies the type of interpolation.
        ('linear', 'nearest', 'zero', 'slinear', 'quadratic, 'cubic')
        or as an integer specifying the order of the spline interpolator
        to use. Default is 'linear'.  See `scipy.interpolate.interp1d`.
    """
    from matplotlib import cm
    # import scipy
    from scipy.interpolate import interp1d
    import numpy as np
    # import matplotlib.pyplot as plt
    # import matplotlib as mpl
    if n < 0.5:
        if not interp:
            interp = 'linear'

        _data = (
            (1, 1, 1),
            (0, 1, 1), # cyan
            (0, 0, 1), # blue
            #(n, n, n), # dark neutral
            (0, 0, n),
            (1, 0, 0), # red
            (1, 1, 0), # yellow
        )
    elif n >= 0.5:
        if not interp:
            interp = 'cubic'

        _data = (
            (0, 0, 1), # blue
            (0, 1, 1), # cyan
            (n, n, n), # light neutral
            (1, 1, 0), # yellow
            (1, 0, 0), # red
        )
    else:
        raise ValueError('n must be 0.0 < n < 1.0')

    xi = np.linspace(0, 1, np.size(_data, 0))

    #xi = np.cumsum([4,2,1,1,1,1])
    xi = np.cumsum([2,5,2,2,2,2])
    xi = xi - xi[0]
    xi = xi/xi[-1]

    cm_interp = interp1d(xi, _data, axis=0, kind=interp)
    xnew = np.linspace(0, 1, lutsize)
    ynew = cm_interp(xnew)

    ynew = np.clip(ynew, 0, 1)

    return cm.colors.LinearSegmentedColormap.from_list('bipolar', ynew, lutsize)

