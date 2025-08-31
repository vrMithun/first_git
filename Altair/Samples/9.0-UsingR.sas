/*
* (c) 2025 World Programming, an Altair Company.
*
* This example shows how to use the R procedure in Altair SLC.
*
* Ensure that you have an operational R installation on the system
* on which you will be running this SAS language program.
*
* The R installation must have support for the 'shared library'
* interface.
*
* For more about using the R procedure, see the
* Altair SLC Reference for Language Elements.
*/


/* Set R_HOME */
options SET=R_HOME "C:\Program Files\R\R-3.5.1";

/* Return the version of R */
PROC R;
  SUBMIT;
    R.version
  ENDSUBMIT;
run;


/* Passing data between Altair SLC and R */


data source;
  do x=1 to 10;
    y=ranuni(-1);
    output;
  end;


PROC R;
  EXPORT DATA=source;
  SUBMIT;
    str(source)
    print(source)
  ENDSUBMIT;
RUN; 


PROC R;
  SUBMIT;
    x <- (1:10)
  ENDSUBMIT;
  IMPORT R=x;
  
PROC PRINT DATA=x;
RUN;


/* Generate some graphics with R */
DATA source;
  DO x=1 TO 10;
    y=RANUNI(-1);
  OUTPUT;
  END;

PROC R;
  EXPORT DATA=source;
  SUBMIT;
    model <- lm(source$y ~ source$x)  
    print(model)
    par(mfrow=c(2, 2)) 
    plot(model)
  ENDSUBMIT;
RUN;
