/*
* (c) 2025 World Programming, an Altair Company.
*
* This example uses the ASSOCRULES procedure to generate matches
* from a previously saved association rules dataset and a new
* transaction dataset. This mode of operation is invoked with
* the INEST option.
*
* For more about using the ASSOCRULES procedure, see the
* Altair SLC Reference for Language Elements.
*/

DATA ALevels2017;
  INFILE CARDS dlm='#';
  FORMAT Transactions $10.;
  FORMAT Items $20.;
  INPUT Transactions Items;
  DATALINES;
John     # Physics
John     # Maths
John     # ComputerScience
Jane     # English
Jane     # History
Jane     # Art
Julia    # Chemistry
Julia    # Biology
Julia    # Business
Jennifer # Physics
Jennifer # Maths
Jennifer # Chemistry
Jake     # Music
Jake     # Art
James    # English
James    # History
Joanna   # French
Joanna   # German
Joanna   # Art
Joe      # Cooking
Joe      # Sport
Jasper   # Maths
Jasper   # FurtherMaths
Jasper   # Physics
Julian   # Maths
Julian   # Physics
Julian   # Chemistry
;
RUN;


PROC ASSOCRULES OUTEST=alevelR DATA=ALevels2017 MODE=WPL MINSUPPORT=1 
     MINLIFT=4.0 RULESTOPRINT=10 SORTBY=(LIFT) PRINTCONFIDENCE 
     PRINTLIFT;
  OUTPUT OUT=AlevelM2017;
RUN;       

DATA ALevels2018;
  INFILE CARDS dlm='#';
  FORMAT Transactions $10.;
  FORMAT Items $20.;
  INPUT Transactions Items;
  DATALINES;
Simon     # Physics
Simon     # Maths
Simon     # ComputerScience
Sophie    # English
Sophie    # History
Sophie    # Art
Samantha  # Chemistry
Samantha  # Biology
Samantha  # Business
Stephanie # Physics
Stephanie # Maths
Stephanie # Chemistry
Stephen   # Music
Stephen   # Art
Sam       # English
Sam       # History
Sarah     # French
Sarah     # German
Sarah     # Art
Sebastien # Cooking
Sebastien # Sport
Steve     # Maths
Steve     # FurtherMaths
Steve     # Physics
Susan     # Maths
Susan     # Physics
Susan     # Chemistry
;
RUN;

PROC ASSOCRULES DATA=ALevels2018 PRINTCONFIDENCE INEST=alevelR;
  OUTPUT OUT=AlevelM2018;
RUN;