/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates how to output a dataset to ODS HTML.
*
* Use the Output Explorer view to open the resulting HTML output.
*/

/* Use this sample data */
DATA vehicles;
LENGTH Vehicle $10 Repaired 3 Maintenance $15;
INPUT Vehicle $ Repaired Maintenance $;
DATALINES;
Saloon 7 Exhaust
Sports 2 Service
Sports 6 Body-Work
Saloon 3 Body-Work
4-Door 12 Major-Repair
Sports 10 Minor-Repair
4-Door 5 Service
Pick-Up 3 Minor-Repair
;

/* Produce some frequency and MEANS output */
PROC FREQ DATA = vehicles;
	TABLE Maintenance;
	TITLE 'Monthly Vehicle Maintenance Report';
RUN;

PROC SORT DATA = vehicles;
	BY Maintenance;
RUN;
    
PROC MEANS DATA = VEHICLES;
	BY Maintenance;
RUN;
