/*
* (c) 2025 World Programming, an Altair Company.
*
* This file illustrates how to import and export XML data using
* the XMLMAP xmltype.
*
* This program imports XML from a non-generic XML structure.
* The Name, AccountType, and Town variables are read from the
* 7.1-CustomerAccounts.xml file.
* The AccountType variable is retained (RETAIN=yes) to ensure
* each Name receives the correct AccountType
*
* This program outputs the Customers dataset to the file
* 7.1-NameAndPhone.xml. Refresh the Samples project and open
* the XML file.
*/


FILENAME inmap 'Samples/7.1-ImportNames.map';
FILENAME inx 'Samples/7.1-CustomerAccounts.xml';

LIBNAME in XML XMLFILEREF=inx XMLMAP=inmap;

PROC CONTENTS DATA=in.CustDetails;
RUN;

PROC PRINT DATA=in.CustDetails;
RUN;


FILENAME outmap 'Samples/7.1-ExportNames.map';
FILENAME outx 'Samples/7.1-NameAndPhone.xml';

LIBNAME out XML XMLFILEREF=outx XMLMAP=outmap;

DATA customers;
    INPUT Name $ Phone;
DATALINES;
John 123456
Jane 100000
James 987654
;
RUN;


DATA out.Names;
    set work.customers;
RUN;