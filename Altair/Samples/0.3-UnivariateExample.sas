/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates some of the plotting
* capabilities using the UNIVARIATE procedure.
*
* This program performs univariate analysis on measurements of the
* depth of the River Test, in Romsey, UK, where sluice gates are
* installed to regulate the water flow.
*/


DATA TestRiverHeight;
  LABEL Depth="Depth in cm";
  INPUT Depth @@;
  DATALINES;
90 87 90 93 70 53 30 52 67 74 74 74
72 73 65 64 64 65 64 65 66 67 68 72
72 71 70 69 68 67 66 68 67 64 61 58
60 60 60 60 59 56 49 48 46 45 61 64
61 55 53 56 55 52 66 66 57 57 50 55
56 54 56 54 55 50 60 60 58 56 53 50
49 46 57 57 56 55 56 58 59 48 46 44
44 47 42 43 42 39 48 43 42 43 44 44
46 39 44 47 49 57 46 49 55 41 51 49
54 65 61 61 55 62 58 63 60 66 55 65
68 64 71 62 56 66 61 59 61 59 57 57
56 53 53 60 56 65 45 45 44 52 52 53
RUN;

ODS GRAPHICS ON;

PROC UNIVARIATE DATA=TestRiverHeight;
  VAR Depth;
  HISTOGRAM;
  QQPLOT;
RUN;

ODS GRAPHICS OFF;