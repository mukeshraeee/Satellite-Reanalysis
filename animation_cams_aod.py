""" Creat gif cams_aod """

from pathlib import Path
import imageio
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt, animation
from IPython.display import HTML, display
import moviepy.editor as mp
import ffmpy


file = xr.open_dataset('data.nc')
# = Bring longitude coordinates onto a [-180,180] grid
file_assigned = file.assign_coords(longitude=(((file.longitude + 180) % 360) - 180)).sortby('longitude')
# retrieve the data variable  AOD at 550nm as xarray.DataArray

aod = file_assigned.aod550

#=== Get long name and units
long_name = aod.long_name
units     = aod.units
#== get lat lon
lats  = aod.latitude
lons = aod.longitude


#=== This create figures on different time
for i in range(120):
         aod[i,:,:].plot(figsize = (6,3))
         plt.title("Time = " + str(aod.coords['time'].values[i])[:13])
         plt.savefig(f"/mnt/e/sentinel_training/cams_excercise/cams_aod_fig/cams_aod_01_frame_{i:04}.png")
         plt.close()

#== Now create gif using figures =======
image_path = Path('/mnt/e/sentinel_training/cams_excercise/cams_aod_fig/')
images = list(image_path.glob('*.png'))
image_list = []
for file_name in images:
         image_list.append(imageio.imread(file_name))
imageio.mimwrite('cams_aod_new11.gif', image_list)


#=== GIF to MP4 conversion
f = ffmpy.FFmpeg(inputs={'cams_aod_new11.gif': None},outputs={'cams_aod.mp4': None})
ff.run()
