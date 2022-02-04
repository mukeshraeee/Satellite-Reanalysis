""" This code enable to visualize and produce animatio of
    CAMS forecast data """

import os
import xarray as xr
import numpy as np
import netCDF4 as nc
import pandas as pd
from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.cm import get_cmap
#from matplotlib import animation
import matplotlib.animation as animation
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
from matplotlib.axes import Axes
from cartopy.mpl.geoaxes import GeoAxes
GeoAxes._pcolormesh_patched = Axes.pcolormesh
from mpl_toolkits.basemap import Basemap
import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.mpl.ticker as cticker 
import matplotlib.ticker as mticker
import cmaps
# load EAC4 reanalysis data
file = xr.open_dataset('data.nc')
# = Bring longitude coordinates onto a [-180,180] grid
#file_assigned = file.assign_coords(longitude=(((file.longitude + 180) % 360) - 180)).sortby('longitude')
# retrieve the data variable  AOD at 550nm as xarray.DataArray

aod = file.aod550

#=== Get long name and units
long_name = aod.long_name
units     = aod.units
#== get lat lon
lats  = aod.latitude
lons = aod.longitude

def make_figure():
    fig = plt.figure(figsize=(6, 3), dpi=200)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    # generate a basemap with country borders, oceans and coastlines
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_left = True
    gl.ylabels_right  = False    
    gl.xlabels_bottom = True    
    gl.xlines = True
    gl.xlocator = mticker.FixedLocator([130,120,110,100,90,80,70,60,50,40,30])
    gl.ylocator = mticker.FixedLocator([0,10,20,30,40,50,60])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 8, 'color': 'black'}
    gl.ylabel_style = {'size': 8, 'color': 'black'}
    lon_formatter = cticker.LongitudeFormatter()
    lat_formatter = cticker.LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #ax.gridlines(xlocs=np.arange(45,125,15), draw_labels=True, crs=ccrs.PlateCarree())
    ax.add_feature(cfeat.LAND,facecolor='0.3')
    ax.add_feature(cfeature.LAKES, alpha=0.9)
    ax.add_feature(cfeat.OCEAN)
    ax.add_feature(cfeat.COASTLINE,zorder=10)
    ax.add_feature(cfeat.BORDERS, linestyle='solid')
    return fig, ax

make_figure();

fig, ax = make_figure()

frames    = aod.time.size
min_value = aod.values.min()
max_value = aod.values.max()


def draw(frame, add_colorbar):
    grid = aod[frame]
    contour = grid.plot(ax=ax, transform=ccrs.PlateCarree(),cmap=cmaps.WhiteBlueGreenYellowRed,
                        add_colorbar=add_colorbar, vmin=min_value, vmax=max_value)
    title = u"%s — %s" % (file.aod550.long_name, str(aod.time[frame].values)[:20])
    ax.set_title(title)
    return contour


def init():
    return draw(0, add_colorbar=True)


def animate(frame):
    return draw(frame, add_colorbar=False)


ani = animation.FuncAnimation(fig, animate, frames, interval=0.015, blit=False,
                              init_func=init, repeat=False)
ani.save('cams_aod_forecast5.gif', writer=animation.FFMpegWriter(fps=8))
plt.close(fig)
