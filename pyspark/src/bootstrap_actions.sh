#!/usr/bin/env bash

# install conda
wget --quiet https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O ~/anaconda3.sh \
    && /bin/bash ~/anaconda3.sh -b -p $HOME/conda

echo -e '\nexport PATH=$HOME/conda/bin:$PATH' >> $HOME/.bashrc && source $HOME/.bashrc


# Install PySpark
conda install -y pyspark

# Install additional packages
conda install -y ipython jupyter

# Install PyArrow for Apache Arrow support
pip install pyarrow

# Install Optimus for data processing and formatting
pip install optimuspyspark