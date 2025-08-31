/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates how to read data from a file into a SAS
* language program in Altair SLC and use a SAS language macro
* to generate output.
*/


/* A macro to sort data and print output */
%MACRO filter(dept=,sortBy=);
	PROC SORT DATA = clothes OUT = sold;
		BY &sortBy;
		WHERE Department = "&dept";
	PROC PRINT DATA = sold;
		TITLE "Sales for &dept Department";
		FORMAT LastSoldDate WORDDATE18.;
%MEND filter;

/* Read the external data */
DATA clothes;
	INFILE 'Samples/5.1-Clothes.dat';
	INPUT Department $ 
		@8 LastSoldDate DDMMYY10. 
		@19 Clothing $9. 
		Quantity;
RUN;

/* Use the macro to generate output */
%filter(dept = Mens, sortBy = Quantity)
%filter(dept = Womens, sortBy = Clothing)
RUN;
