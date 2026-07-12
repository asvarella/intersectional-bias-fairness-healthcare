# intersectional-bias-fairness-healthcare
A study on mitigating intersectional bias in healthcare-related data for ML models with focus on both pre-processing and in-processing methods

## Setup
This project runs with Python 3.12.13 in a virtual environment. All dependencies are listed in `requirements.txt`.

Create and activate a virtual environment, then install dependencies:
```
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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
