# intersectional-bias-fairness-healthcare
A study on mitigating intersectional bias in healthcare-related data for ML models with focus on both pre-processing and in-processing methods

## Setup
This project runs in a conda environment with Python 3.12.13 installed. All other dependencies are listed in `requirements.txt` file.

Set up conda environment with this Python version and run the command below to install dependencies:
```
pip install requirements.txt
```

## Running on Docker

Build the image:
```
docker build -t intersectional-bias-healthcare .
```

Run the container:
```
docker run -p 8888:8888 -v $(pwd):/project intersectional-bias-healthcare
```

The `-v $(pwd):/project` flag mounts your local directory into the container so changes to notebooks and files persist on your machine.

Once running, open the URL printed in the terminal (e.g. `http://127.0.0.1:8888/?token=...`) in your browser to access Jupyter.
