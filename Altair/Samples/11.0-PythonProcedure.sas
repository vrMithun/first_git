/*
* (c) 2025 World Programming, an Altair Company.
*
* This example shows how to use the PYTHON procedure.
* The Python procedure supports Python version 3.4 or higher.
*
* Datasets are passed from Altair SLC to Python as a 
* pandas DataFrame.
* 
* You must have the pandas package and its prerequistes installed.
* To run this program, you require the statsmodel Python package.
*
* The data step creates a dataset of random numbers that is passed
* to Python for linear regression ordinary least squares test. The
* resultant parameters are printed through Python and are displayed
* in the output defined in the SAS language program.
*
* When run through Workbench, the parameters will typically be in
* HTML output. When run on the command line, the
* parameters will typically be displayed in the print file.
*
* For more about using the PYTHON procedure, see the
* Altair SLC Reference for Language Elements.
*/

DATA source;
  DO x=1 TO 10;
    y =RANUNI(-1);
    z =RANUNI(1);
    OUTPUT;
  END;
RUN;

PROC PYTHON;
  EXPORT DATA=source;
  SUBMIT;
import statsmodels.formula.api as lm
result = lm.ols(formula='x ~ y + z', data=source).fit()
print (result.params)
  ENDSUBMIT;
RUN;