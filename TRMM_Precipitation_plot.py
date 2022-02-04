##====== Import libraries ====================
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import numpy as np
from matplotlib.patches import Patch
from pylab import *
import cmaps
##===========================================
nc =  "3B43.20170701.7.HDF.nc4"
fh =  Dataset(nc,'r')

lons = fh.variables['nlon'][:]
lats = fh.variables['nlat'][:]
ppt = fh.variables['precipitation'][:]
##===== Transpose requires for plotting precipitation ========
ppt1 = np.transpose(ppt)

m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=119,urcrnrlat=50,resolution='h')
#======= Use meshgrid to create 2D arrays ===================
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)
####### Now plot the data #######
cs = m.pcolor(xi,yi,np.squeeze(ppt1),cmap=cm.tab20c)
#====== Add Grid lines ==================
m.drawparallels(np.arange(10, 50, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
#======== Add countries boundasy ==================
m.drawcountries()
m.drawcoastlines()
#========= Add Colourbar =============
cbar = m.colorbar(cs, location='bottom', pad="10%",size="5%")
cbar.set_label('Total Precipitation(mm)')
#======= Add Title ==============
plt.title('TRMM-Total precipitation')


plt.show()

