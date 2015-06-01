# Media Website 
# Class to store information about different websites
# Each website is saved in a separate text file which is parsed into our list

from parse import *
import csv

# list of all parameters for a media website
media_website_params = ['title','type']

class MediaWebsite(object):

    def __init__(self, media_website_file):

        # create empty dictionary to store required information
        params = {}

        # open the file
        with open(media_website_file, 'r') as content_file:
            content = content_file.read()

            for param in media_website_params:
                result = search(param +': {}\n', str(content))

                if (result):
                    params[param] = result[0]

            print(params)


def main():
    MediaWebsite("media_website_test.txt")

main()