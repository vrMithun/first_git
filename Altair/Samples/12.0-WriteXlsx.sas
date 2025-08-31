/*
* (c) 2025 World Programming, an Altair Company.
*
* This example demonstrates how to output a sample dataset to an
* Excel worksheet.
*
* Data is read from the 4.1-Shops.csv file and output using the
* LIBNAME XLSX statement to a worksheet in the shops.xlsx file.
*/



/* Read this external file */
DATA shops;
   INFILE 'Samples/4.1-Shops.csv' DLM = ',' DSD MISSOVER;
   LENGTH ShopName $20.;
   INFORMAT Opened DDMMYY10.;
   INPUT ShopName Opened FirstYear SecondYear ThirdYear 
         FourthYear FifthYear;
RUN;

LIBNAME excel XLSX './shops.xlsx' REPLACE;

/* Create the output Sheet */
DATA excel.shops;
  SET shops;
RUN; 

PROC PRINT DATA = excel.shops;
RUN;
