#!/bin/bash

print_line='{printf "%-24s: %6d / %6d -> %5.1f%%\n", $1, $2, $3, 100.0*$2/$3}'

echo "---------------------------------------------------"
for group in results/*
do
  group=${group#results/}
  passed=`wc -l results/$group/PASS | awk '{print $1}'`
  total=`wc -l results/$group/{PASS,FAIL,WARN,NOSUPPORT,CRASH,TIMEOUT} | \
    tail -n 1 | awk '{print $1}'`
  echo $group $passed $total | awk "$print_line"
done

echo "---------------------------------------------------"
passed="`wc -l results/*/PASS | tail -n 1 | awk '{print $1}'`"
failed="`wc -l results/*/FAIL | tail -n 1 | awk '{print $1}'`"
crashed="`wc -l results/*/CRASH | tail -n 1 | awk '{print $1}'`"
timedout="`wc -l results/*/TIMEOUT | tail -n 1 | awk '{print $1}'`"
warned="`wc -l results/*/WARN | tail -n 1 | awk '{print $1}'`"
unsupported="`wc -l results/*/NOSUPPORT | tail -n 1 | awk '{print $1}'`"
total=$[passed+failed+crashed+timedout+warned+unsupported]
echo "Total tests passed,$passed,$total" | awk -F ',' "$print_line"
echo "Total tests failed,$failed,$total" | awk -F ',' "$print_line"
echo "Total tests crashed,$crashed,$total" | awk -F ',' "$print_line"
echo "Total tests timedout,$timedout,$total" | awk -F ',' "$print_line"
echo "Total tests warned,$warned,$total" | awk -F ',' "$print_line"
echo "Total tests unsupported,$unsupported,$total" | awk -F ',' "$print_line"
echo "---------------------------------------------------"
echo "Supported tests passed,$passed,$[total-unsupported]" | awk -F ',' "$print_line"
echo "---------------------------------------------------"
