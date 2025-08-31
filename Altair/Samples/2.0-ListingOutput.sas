/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates how to to generate ODS output to all
* automatically-managed output types. You can modify the managed
* types from the Results page of the Preferences dialog box.
*
* Use the Output Explorer view to open the resulting ODS output.
* Use the Server Explorer view to open the resulting 'employees'
* dataset from the Work library of the server on which this
* example is invoked.
*/

/* Generate some sample data*/
DATA employees;
LENGTH Name $10 Age 3 Job $15;
INPUT Name $ Age Job $;
DATALINES;
Beth 41 Sales-Manager
Steve 32 Sales
William 35 Accounts
Anne 28 Marketing
Dawn 26 Sales
Andrew 36 Support
;

/* Use the sample data in ODS output */
PROC SORT DATA = employees; 
  BY name;
RUN;

PROC PRINT DATA = employees noobs;
RUN; 

TITLE 'Employees in Company X';
