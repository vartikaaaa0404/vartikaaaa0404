#!/bin/bash
read -p "Enter basic salary: " basic
read -p "Enter HRA percentage: " hra_percent
read -p "Enter DA percentage: " da_percent

hra=$(( basic * hra_percent / 100 ))
da=$(( basic * da_percent / 100 ))
gross_salary=$(( basic + hra + da ))

echo "Gross Salary is $gross_salary"
