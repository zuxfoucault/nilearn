"""
Plotting tools in nilearn
==========================

Nilearn comes with a set of plotting functions for an easy visualization of
Nifti-like images types such as statistical maps overlayed on anatomical
images or overlayed on glass brain image, anatomical images, functional/EPI
images, region specific mask images.

See :ref:`plotting` for more details.
"""

###############################################################################
# First, we retrieve the data from nilearn: haxby dataset to have EPI images
# and masks, and localizer dataset to have contrast maps

# Import datasets module
from nilearn import datasets

haxby_dataset = datasets.fetch_haxby(n_subjects=1)

# print basic information on the dataset
print('First subject anatomical nifti image (3D) is at: %s' %
      haxby_dataset.anat[0])
print('First subject functional nifti image (4D) is at: %s' %
      haxby_dataset.func[0])  # 4D data

haxby_anat_filename = haxby_dataset.anat[0]
haxby_mask_filename = haxby_dataset.mask_vt[0]
haxby_func_filename = haxby_dataset.func[0]

localizer_dataset = datasets.fetch_localizer_contrasts(
    ["left vs right button press"],
    n_subjects=2,
    get_anats=True,
    get_tmaps=True)
localizer_anat_filename = localizer_dataset.anats[1]
localizer_tmap_filename = localizer_dataset.tmaps[1]

###############################################################################
# Plotting statistical maps using function `plot_stat_map`

# Import plotting module
from nilearn import plotting

# Visualizing t-map image on subject specific anatomical image with manual
# positioning of coordinates using cut_coords given as a list
plotting.plot_stat_map(localizer_tmap_filename, bg_img=localizer_anat_filename,
                       threshold=3, title="plot_stat_map",
                       cut_coords=[36, -27, 66])

###############################################################################
# Plotting statistical maps on glass brain image using function `plot_glass_brain`

# Now, t-map image is overlayed on glass brain image as fixed background
plotting.plot_glass_brain(localizer_tmap_filename, title='plot_glass_brain',
                          threshold=3)

###############################################################################
# Plotting anatomical images using function `plot_anat`

# Visualizing anatomical image of haxby dataset
plotting.plot_anat(haxby_anat_filename, title="plot_anat")

###############################################################################
# Plotting ROIs (here the mask) using function `plot_roi`

# Visualizing ventral temporal region image from haxby dataset overlayed on
# subject specific anatomical image with coordinates positioned automatically on
# region of interest (roi)
plotting.plot_roi(haxby_mask_filename, bg_img=haxby_anat_filename,
                  title="plot_roi")

###############################################################################
# Plotting EPI image using function `plot_epi`

# Import image processing tool
from nilearn import image

# compute mean of the functional image from haxby dataset in t dimension.
# Basically reducing the functional image from 4D to 3D
mean_haxby_img = image.mean_img(haxby_func_filename)

# Visualizing mean image (3D)
plotting.plot_epi(mean_haxby_img, title="plot_epi")

plotting.show()
