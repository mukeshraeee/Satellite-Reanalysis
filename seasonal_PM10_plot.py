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
### Load data ##################################
winter = "winter-pm10.nc"
spring = "spring-pm10.nc"
summer = "summer-pm10.nc"
autumn = "autumn-pm10.nc"
#####################################################
winter_data = Dataset(winter)
spring_data = Dataset(spring)
summer_data = Dataset(summer)
autumn_data = Dataset(autumn)
#############Getting AOD ###########################
aod_winter = winter_data.variables['pm10'][:]
aod_spring = spring_data.variables['pm10'][:]
aod_summer = summer_data.variables['pm10'][:]
aod_autumn = autumn_data.variables['pm10'][:]
############ smooth  #######################
smooth_winter = smooth2d(aod_winter, 1, cenweight=1)
smooth_spring = smooth2d(aod_spring, 1, cenweight=1)
smooth_summer = smooth2d(aod_summer, 1, cenweight=1)
smooth_autumn = smooth2d(aod_autumn, 1, cenweight=1)
############# Getting lat and long ###############
lat = winter_data.variables['latitude'][:]
lon = winter_data.variables['longitude'][:]
#####  average over the first dimension: time ####
avg_winter = np.mean(smooth_winter[:,:,:], axis = 0)
avg_spring = np.mean(smooth_spring[:,:,:], axis = 0)
avg_summer = np.mean(smooth_summer[:,:,:], axis = 0)
avg_autumn = np.mean(smooth_autumn[:,:,:], axis = 0)

################### Plot for winter ###########################################
fig = plt.figure()
gridspec.GridSpec(2,2)
plt.subplot2grid((2,2), (0,0))
########################################################
m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m.drawcountries()
m.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon,lat) # set the latitude and longitude variables from the data
x,y = m(lons, lats)
winter_plot = m.pcolormesh(x, y, avg_winter, cmap=cmaps.WhiteBlueGreenYellowRed) # plot the temperature data on the map
cbar = m.colorbar(winter_plot, location='bottom', pad="10%",size="5%") #,ticks=[-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30])
#cbar.ax.set_xticklabels(['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30'])
plt.title('Winter[PM10]')

################ Plot for Spring ######################################
plt.subplot2grid((2,2), (0,1))

m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m.drawcountries()
m.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon,lat) # set the latitude and longitude variables from the data
x,y = m(lons, lats)
spring_plot = m.pcolormesh(x, y, avg_spring, cmap=cmaps.WhiteBlueGreenYellowRed) # plot the temperature data on the map
cbar = m.colorbar(spring_plot, location='bottom', pad="10%",size="5%") #,ticks=[0.5,0.6,0.7,0.8,0.9,1,1,1.1,1.2])
#cbar.ax.set_xticklabels(['0.5','0.6','0.7','0.8','0.9','1','1.1','1.2'])
plt.title('Spring[PM10]')

############### Plot for Summer ##################################
plt.subplot2grid((2,2), (1,0))

m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m.drawcountries()
m.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon,lat) # set the latitude and longitude variables from the data
x,y = m(lons, lats)
summer_plot = m.pcolormesh(x, y, avg_summer, cmap=cmaps.WhiteBlueGreenYellowRed)
cbar = m.colorbar(summer_plot, location='bottom', pad="10%",size="5%")
plt.title('Summer[PM10]')

##################### Plot for autumn ##########################
plt.subplot2grid((2,2), (1,1))

m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
m.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m.drawcountries()
m.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(lon,lat) # set the latitude and longitude variables from the data
x,y = m(lons, lats)
autumn_plot = m.pcolormesh(x, y, avg_autumn, cmap=cmaps.WhiteBlueGreenYellowRed)
cbar = m.colorbar(autumn_plot, location='bottom', pad="10%",size="5%")
plt.title('Autumn[PM10]')

plt.show()

