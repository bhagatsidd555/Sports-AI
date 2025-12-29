"""
Ingestion package
Handles loading and parsing of Garmin CSV and FIT files
"""

from .csv_loader import load_csv
from .fit_loader import load_fit
from .schema import GarminSchema
