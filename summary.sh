#!/bin/bash

echo "-----------------------------------------------"
passed=0
total=0
for group in results/*
do
  group=${group#results/}
  _passed=`wc -l results/$group/PASS | awk '{print $1}'`
  _total=`wc -l results/$group/{PASS,FAIL,WARN,NOSUPPORT,CRASH,TIMEOUT} | \
    tail -n 1 | awk '{print $1}'`
  echo $group $_passed $_total | \
    awk '{printf "%-20s: %6d / %6d -> %5.1f%%\n", $1, $2, $3, 100.0*$2/$3}'
  let passed+=$_passed
  let total+=$_total
done

echo "-----------------------------------------------"
echo $passed $total | \
  awk '{printf "Total tests passed  : %6d / %6d -> %5.1f%%\n", $1, $2, 100.0*$1/$2}'
echo "-----------------------------------------------"
