
import logging
from pathlib import Path
import pandas as pd

pd.options.display.max_columns = 900

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parents[1].absolute() / 'Assignment_1'


def read_csv_data(path_to_file):

    return pd.read_csv(str(DATA_DIR / path_to_file))
