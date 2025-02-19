# Advanced NLP Code Examples

This is a repository of code examples for the 2021 edition of CMU CS 11-711
[Advanced NLP](http://phontron.com/class/anlp2021/).

## 1. Create an environment with dependencies specified in env.yml:
    conda env create -f env.yml

## 2. Activate the new environment:
    conda activate cs224n
    
## 3. Inside the new environment, install IPython kernel so we can use this environment in jupyter notebook: 
 
    ```
    python -m ipykernel install --user --name cs224n
    ```


## 4. Homework 1 (only) is a Jupyter Notebook. With the above done you should be able to get underway by typing:

    ```
    jupyter notebook --ip=127.0.0.1 xxx.ipynb
    ```
    
## 5. To make sure we are using the right environment, go to the toolbar of exploring_word_vectors.ipynb, click on Kernel -> Change kernel, you should see and select cs224n in the drop-down menu.

## To deactivate an active environment, use
    conda deactivate