/*
* (c) 2025 World Programming, an Altair Company.
*
* This example demonstrated how to use multi-byte characters
* in a SAS language program.
*
* Ensure the server startup option ENCODING is set to UTF8 on the
* Altair SLC server on which this program is invoked.
*
* Use the Output Explorer view to open the resulting HTML output.
*/


/* Use this sample Data with some Japanese fish names*/
DATA fish; 
  LENGTH Name $10 Caught 3;
  INPUT Name $ Caught;
  DATALINES;
Mackerel 123
Shark 2
Pike 12
マグロ 12
;
RUN;

/* Generate some output */
PROC SORT DATA = fish;
  BY NAME;
RUN;
 
TITLE 'Fish that We Caught';
TITLE2 '私たちは、つかまえた魚';

PROC PRINT DATA = fish NOOBS; 
RUN;
