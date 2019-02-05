#!/bin/sh

# Script to compile targeted source codes and run the compiled binary.
# The command supports upto 5 source files and compile flags as arguments.
#
# $./runtest.sh source1.cpp source2.cpp source3.cpp source4.cpp
#
# Add -DDEBUG like below to enable debug messages
# $./runtest.sh source1.cpp source2.cpp source3.cpp source4.cpp -DDEBUG

g++ $1 $2 $3 $4 $5 -std=c++11 && ./a.out