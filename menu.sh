#!/bin/bash

while true; do
  echo "Menu:"
  echo "1. List of files"
  echo "2. Process Status"
  echo "3. Date"
  echo "4. Users in system"
  echo "5. Quit"
  read -p "Choose an option: " choice

  case $choice in
    1) ls ;;
    2) ps ;;
    3) date ;;
    4) who ;;
    5) exit ;;
    *) echo "Invalid option, please try again" ;;
  esac
done
