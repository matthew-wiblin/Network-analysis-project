#!/bin/bash

echo "Compiling cpp packet analyser"
sudo g++ -o main main.cpp -lpcap

echo "running program"
sudo ./main