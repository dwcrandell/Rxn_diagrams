Rxn_diagrams.py README
Created by Doug Crandell - Indiana University 2013

A simple script to draw a reaction energy diagram using bezier curves.  Enter relative energies (in kcal/mol) of all minima and maxima on the potential energy surface from the command line.

For example the following generates the diagram shown in the sample figure in the folder.

python rxn_diagrams.py 0 10 5 13 6 8 2

The diagram starts with an intermediate at set at 0 and passes through a transition state 10 kcal/mol higher in energy relative to that intermediate to produce a intermediate at 5 kcal/mol and so forth.}
