#!/bin/bash

read -n1 -p "Do that? [y,n]" doit 
case $doit in  
  y|Y) echo yes ;; 
  n|N) echo no ;; 
  *) echo dont know ;; 
esac
