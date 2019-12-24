# MyBusinessCardParser
Contains the Project: Business Card Parser that extracts the name, phone number, and email of the Business Card

# Testing 
In order for this Project to run follow these steps at the command line or Python interpreter:
  1. A virtual environment needs to be created<br/> 
     apt-get install python3-venv<br/>
     python3 -m venv env #env can be called anything 
  2. Activate and install Spacy<br/>
      source ./env/bin/activate<br/>
      pip install spacy
  3. Download Model for Spacy<br/>
      python -m spacy download en_core_web_sm
 
 
 Download and Copy BusinessCardParser.py, BusinessCard1.txt, BusinessCard2.txt, BusinessCard3.txt
 to env(Or whatever it has been named)
 
 Then BusinessCardParser.py can now be run using python in the virtual enviroment
 
 The Program will prompt for the text to be inputted and the name, phone, and email will be extracted
