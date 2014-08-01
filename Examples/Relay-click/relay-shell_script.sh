#!/bin/bash

cd /sys/class/gpio
echo 50 > export
echo 113 > export

cd gpio50
echo "out" > direction
cd ..

cd gpio113
echo "out" > direction
cd ..

cd gpio50
echo 1 > value
cd ..

cd gpio113
echo 1 > value
cd ..

cd gpio50
echo 0 > value
cd ..

cd gpio113
echo 0 > value
cd ..

cd gpio50
echo 1 > value
cd ..

cd gpio113
echo 1 > value
cd ..

cd gpio50
echo 0 > value
cd ..

cd gpio113
echo 0 > value
cd ..

cd gpio50
echo 1 > value
cd ..

cd gpio113
echo 1 > value
cd ..

cd gpio50
echo 0 > value
cd ..

cd gpio113
echo 0 > value
cd ..

cd gpio50
echo 1 > value
cd ..

cd gpio113
echo 1 > value
cd ..

cd gpio50
echo 0 > value
cd ..

cd gpio113
echo 0 > value
cd ..

cd gpio50
echo 1 > value
cd ..

cd gpio113
echo 1 > value
cd ..

cd gpio50
echo 0 > value
cd ..

cd gpio113
echo 0 > value
cd ..

cd gpio50
echo 1 > value
cd ..

cd gpio113
echo 1 > value
cd ..

cd gpio50
echo 0 > value
cd ..

cd gpio113
echo 0 > value
cd ..