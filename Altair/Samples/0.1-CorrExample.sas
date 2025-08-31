/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates some of the plotting
* capabilities using the CORR procedure.
*
* This program performs a correlation analysis using a random
* dataset representing height, hand and foot lengths in male and
* female subjects.
*/

data StatureData;
DO i = 1 TO 100;
IF (i lt 45) THEN DO;
	gender = 'F';
	height = 1600 + RANNOR(213)*49.2353284;
	handlength = 189.58 + RANNOR(53)*9.3349677;
	footLength = 234.7493333+ RANNOR(2134)*12.1144918;
	OUTPUT;
	END;
ELSE DO;
	gender = 'M';
	height = 1750 + RANNOR(2213)*61.2736962;
	handlength = 208.77 + RANNOR(153)*9.2076838;
	footLength = 262.5562500 + RANNOR(24134)*12.4232412;
	OUTPUT;
	END;
END;
RUN;

ODS GRAPHICS ON;

PROC CORR DATA=StatureData PLOTS=(MATRIX(HIST) SCATTER);
  BY gender;
  VAR height handlength footLength;
RUN;

ODS GRAPHICS OFF;