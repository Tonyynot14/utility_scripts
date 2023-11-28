#!/bin/bash

#### running this with alias should set target for current terminal and any new terminals, helpful to target just one machine at a time in PEN test 
export target=$1
sed -i "s:^target=.*:target=$1:g" /home/kali/.zshrc
