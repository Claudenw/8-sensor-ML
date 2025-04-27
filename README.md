# 8-sensor-ML

A machine learning model to using 8 binary sensors based
on [Donald Michie](https://en.wikipedia.org/wiki/Donald_Michie)'
s [MENACE](https://opendatascience.com/menace-donald-michie-tic-tac-toe-machine-learning/) design.

## Concept

The concept is to build an ML model system that tracks 8 bump sensors placed at the 4 edges and 4 corners of a mobile
platform with independent left and right drive mechanisms.

Each motor has 3 states (off, forward, reverse) which can be encoded as
`b00`, `b01` and `b10`. Shifting the encoding for one of the motors two bits to the left and we have the following

 State | Left          | Right         
 -------|---------------|---------------
 b0000 | off           | off           
 b0001 | off           | forward       
 b0010 | off           | reverse       
 b0100 | forward       | off           
 b1000 | reverse       | off           
 b1111 | no preference | no preference 

Each sensor will be represented by a neuron in an ML network. Each neuron will indicate which of 6 possible motor states
is acceptable.

The output from each neuron will be logically`AND`ed with the output of all the other neurons to indicate which actions
are acceptable.

The bitmap in the table is then decompsed into the two outputs, one for each motor. In the case where the output is "no
preference" either a random selection is made or the previous state is continued.