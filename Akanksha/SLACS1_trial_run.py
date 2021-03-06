"""
Pipelines: Light Parametric + Mass Light Dark + Source Parametric
=================================================================

By chaining together three searches this script  fits `Imaging` dataset of a 'galaxy-scale' strong lens, where in the final model:

 - The lens galaxy's light is a parametric `EllSersic`.
 - The lens galaxy's stellar mass distribution is tied to the light model above.
 - The lens galaxy's dark matter mass distribution is a `SphNFW`.
 - The source galaxy's light is a parametric `EllSersic`.
"""

from pyprojroot import here
from os import path
import autofit as af
import autolens as al
import autolens.plot as aplt

"""
__Dataset + Masking__

Load, plot and mask the `Imaging` data.
"""
workspace_path = str(here())
dataset_path = path.join(workspace_path, "Akanksha","SLACS1_new")

imaging = al.Imaging.from_fits(
    image_path=path.join(dataset_path, "image.fits"),
    noise_map_path=path.join(dataset_path, "noise_map.fits"),
    psf_path=path.join(dataset_path, "psf.fits"),
    pixel_scales=0.05,
)

mask = al.Mask2D.circular_annular(
    shape_native=imaging.shape_native,
    pixel_scales=imaging.pixel_scales,
    inner_radius=0.25,
    outer_radius=1.6,
)
#mask = al.Mask2D.circular(
#    shape_native=imaging.shape_native, pixel_scales=imaging.pixel_scales, radius=3.0
#)

imaging = imaging.apply_mask(mask=mask)

imaging_plotter = aplt.ImagingPlotter(imaging=imaging)
imaging_plotter.subplot_imaging()

"""
__Paths__

The path the results of all chained searches are output:
"""
path_prefix = path.join(workspace_path, "Akanksha","SLACS1_output")

"""
__Redshifts__

The redshifts of the lens and source galaxies, which are used to perform unit converions of the model and data (e.g.
from arc-seconds to kiloparsecs, masses to solar masses, etc.).

In this analysis, they are used to explicitly set the `mass_at_200` of the elliptical NFW dark matter profile, which is
a model parameter that is fitted for.
"""
redshift_lens = 0.2803
redshift_source =  0.9818

"""
__Model + Search + Analysis + Model-Fit (Search 1)__

In search 1 we fit a lens model where:

 - The lens galaxy's light is a parametric `EllSersic` bulge [7 parameters].

 - The lens galaxy's mass and source galaxy are omitted.

The number of free parameters and therefore the dimensionality of non-linear parameter space is N=11.
"""
model = af.Collection(
    galaxies=af.Collection(
        lens=af.Model(al.Galaxy, redshift=redshift_lens, bulge=af.Model(al.lp.EllSersic))
    )
)

"""
Positions taken from positons.json file
"""

positions = al.Grid2DIrregular.from_json(
    file_path=path.join(workspace_path, "Akanksha", "slacs_new","slacs0252+0039", "positions.json")
)

visuals_2d = aplt.Visuals2D(positions=positions)

imaging_plotter = aplt.ImagingPlotter(imaging=imaging, visuals_2d=visuals_2d)
imaging_plotter.subplot_imaging()

settings_lens = al.SettingsLens(positions_threshold=1.0)

search = af.DynestyStatic(
    path_prefix=path_prefix,
    name="search_1_EllSersic",
    unique_tag='SLACS1',
    nlive=50,
)

#analysis = al.AnalysisImaging(dataset=imaging)
analysis = al.AnalysisImaging(
    dataset=imaging, positions=positions, settings_lens=settings_lens
)

result_1 = search.fit(model=model, analysis=analysis)

"""
__Model + Search + Analysis + Model-Fit (Search 2)__

We use the results of search 1 to create the lens model fitted in search 2, where:

 - The lens galaxy's light and stellar mass is a parametric `EllSersic` bulge [parameters fixed to result of
 search 1].

 - The lens galaxy's dark matter mass distribution is a `EllNFWMCRLudlow` whose centre is aligned with the
 `EllSersic` bulge and stellar mass model above [3 parameters].

 - The lens mass model also includes an `ExternalShear` [2 parameters].

 - The source galaxy's light is a parametric `EllSersic` [7 parameters].

The number of free parameters and therefore the dimensionality of non-linear parameter space is N=12.

NOTES:

 - By using the fixed `bulge` model from the result of search 1, we are assuming this is a sufficiently accurate fit
 to the lens's light that it can reliably represent the stellar mass.
"""
bulge = result_1.instance.galaxies.lens.bulge

dark = af.Model(al.mp.SphNFW)
dark.centre = bulge.centre
dark.mass_at_200 = af.LogUniformPrior(lower_limit=1e8, upper_limit=1e15)
dark.redshift_object = redshift_lens
dark.redshift_source = redshift_source

model = af.Collection(
    galaxies=af.Collection(
        lens=af.Model(
            al.Galaxy,
            redshift=redshift_lens,
            bulge=bulge,
            dark=af.Model(al.mp.SphNFW),
            shear=al.mp.ExternalShear,
        ),
        source=af.Model(al.Galaxy, redshift=redshift_source, bulge=al.lp.EllSersic),
    )
)

search = af.DynestyStatic(
    path_prefix=path_prefix,
    name="search_2_SphNFW",
    unique_tag=dataset_name,
    nlive=75,
)

#analysis = al.AnalysisImaging(dataset=imaging)

analysis = al.AnalysisImaging(
    dataset=imaging, positions=positions, settings_lens=settings_lens
)

result_2 = search.fit(model=model, analysis=analysis)

"""
__Model + Search + Analysis + Model-Fit (Search 3)__

We use the results of searches 1 and 2 to create the lens model fitted in search 3, where:

 - The lens galaxy's light and stellar mass is a parametric `EllSersic` bulge [8 parameters: priors initialized
 from search 1].

 - The lens galaxy's dark matter mass distribution is a `EllNFWMCRLudlow` whose centre is aligned with the
 `EllSersic` bulge and stellar mass model above [3 parameters: priors initialized from search 2].

 - The lens mass model also includes an `ExternalShear` [2 parameters: priors initialized from search 2].

 - The source galaxy's light is a parametric `EllSersic` [7 parameters: priors initialized from search 2].

The number of free parameters and therefore the dimensionality of non-linear parameter space is N=22.

Notes:

 - This search attempts to address any issues there may have been with the bulge's stellar mass model.
"""
bulge = result_1.model.galaxies.lens.bulge

dark = result_2.model.galaxies.lens.dark
dark.centre = bulge.centre

model = af.Collection(
    galaxies=af.Collection(
        lens=af.Model(
            al.Galaxy,
            redshift=redshift_lens,
            bulge=bulge,
            dark=dark,
            shear=result_2.model.galaxies.lens.shear,
        ),
        source=af.Model(
            al.Galaxy, redshift=redshift_source, bulge=result_2.model.galaxies.source.bulge
        ),
    )
)

search = af.DynestyStatic(
    path_prefix=path_prefix,
    name="search_3_EllSersic",
    unique_tag=dataset_name,
    nlive=75,
)

#analysis = al.AnalysisImaging(dataset=imaging)
analysis = al.AnalysisImaging(
    dataset=imaging, positions=positions, settings_lens=settings_lens
)

result_3 = search.fit(model=model, analysis=analysis)

"""
Finish.
"""
