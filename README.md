Small Genshi set up for the generation of
various products which require unit information
from the 5.1 OME schema.

Steps
-----
- `conda env create -f environment.yml`
- If necessary, `python omesym/run.py --python > equations.py`
- `make DIR=/opt/omero-build all move`
