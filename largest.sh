#!/bin/bash
read -p "Enter first number: " num1
read -p "Enter second number: " num2
read -p "Enter third number: " num3

max=$num1
if (( num2 > max )); then max=$num2; fi
if (( num3 > max )); then max=$num3; fi

echo "Largest number is $max"
