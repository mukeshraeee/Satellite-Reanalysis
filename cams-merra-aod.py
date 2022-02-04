##### This scripts enable to plot CAMS data for plotting AOD  ##
#### add libraries ##
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import numpy as np
import cmaps
from matplotlib.patches import Patch
from pylab import *
from matplotlib.pyplot import figure
import matplotlib.gridspec as gridspec
from wrf import smooth2d
import matplotlib as mpl
######## Load CAMS and MERRA-2 AOD data ##################################
monsoon_cams     = 'CAMS_AOD_Monsoon_daily_ave.nc'
nonmonsoon_cams  = 'CAMS_AOD_NonMonsoon_daily_ave.nc'
monsoon_merra    = 'Merra-2_AOD_Monsoon.nc'
nonmonsoon_merra = 'Merra-2_AOD_NonMonsoon.nc'
#####################################################
cams_monsoon     = Dataset(monsoon_cams)
cams_nonmonsoon  = Dataset(nonmonsoon_cams)
merra_monsoon    = Dataset(monsoon_merra)
merra_nonmonsoon = Dataset(nonmonsoon_merra)
############# Getting AOD ###########################
aod_monsoon_cams       = cams_monsoon.variables['aod550'][:]
aod_nonmonsoon_cams    = cams_nonmonsoon.variables['aod550'][:]
aod_monsoon_merra      = merra_monsoon.variables['TOTEXTTAU'][:]
aod_nonmonsoon_merra   = merra_nonmonsoon.variables['TOTEXTTAU'][:]

############ smooth  #######################
smooth_monsoon_cams     = smooth2d(aod_monsoon_cams, 5, cenweight=5)
smooth_nonmonsoon_cams  = smooth2d(aod_nonmonsoon_cams, 5, cenweight=5)
smooth_monsoon_merra    = smooth2d(aod_monsoon_merra, 5, cenweight=5)
smooth_nonmonsoon_merra = smooth2d(aod_nonmonsoon_merra, 5, cenweight=5)
############# Getting lat and long ###############
lat  = cams_monsoon.variables['latitude'][:]
lon  = cams_monsoon.variables['longitude'][:]
lat1 = merra_monsoon.variables['lat'][:]
lon1 = merra_monsoon.variables['lon'][:]

#####  average over the first dimension: time ####
avg_monsoon_cams     = np.mean(smooth_monsoon_cams[:,:,:], axis = 0)
avg_nonmonsoon_cams  = np.mean(smooth_nonmonsoon_cams[:,:,:], axis = 0)
avg_monsoon_merra    = np.mean(smooth_monsoon_merra[:,:,:], axis = 0)
avg_nonmonsoon_merra = np.mean(smooth_nonmonsoon_merra[:,:,:], axis = 0)
################### Plot for Monsoon  ###########################################
#fig = plt.figure()
#gridspec.GridSpec(2,2)
plt.subplot(221)
############################################################
#plt.subplot2grid((2,2), (0,0))
m1 = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m1.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m1.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m1.drawcountries()
m1.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon,lat) # set the latitude and longitude variables from the data
x,y = m1(lons, lats)
cams_monsoon_plot = m1.pcolormesh(x, y, avg_monsoon_cams, cmap=cmaps.WhiteBlueGreenYellowRed) # plot the temperature data on the map
#cbar1 = m1.colorbar(cams_monsoon_plot, location='bottom', pad="10%",size="5%",ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
#cbar1.ax.set_xticklabels(['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1'])
plt.title('CAMS [Monsoon]')
plt.clim(0,1)
plt.colorbar()
################## Plot MERRA-2 - monsoon  ##############################
plt.subplot(223)
#plt.subplot2grid((2,2), (1,0))
m3= Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m3.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m3.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m3.drawcountries()
m3.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon1,lat1) # set the latitude and longitude variables from the data
x,y = m3(lons, lats)
merra_monsoon_plot = m3.pcolormesh(x, y, avg_monsoon_merra, cmap=cmaps.WhiteBlueGreenYellowRed)
#cbar3 = m3.colorbar(merra_monsoon_plot, location='bottom', pad="10%",size="5%",ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
#cbar3.ax.set_xticklabels(['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1'])
plt.title('MERRA-2 [Monsoon]')
#plt.subplots_adjust(bottom=0.1, right=0.88, top=0.88,left=0.14)
#cax = plt.axes([0.5, 0.1, 0.03, 0.8]) #left, bottom, width, height
plt.clim(0,1)
plt.colorbar()

################ cams - non monsoon ######################################
plt.subplot(222)
#plt.subplot2grid((2,2), (0,1))
m2 = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m2.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m2.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m2.drawcountries()
m2.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon,lat) # set the latitude and longitude variables from the data
x,y = m2(lons, lats)
cams_nonmonsoon_plot = m2.pcolormesh(x, y, avg_nonmonsoon_cams, cmap=cmaps.WhiteBlueGreenYellowRed) # plot the temperature data on the map
#cbar2 = m2.colorbar(cams_nonmonsoon_plot, location='bottom', pad="10%",size="5%",ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
#cbar2.ax.set_xticklabels(['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1'])
plt.title('CAMS [Non-Monsoon]')
plt.clim(0,1)
plt.colorbar()
################## Plot for MERRA-2 nonmonsoon  ##########################
plt.subplot(224)
#plt.subplot2grid((2,2), (1,1))
m4 = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m4.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m4.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m4.drawcountries()
m4.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon1,lat1) # set the latitude and longitude variables from the data
x,y = m4(lons, lats)
merra_nonmonsoon_plot = m4.pcolormesh(x, y, avg_nonmonsoon_merra, cmap=cmaps.WhiteBlueGreenYellowRed)
#cbar4 = m4.colorbar(merra_nonmonsoon_plot, location='bottom', pad="10%",size="5%",ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
#cbar4.ax.set_xticklabels(['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1'])
plt.title('MERRA-2 [Non-Monsoon]')
plt.clim(0,1)
plt.colorbar()
#plt.subplots_adjust(bottom=0.1, right=0.9, top=0.9)
#cax = plt.axes([0.9, 0.1, 0.03, 0.8])   # left, bottom, width, height
#plt.colorbar(cax=cax)


plt.show()

