/*
* (c) 2025 World Programming, an Altair Company.
*
* This example shows how to output results as a PDF file
* using ODS PDF.
*
* Ensure that the Altair Analytics Workbench preference
* "Automatically Manage Result Types" is enabled for PDF.
*
* The data step creates a dataset of random numbers and that
* dataset is passed to the UNIVARIATE procedure to produce a
* histogram of the data. The output is written to a PDF file by
* wrapping the procedure statements in ODS PDF statements to
* create and close the PDF stream.
*/


DATA input(DROP=i);
  DO i = 1 TO 1000;
    x = RAND('NORMAL', 0.0, 20.0);
    y = RAND('EXPONENTIAL');
    OUTPUT;
  END;
RUN;
 
ODS PDF FILE = "univariate_example.pdf";
PROC UNIVARIATE DATA = input;
  HISTOGRAM;
RUN;
ODS PDF CLOSE;


