#!/bin/bash

sudo apt-get install python3-venv
python3 -m venv BusinessCardReader

source ./BusinessCardReader/bin/activate
pip install spacy
python -m spacy download en_core_web_sm
