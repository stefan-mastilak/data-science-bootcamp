----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

### Jupyter notebooks:
  
   * to run jupyter notebook use:
      * venv terminal - jupyter notebook
      * makefile - on terminal type: make notebook
    

   * Shortcuts:
      * shift + enter >> to run a code on current line(cell) in notebook
      * esc >> to escape from editing mode
      * enter >> to go back to editing mode
      * m >> to switch from code writing mode to markdown writing mode 
      * y >> to switch from the markdown writing mode t code writing mode 
      * shift + tab >> inside bracket of function will show you documentation string of the function

     
### Jupyter tips for warnings and debugging:

```python
# to ignore warnings:
import warnings
warnings.filterwarnings('ignore')

# to revert ignore warnings:
warnings.filterwarnings('default')

# to show sklearn version and its dependencies:
import sklearn
sklearn.show_versions()
```
