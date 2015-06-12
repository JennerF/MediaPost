# Media Website 
# Class to store information about different websites
# Each website is saved in a separate text file which is parsed into our list

from parse import *
import csv
from glob import iglob
import sys
import os

# list of all parameters for a media website
media_website_params = ['title','type']

class MediaWebsite(object):

    def __init__(self, media_website_file):

        # create empty dictionary to store required information
        params = {}

        # open the file
        with open(os.path.join("websites" ,media_website_file), 'r') as content_file:
            content = content_file.read()

            for param in media_website_params:
                result = search(param +': {}\n', str(content))

                if (result):
                    params[param] = result[0]
                    
        self.params = params


    def type(self):
        return self.params["type"]

    def name(self):
        return self.params["name"]

    def url(self):
        return self.params["url"]


def populateWebsiteList():
    website_list = []
    relative_path = os.path.dirname(os.path.realpath(__file__)) + "\\websites"
    for file in os.listdir(relative_path):
        if file.endswith(".txt"):
            website_list.append(MediaWebsite(file))
    
    return website_list