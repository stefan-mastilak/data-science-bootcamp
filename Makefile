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
	jupytext --to py notebooks/pandas_introduction.ipynb
	jupytext --to py notebooks/pandas_exercises.ipynb
	jupytext --to py notebooks/numpy_introduction.ipynb
	jupytext --to py notebooks/numpy_exercises.ipynb

notebook_save_py:
	jupytext --output notebooks/pandas_introduction.py notebooks/pandas_introduction.ipynb
	jupytext --output notebooks/pandas_exercises.py notebooks/pandas_exercises.ipynb
	jupytext --output notebooks/numpy_introduction.py notebooks/numpy_introduction.ipynb
	jupytext --output notebooks/numpy_exercises.py notebooks/numpy_exercises.ipynb

notebook_load:
	jupytext --to notebook notebooks/pandas_introduction.py
	jupytext --to notebook notebooks/pandas_exercises.py
	jupytext --to notebook notebooks/numpy_introduction.py
	jupytext --to notebook notebooks/numpy_exercises.py
