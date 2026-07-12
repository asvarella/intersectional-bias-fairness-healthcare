FROM continuumio/miniconda3:latest

WORKDIR /project

RUN conda install -y python=3.12.13 && \
    conda install -y -c conda-forge jupyter && \
    conda clean -afy

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/project"]
