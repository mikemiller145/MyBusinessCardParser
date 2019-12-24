#!/usr/bin/env python3

import re  # Allows Regular Expressions to be used
import os  # Checks for validity of file input
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
venv_dir = os.path.join(parent_dir, 'venv/Lib/site-packages/spacy')

sys.path.append(venv_dir)

import spacy  # imports Name Recognition Software called spacy

#  class for ContactInfo
class ContactInfo:
    def __init__(self, file):  # Constructor for Contact Info class with a file argument
        self.fullname = "N/A"  # Stores the full name from the businessCard
        self.phone = "N/A"  # Stores the Digits of the Business card's phone number
        self.email = "N/A"  # Stores the Email from the business car
        self.file = file  # Stores the Business Card Documents

    # Retrieves the full name from the Business Card
    def getName(self):
        file.seek(0)  # Resets the current position of the file back to the beginning
        nlp = spacy.load('en_core_web_sm')  # loads a English model to use to recognize different entities
        line = self.file.read()  # Assigns the file being read

        business_card_doc = nlp(line)  # creates the nlp object that will analyze the Business card file
        for ent in business_card_doc.ents:  # For loop that searches for each name entity
            if (ent.label_ == "PERSON"):  # If it is a person assign the text to fullname
                self.fullname = ent.text
                return self.fullname

        file.close()

    #  Retrieves the phone number from the Business Card
    def getPhoneNumber(self):
        file.seek(0)
        line = self.file.readline()
        while line:  # Regex for finding the line that has the correct phone number
            check = '^(Phone: |Tel: )?(\+1 )?(\()?[0-9]{3}(\)|\-)(\s)?[0-9]{3}-[0-9]{4}$'
            if (re.search(check, line)):
                self.phone = re.sub("\D", "",
                                    line)  # Takes the line found and extracts just the digits and assigns it to phone
                return self.phone

            line = file.readline()
        file.close()

    # Retrieves the email address from the business card
    def getEmailAddress(self):
        file.seek(0)
        line = file.readline()  # below, Regex for finding the line that has the correct email address
        check = '^[a-z]+([\.-]?[a-z]+)*@[a-z]+([\.-]?[a-z]+)*(\.[a-z]{2,3})+$'
        while line:
            if (re.search(check, line)):
                self.email = line  # finds line the with the email address and assigns it to email
                return self.email

            line = file.readline()
        file.close()


# Definition for the BusinessCardParser
class BusinessCardParser:
    def __init__(self):
        self.contact = "N/A"  # Stores ContactInfo object

    # Creates takes business card file as argument and creates ContactInfo object and returns
    def getContactInfo(self, file):
        contact = ContactInfo(file)
        return contact


# Asks user for input
print("Welcome to the Business Card Reader!")
businessCard = input("Please enter a valid file name: ")

# Checks to make sure a valid input file has been entered
while not os.path.exists(businessCard):
    print("Error! File does not exist please try again")
    businessCard = input("Please enter a valid file name: ")

#  Opens file
file = open(businessCard, "r")
#  Creates Business Card Parser Object
myBusinessParser = BusinessCardParser()
#  Create ContactInfo object
myContacts = myBusinessParser.getContactInfo(file)
#  Perform getName, getPhoneNumber, getEmailAddress
print("Name: " + myContacts.getName())
print("Phone: " + myContacts.getPhoneNumber())
print("Email: " + myContacts.getEmailAddress())
