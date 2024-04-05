#%%
import plotfactory.definitions as definitions
from pathlib import Path

notexstyle = Path(definitions.MPLSTYLE_DIR) / 'notex.mplstyle'
notex4slidestyle = Path(definitions.MPLSTYLE_DIR) / 'notex4slide.mplstyle'
texstyle = Path(definitions.MPLSTYLE_DIR) / 'tex.mplstyle'
tex4slidesstyle = Path(definitions.MPLSTYLE_DIR) / 'tex4slides.mplstyle'
notexposterstyle = Path(definitions.MPLSTYLE_DIR) / 'notexposter.mplstyle'
notexposte = Path(definitions.MPLSTYLE_DIR) / 'notexposter.mplstyle'

from plotfactory.src import plotting
from plotfactory.src.plotting import join_axes, join_xaxes, join_yaxes
from plotfactory.styles.mplcolormaps import bipolar_cm
# %%
