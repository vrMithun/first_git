/*
* (c) 2025 World Programming, an Altair Company.
*
* This example demonstrates how to output a sample dataset to a
* JSON format file.
*
* Two files are created from the input dataset:
* - The first file contains the dataset with no modification.
* - The second file contains output grouped by team and the
*   EXPORT statement selects only the data that applies to
*   the selected team.
*
*  Before running the program, please change <file-path> in the
*  OUT option on the PROC JSON statements to a relevant location
*  on your computer.
*
* For more about using the JSON procedure, see the
* Altair SLC Reference for Language Elements.
*/

DATA 'prem17_18'n;
  INFILE CARDS dlm='#';
  FORMAT Home Away $18.;
  FORMAT HS AS WORDS.;
  INFORMAT PlayedOn YYMMDD.;
  FORMAT PlayedOn DATE11.;
  INPUT Home Away HS AS PlayedOn;
  CARDS;
Liverpool         # Manchester City   # 4 # 3 # 2018-01-14
Liverpool         # Manchester United # 0 # 0 # 2017-10-14
Liverpool         # Tottenham Hotspur # 2 # 2 # 2018-02-03
Manchester City   # Liverpool         # 5 # 0 # 2017-09-09
Manchester City   # Manchester United # 2 # 3 # 2018-04-07
Manchester City   # Tottenham Hotspur # 4 # 1 # 2017-12-16
Manchester United # Liverpool         # 2 # 1 # 2018-01-10
Manchester United # Manchester City   # 1 # 2 # 2017-12-09
Manchester United # Tottenham Hotspur # 1 # 0 # 2017-10-24
Tottenham Hotspur # Liverpool         # 4 # 1 # 2017-10-24
Tottenham Hotspur # Manchester City   # 1 # 3 # 2018-04-14
Tottenham Hotspur # Manchester United # 2 # 0 # 2018-01-30
;
RUN;

PROC JSON OUT='<file-path>/results.json' PRETTY;
  EXPORT _LAST_;
RUN;

PROC JSON OUT = '<file-path>/results-by-division.json' PRETTY NOSASTAGS;
  WRITE OPEN OBJECT;
    WRITE VALUES 'premier league';
    WRITE OPEN OBJECT;
      WRITE VALUES 'liverpool';
      EXPORT _LAST_ (WHERE=(HOME='Liverpool'));
      WRITE VALUES 'Manchester City';
      EXPORT _LAST_ (WHERE=(HOME='Manchester City')) / FMTNUMERIC;
    WRITE CLOSE;
  WRITE CLOSE;
RUN;