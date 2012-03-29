#!/bin/sh

python setup.py bdist_egg
cd doc
make html
cp -R build/html ../dist/doc
cd ..
