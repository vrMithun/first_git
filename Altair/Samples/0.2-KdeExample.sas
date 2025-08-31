/*
* (c) 2025 World Programming, an Altair Company.
*
* This example illustrates some of the plotting
* capabilities using the KDE procedure.
*
* This program generates a mixture of Gaussian distributions and
* performs univariate and bivariate kernel density estimation.
*/


DATA GaussMixtureData;
DO i=1 TO 900;
	SELECT;
	 WHEN(i lt 250) DO;
			x1 = RANNOR(231)*0.5 - 2.0;
			x2 = RANNOR(421)*0.5 + 3.0;
		END;
	WHEN(i lt 600) DO;
			x1 = RANNOR(231) + 0.5;
			x2 = RANNOR(421) + 3.0;
		END;
	OTHERWISE DO;
			x1 = RANNOR(231) + 0.5;
			x2 = RANNOR(421) - 2.0;
		END;
	END;
	OUTPUT;
END;
RUN;

ODS GRAPHICS ON;

PROC KDE DATA = GaussMixtureData;
UNIVAR x1 x2 / OUT=univoutput METHOD=OS PLOTS=(HISTDENSITY);
BIVAR x1 x2 / OUT=bivoutput BIVSTATS PLOTS=(SCATTER CONTOURSCATTER);
RUN;

ODS GRAPHICS OFF;