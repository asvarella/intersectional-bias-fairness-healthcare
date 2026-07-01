"""
generalized function with steps applied to fetch target datasets
"""

from ucimlrepo import fetch_ucirepo

def fetch_dataset_and_prepare_data(dataset_id):
    target_dataset = fetch_ucirepo(id=dataset_id)

    X = target_dataset.data.features
    y = target_dataset.data.targets

    # print assets
    print(target_dataset.metadata)
    print(target_dataset.variables)
    
    return X,y
