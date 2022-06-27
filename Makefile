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
	jupytext --output notebooks/notebooks_py/pandas_introduction.py notebooks/pandas_introduction.ipynb
	jupytext --output notebooks/notebooks_py/pandas_exercises.py notebooks/pandas_exercises.ipynb
	jupytext --output notebooks/notebooks_py/numpy_introduction.py notebooks/numpy_introduction.ipynb
	jupytext --output notebooks/notebooks_py/numpy_exercises.py notebooks/numpy_exercises.ipynb
	jupytext --output notebooks/notebooks_py/matplotlib_introduction.py notebooks/matplotlib_introduction.ipynb
	jupytext --output notebooks/notebooks_py/matplotlib_exercises.py notebooks/matplotlib_exercises.ipynb
	jupytext --output notebooks/notebooks_py/sklearn_introduction.py notebooks/sklearn_introduction.ipynb
	jupytext --output notebooks/notebooks_py/sklearn_workflow.py notebooks/sklearn_workflow.ipynb

notebook_load:
	jupytext --to notebook notebooks/notebooks_py/pandas_introduction.py
	jupytext --to notebook notebooks/notebooks_py/pandas_exercises.py
	jupytext --to notebook notebooks/notebooks_py/numpy_introduction.py
	jupytext --to notebook notebooks/notebooks_py/numpy_exercises.py
	jupytext --to notebook notebooks/notebooks_py/matplotlib_introduction.py
	jupytext --to notebook notebooks/notebooks_py/matplotlib_exercises.py
	jupytext --to notebook notebooks/notebooks_py/sklearn_workflow.py
	jupytext --to notebook notebooks/notebooks_py/sklearn_introduction.py
