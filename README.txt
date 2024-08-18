Maeve Sunseri
Department of Social and Behavioral Sciences, Colorado Mesa University

A repository for MVSL, a project that analyzes the proportionality of election results.
While I wrote this program for my own research use, it might help somebody else out :]

MVSL.py:

This program requires a lot of specificity to work properly, but it isn't terribly complex.

To use this program, the user must have a previously written txt file that contains election party, vote, and results information.
To function properly, these absolutely MUST be formatted as follows:

Party 1: <Vote Total>
Party 2: <Vote Total>

Party 1: <Actual Seat Total>
Party 2: <Actual Seat Total>

The program works by first splitting the input file at \n\n, so there must be exactly one line of space between the vote and seat sections.
Next, the program splits each of these blocks into each line. As such, any empty lines aside from the one mentioned before *will* cause the program to not work as intended.
Next, each line is split wherever there is a ":" followed by a space. This means that there must be exactly one colon and space between a party name and vote/seat info.
A sample file is included with the program itself, titled "2024 UK General Election Outcome". Input file titles must follow this format: "<Year> <Country> <Election Type> Election Outcome.txt".

Running this program will generate a text file titled "<Year> <Country> <Election Type> Election Analysis.txt". 
This file will include a list of parties, the corresponding vote totals, the actual seat totals/election results, and the hypothetical seat totals that would result from the Sainte-Lague method applied in a single, national constituency.

Additionally, the program calculates and includes the Sainte-Lague Index (SLI), which measures the proportionality of an election, for both the actual and hypothetical vote/seat ratios. An SLI of 0 implies that an election is perfectly proportional (according to one definition of proportionality), while an SLI of 1 implies that an election is perfectly *disproportional*.

I will likely be adding to this project as needed for my own research :]