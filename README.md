# Belvedere Glacier Long-term Monitoring Open Data

## Creators and Contributors

- Ioli, Francesco<sup>1</sup>
- De Gaetani, Carlo<sup>1</sup>
- Barbieri, Federico<sup>1</sup>
- Gaspari, Federica<sup>1</sup>
- Pinto, Livio<sup>1</sup>
- Rossi, Lorenzo<sup>1</sup>

**Project members:**

- Bianchi, Alberto<sup>1</sup>
- Cina, Alberto<sup>2</sup>
- De Michele, Carlo<sup>1</sup>
- Maschio, Paolo<sup>2</sup>
- Passoni, Daniele<sup>1</sup>

<details>
<summary>Affiliations</summary>
1.  Department of Civil and Environmental Engineering, Politecnico di Milano (Italy)
2.  Department of Environment, Land and Infrastructure Engineering, Politecnico di Torino (Italy)
</details>

## Introduction

This dataset contains extensive, long-term monitoring data on the Belvedere Glacier, a debris-covered glacier located on the east face of Monte Rosa in the Anzasca Valley of the Italian Alps. The data is derived from photogrammetric 3D reconstruction of the full Belvedere Glacier and includes:

- **dense point clouds** obtained with Structure-from-Motion (SfM) covering the entire glacier body
- high-resolution **orthophotos**
- high-resolution **DEMs**

Since 2015, in-situ surveys of the glacier have been conducted annually using fixed-wing UAVs (until 2020) and quadcopters (2021-2022) to remotely sense the glacier and build high-resolution photogrammetric models. GCPs were established across the glacier and surveyed with topographic-grade GNSS receivers (Ioli et al., 2022).

For the period from 1977 to 2001, historical analog images, acquired from aerial platforms and digitized with photogrammetric scanners, were used in combination with GCPs obtained from recent photogrammetric models (De Gaetani et al., 2021).

## Belvedere Glacier

The Belvedere Glacier is an important temperate alpine glacier located on the east face of Monte Rosa in the Anzasca Valley of Italy. The Belvedere Glacier is of particular importance among alpine glaciers because it is a debris-covered glacier and it reaches its lowest elevation at about 1800 m a.s.l. Over the last century, the Belvedere Glacier has experienced extraordinary dynamics, such as a surge-like movement or the formation of a supraglacial lake, which seriously threatened the nearby community of Macugnaga.

## Data Organization

The data are organized by year in compressed zip folders named belvedere_YYYY.zip, which can be downloaded independently. Each folder contains all data available for that year (i.e. photogrammetric point clouds, orthophotos and DEMs) and the corresponding metadata. Metadata is provided as a .json file which contains all the main information for data usage. Point clouds are saved in compressed las format (.laz) and they can be inspected e.g., with CloudCompare. Orthophotos and DEMs are georeferenced images (.tif) that can be inspected with any GIS software (e.g., QGIS).

Large point clouds are subdivided into regular tiles, which are numbered with a progressive row-wise order from the bottom-left corner of the point cloud bounding box.

All the files are named according to the following naming schema:

"belv_YYYY_surveyplatform_datatype[\_resolution][vertical_datum][-tile_number].extension"

where:

- YYYY: is the year of the survey
- surveyplatform: can be either "uav" for the UAV-based photogrammetry survey or "histo" for the historical aerial datasets.
- datatype: can be either "pcd" for point clouds, "orthophoto" for orthophotos and "dsm" for DSMs.
- resolution: on-ground resolution of each pixel in meters. This applies only to raster data (orthophoto and DSMs)
- vertical_datum: if the DSM is given in orthometric coordinates, a label "ortho" is present in the filename, otherwise the height of the dataset is supposed to be ellipsoidical.
- tile: tile number, if the data is tiled to avoid large files.

## Data Usage

This dataset can be used to estimate glacier velocities, volume variations, study geomorphological processes such as the process of moraine collapse, or derive other information on glacier dynamics. If you have any requests on the data provided, data acquisition, or on the raw data themselves, you are encouraged to contact us.

## Contributions

The monitoring activity carried out on the Belvedere Glacier was designed and conducted jointly by the Department of Civil and Environmental Engineering (DICA) of Politecnico di Milano and the Department of Environment, Land and Infrastructure Engineering (DIATI) of Politecnico di Torino.

**If you use the data, please cite these publications:**

- Ioli, F., Dematteis, N., Giordan, D., Nex, F., Pinto, L., Deep Learning Low-cost Photogrammetry for 4D Short-term Glacier Dynamics Monitoring. PFG (2024). [https://doi.org/10.1007/s41064-023-00272-w](https://doi.org/10.1007/s41064-023-00272-w)
- Ioli, F.; Bianchi, A.; Cina, A.; De Michele, C.; Maschio, P.; Passoni, D.; Pinto, L. Mid-Term Monitoring of Glacier’s Variations with UAVs: The Example of the Belvedere Glacier. Remote Sensing, 14, 28 (2022). [https://doi.org/10.3390/rs14010028](https://doi.org/10.3390/rs14010028)
- De Gaetani, C.I.; Ioli, F.; Pinto, L. Aerial and UAV Images for Photogrammetric Analysis of Belvedere Glacier Evolution in the Period 1977–2019. Remote Sensing, 13, 3787 (2021). [https://doi.org/10.3390/rs13183787](https://doi.org/10.3390/rs13183787)
