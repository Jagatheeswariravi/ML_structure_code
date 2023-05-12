import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : os.path.join("artifact","train.csv")
    test_data_path : os.path.join("artifact","test.csv")
    raw_data_path : os.path.join("artifact","raw_data.csv")







 