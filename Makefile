# Makefile for Data science bootcamp

notebook:
	jupyter lab notebooks/ > ./jupyterlab.log 2>&1 &

notebook_save:
	jupytext --to py notebooks/ml_bootcamp.ipynb

notebook_save_py:
	jupytext --output notebooks/ml_bootcamp.py notebooks/ml_bootcamp.ipynb

notebook_load:
	jupytext --to notebook notebooks/ml_bootcamp.py
