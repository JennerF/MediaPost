# Post to the Interwebs

import MediaWebsite





def getUserDesiredMediaType():
	response = input("Please select the desired media type by number: 1. Video  2. Image  3. Audio \n")

	if (response.isdigit()) and (1 <= int(response) <= 3):
		return int(response)
	else:
		print("Please select a value of 1, 2, or 3. \n")
		return getUserDesiredMediaType()

def getDesiredMediaList():
	desired_media = getUserDesiredMediaType()
	desired_websites = filterMediaType(desired_media)
	return desired_websites


def filterMediaType(media_selection):
	if (media_selection == 1):
		filtered_list = filterWebsites('video')
	elif (media_selection == 2):
		filtered_list = filterWebsites('image')
	else:
		filtered_list = filterWebsites('audio')

	return filtered_list


def filterWebsites(media_type):
	website_list = MediaWebsite.populateWebsiteList()
	desired_website_list = []

	for website in website_list:
		if website.type() == media_type:
			desired_website_list.append(website)

	return desired_website_list




