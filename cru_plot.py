#Add the following useful modules which will help analyse the data
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from  mpl_toolkits.basemap import Basemap
import cmaps
import matplotlib.gridspec as gridspec

### Plotting for Monsoon season
cru_mon = "CRU_Monsoon_temp.nc" # the location of the data
data = Dataset(cru_mon)
### read temp data
temp_mon = data.variables['tmp'][:] # for t
# average over the first dimension: time
temp_av_mon = np.mean(temp_mon[:,:,:], axis = 0)

### plotting subplot
fig = plt.figure()
gridspec.GridSpec(1,2)
plt.subplot2grid((1,2), (0,0))
##########
m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
#map = Basemap(projection="cyl", resolution='c', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180) # set up the map using basemap
m.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m.drawcountries()
m.drawcoastlines(color="black") # add coastlines
lons,lats = np.meshgrid(data.variables['lon'][:], data.variables['lat'][:]) # set the latitude and longitude variables from the data
x,y = m(lons, lats)
temp_plot = m.pcolormesh(x, y, temp_av_mon, cmap=cmaps.WhiteBlueGreenYellowRed) # plot the temperature data on the map
cb = m.colorbar(temp_plot, "bottom", size="5%", pad="2%", extend = 'both') # plotting a colour bar scale
cb.set_label(u"Temperature \u2103") # \u2103 is unicode for the symbol degrees Celcius
plt.title("CRU_Monsoon_Temp")
plt.annotate('Data - CRU TS v4.02',(-178,-88),fontsize=6)

###################################################################################################################################
########### plot non-monsoon #####
plt.subplot2grid((1,2), (0,1)) # the location of the data
cru_nonmon = "CRU_Non-Monsoon_temp.nc" # the location of the data
data = Dataset(cru_nonmon)
temp_nonmon = data.variables['tmp'][:]
temp_av_nonmon = np.mean(temp_nonmon[:,:,:], axis = 0)

m = Basemap(projection='merc',llcrnrlon=45,llcrnrlat=10,urcrnrlon=120,urcrnrlat=55,resolution='h')
#map = Basemap(projection="cyl", resolution='c', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180) # set up the map using basemap
m.drawcoastlines(color="black") # add coastlines
m.drawparallels(np.arange(10, 55, 10), linewidth=0.5, dashes=[4, 1], labels=[1,0,0,0], fontsize=10, color='black')
m.drawmeridians(np.arange(45, 120,15),linewidth=0.5, dashes=[4, 1], labels=[0,0,0,1], fontsize=10, color='black')
m.drawcountries()

lons,lats = np.meshgrid(data.variables['lon'][:], data.variables['lat'][:]) # set the latitude and longitude variables from the data
x,y = m(lons, lats)
temp_plot = m.pcolormesh(x, y, temp_av_nonmon, cmap=cmaps.WhiteBlueGreenYellowRed) # plot the temperature data on the map
cb = m.colorbar(temp_plot, "bottom", size="5%", pad="2%", extend = 'both') # plotting a colour bar scale
cb.set_label(u"Temperature \u2103") # \u2103 is unicode for the symbol degrees Celcius
plt.title("CRU_Non_Monsoon_Temp")
#plt.annotate('Data - CRU TS v4.02')
plt.show() # show the map on screen
#plt.savefig('cruts_global.png') # save the figure with a user defined figure name


