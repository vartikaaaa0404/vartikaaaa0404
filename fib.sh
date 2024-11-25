#!/bin/bash
read -p "Enter the number of terms: " n
a=0
b=1

echo -n "Fibonacci series: $a $b"
for (( i=2; i<n; i++ )); do
  fn=$((a + b))
  echo -n " $fn"
  a=$b
  b=$fn
done
echo
