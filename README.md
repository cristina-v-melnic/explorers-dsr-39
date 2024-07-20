# explorers-dsr-39

## Overview

This is a development of solution for the ["DengAI: Predicting Disease Spread"](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/) competition as coursework in the [Data Science Retreat](https://datascienceretreat.com/) Batch-39. 

Authored by Julien Henry and Cristina Melnic 

## How to install dependencies
1. Create a new conda environment and install python.

```
conda create -n <env-name>

conda activate <env-name>

conda install python=3.12
```

2. To install the required packages run:

```
pip install -r requirements.txt
```

3. To open and run the notebooks, run additionally:
```
pip install ipykernel

python -m ipykernel install --user --name <YOUR ENVIRONMENT> --display-name <YOUR ENVIRONMENT DISPLAY NAME>
```    
After the installation you can start a local notebook server:
```
jupyter notebook
```
Make sure to select the above created kernel to run the notebooks.


## Getting the best results
Our best result can be reproduced by running all the cells in the following notebook:
```
notebooks\<notebook_name>
```

Upon running all the contents, an ouput file in the submission format will appear in the same folder.
To submit the solution to the competition upload the output file.
