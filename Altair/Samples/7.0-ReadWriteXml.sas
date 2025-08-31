/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates how to Import and export xml using
* the GENERIC xmltype.
*
* The program reads the file 7.0-Customer.xml and outputs a dataset
* to the 'In' library. Use the Server Explorer view to open the
* resulting dataset.
*
* The CUSTOMER dataset is output to the file
* 7.1-ExportXml.xml. Refresh the Samples project and open
* the XML file.
*/


FILENAME inf 'Samples/7.0-Customer.xml';
LIBNAME in XML XMLFILEREF = inf XMLTYPE = GENERIC;

PROC DATASETS LIBRARY = in;

PROC CONTENTS DATA = in.customer;
RUN;

PROC PRINT DATA = in.customer;
RUN;


FILENAME outf 'Samples/7.1-ExportXml.xml'; 
LIBNAME outlib XML XMLFILEREF = outf XMLTYPE = GENERIC;

DATA CUSTOMER;
    INPUT Name $ Phone;
DATALINES;
John 123456
Jane 100000
James 987654
;
RUN;

DATA outlib.customer;
    set work.customer;
RUN;
