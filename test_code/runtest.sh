#!/bin/sh

# Script to compile targeted source codes and run the compiled binary.
# The command supports upto 4 source files as arguments.
#
# $./runtest.sh source1.cpp source2.cpp source3.cpp source4.cpp

g++ $1 $2 $3 $4 -std=c++11 && ./a.out