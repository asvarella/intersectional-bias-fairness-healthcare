"""
Parameterized data path
"""

# absolute path for outputs, experiments and so on
from pathlib import Path
ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / "data"
RAW_DATA_PATH = DATA_PATH / "raw"
PROCESSED_DATA_PATH = DATA_PATH / "processed"

'''
Dataset constants and configuration
'''

DATASETS = {
    "AIDS" : {
        "dataset_name": "AIDS",
        "sensitive_attrs": [
            "race", 
            "gender", 
            "homo"
            ],
        "secondary_attrs": ["age_group"],
        "target_col": "target",
        "favorable_label": 0,
        "processed_csv_file": "6_aids_pp.csv",
        "min_sub_count": 60
    },
    "MENTAL" : {
        "dataset_name": "MENTAL HEALTH",
        "sensitive_attrs": [
            "gender", 
            "non_cis"
            ],
        "secondary_attrs": [
            "is_europe_or_north_america",
            "age_group"
            ],
        "target_col": "target",
        "favorable_label": 0,
        "processed_csv_file": "mental_health_pp.csv",
        "min_sub_count": 45
    }
}
