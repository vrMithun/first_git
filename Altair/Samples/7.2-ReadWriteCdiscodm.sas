/*
* (c) 2025 World Programming, an Altair Company.
*
* This example demonstrated how to import from a file using xmltype
* CDISCODM.
*
* This program imports XML from the file 7.2-Patients.xml and
* exports a simple patient dataset to the file 7.2-PatientData.xml
*/


FILENAME fn 'Samples/7.2-Patients.xml';
LIBNAME in XML XMLFILEREF=fn XMLTYPE=CDISCODM;

PROC CONTENTS DATA = in.PD;
RUN;
PROC PRINT DATA = in.PD;
RUN;

FILENAME fn 'Samples/7.2-PatientData.xml';
LIBNAME outp XML xmltype=cdiscodm XMLFILEREF=fn;

DATA PD;
	LENGTH 		__STUDYOID
				__METADATAVERSIONOID
				__SUBJECTKEY
				__STUDYEVENTOID
				__STUDYEVENTREPEATKEY
				__FORMOID
				__FORMREPEATKEY
				__TRANSACTIONTYPE
				__ITEMGROUPOID $ 100;
	RETAIN 		__STUDYOID				"Studyid"
				__METADATAVERSIONOID	"MDV1.0"
				__SUBJECTKEY			"1"
				__STUDYEVENTOID			"1"
				__STUDYEVENTREPEATKEY	"1"
				__FORMOID				"formid"
				__FORMREPEATKEY			"1"
				__TRANSACTIONTYPE		"Snapshot"
				__ITEMGROUPOID			"PD";
	LENGTH 		__ITEMGROUPREPEATKEY $ 100;
				__ITEMGROUPREPEATKEY = trim(left(_n_));
	INPUT		name $ age;
	DATALINES;
John 21
Jane 23
James 33
;
RUN;

DATA outp.PD;
	SET PD;
RUN;
