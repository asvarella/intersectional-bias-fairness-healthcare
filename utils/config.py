"""
constants and parameters
"""

# absolute path for outputs, experiments and so on
from pathlib import Path
ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / "data"



'''
Dataset constants and configuration
'''

# 1. AIDS
DATASETS = {
    "AIDS" : {
        "dataset_name": "AIDS",
        "sensitive_attrs": ["race", "gender", "homo"],
        "secondary_attrs": ["age_group"],
        "target_col": "target",
        "favorable_label": 0,
        "processed_csv_file": "6_aids_pp.csv",
        "min_sub_count": 60
    },
}
