"""
Cutplace is a tool to validate that tabular data stored in CSV, Excel, ODS
and PRN files conform to an interface definition (CID).

Additionally to the command line tool the functionality of cutplace is also
accessible through a Python API.
"""
import pkg_resources

from cutplace.errors import Location
from cutplace.interface import Cid
from cutplace.ranges import Range
from cutplace.validio import Reader, Writer, validate, rows

#: Package version information.
__version__ = pkg_resources.get_distribution("ytec-cutplace").version

#: Public classes and functions.
__all__ = [
    'Cid',
    'Location',
    'Range',
    'Reader',
    'Writer',
    'validate',
    'rows',
    '__version__'
]
