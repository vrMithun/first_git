/*
* (c) 2025 World Programming, an Altair Company.
*
* This example demonstrates how to use the ASSOCRULES procedure to
* mine association rules from a transaction dataset. This is the
* default mode of operation if the INEST option is not specified
* in the PROC ASSOCULES statement.
*
* For more about using the ASSOCRULES procedure, see the
* Altair SLC Reference for Language Elements.
*/

DATA TransactionData1;
  INFILE CARDS dlm='#';
  FORMAT Transactions 3.;
  FORMAT Items $10.;
  INPUT Transactions Items;
  CARDS;
1 # Cereal
2 # Bread
2 # Milk
2 # Eggs
3 # Crisps
3 # Jelly
3 # Sweets
3 # Balloons
4 # Balloons
4 # Crisps
4 # Jelly
5 # Milk
5 # Bread
6 # Milk
6 # Cereal
7 # Bacon
7 # Bread
7 # Milk
7 # Eggs
8 # Bacon
8 # Sausages
9 # Milk
;
RUN;

PROC ASSOCRULES OUTEST=transoplib DATA=TransactionData1 
                MODE=WPL MINSUPPORT=1 MINLIFT=4.0 RULESTOPRINT=10
                SORTBY=(LIFT) PRINTCONFIDENCE PRINTLIFT;
     OUTPUT OUT=outputlib;
RUN;