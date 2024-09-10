#%%
import plotfactory.definitions as definitions
from pathlib import Path

notexstyle = Path(definitions.MPLSTYLE_DIR) / 'notex.mplstyle'
notex4slidestyle = Path(definitions.MPLSTYLE_DIR) / 'notex4slide.mplstyle'
texstyle = Path(definitions.MPLSTYLE_DIR) / 'tex.mplstyle'
tex4slidestyle = Path(definitions.MPLSTYLE_DIR) / 'tex4slides.mplstyle'
texposterstyle = Path(definitions.MPLSTYLE_DIR) / 'texposter.mplstyle'
notexposterstyle = Path(definitions.MPLSTYLE_DIR) / 'notexposter.mplstyle'

from plotfactory.src import plotting
from plotfactory.src.plotting import join_axes, join_xaxes, join_yaxes
from plotfactory.styles.mplcolormaps import bipolar_cm
from plotfactory.styles.styles import set_marker_cycle, set_color_cycle
# %%
