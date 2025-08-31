/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates how to read data from a CSV file into a
* SAS language program in Altair SLC.
*
* This program reads the file 4.1-Shops.csv and outputs the dataset
* to ODS LISTING.
*
* Workbench enables you to open any file listed in the Project
* Explorer view. Double click on the CSV file this program uses.
* If your PC has an application associated with csv files,
* Workbench launches the application.
*/


DATA shops;
   INFILE 'Samples/4.1-Shops.csv' DLM = ',' DSD MISSOVER;
   LENGTH ShopName $20.;
   INFORMAT Opened DDMMYY10.;
   INPUT ShopName Opened FirstYear SecondYear ThirdYear 
         FourthYear FifthYear;

PROC PRINT DATA = shops;
	FORMAT Opened DDMMYY10.;
	TITLE 'Number Of Coffee Shops';
RUN;
