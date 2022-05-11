# Makefile for Data science bootcamp

help:
	@echo  -------------------------------------------------------------------------------------------
	@echo  make notebook - command to open notebooks folder in jupyter lab
	@echo  make notebook_save - command to save .ipynb files in notebooks folder
	@echo  make notebook_save_py - command to save .ipynb files as .py files in notebooks folder
	@echo  -------------------------------------------------------------------------------------------

notebook:
	jupyter lab notebooks/ > ./jupyterlab.log 2>&1 &

notebook_save:
	jupytext --to py notebooks/ml_bootcamp.ipynb

notebook_save_py:
	jupytext --output notebooks/ml_bootcamp.py notebooks/ml_bootcamp.ipynb

notebook_load:
	jupytext --to notebook notebooks/ml_bootcamp.py
