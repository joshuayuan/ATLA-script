#ATLA Script Parser#
By Joshua Yuan.

##Inspiration##
Since the 4th grade I've been super into Avatar the Last Airbender. I would rewatch episodes, act out scenes, study the [Avatar Wikia](http://avatar.wikia.com/wiki/Avatar_Wiki). At one point, I discovered [this website](atla.avatarspirit.net/transcripts.php) which had the scripts for all the episodes, and more. This was my new goto website because now I could memorize the quotes precisely. 

A few years ago, I became paranoid that one day the site might go down and I would lose access to the scripts, so I thought of manually copy and pasting the contents into a document, or of manually saving the html, but these were inefficient and excessive actions, so I decided realized the best way to go about this would be to write a script which could visit each page and save the html automatically.

January 2017 I decided to stop procrastinating and just write this program.

##How it works##
The function *generateURLs* creates a list of strings formatted like "http://atla.avatarspirit.net/transcripts.php?num=" and appended with a book and episode number. For example, "http://atla.avatarspirit.net/transcripts.php?num=305" corresponds to the script for Book 3, Episode 5. 

Then, the function *openPages* iterates through that list generated from the previous function, and calls the *writeHtmlToFile* function, passing the html for each page and a title string as arguments. *writeHtmlToFile* scans the whole html string for "<blockquote>" and "</blockquote>" substrings and saves the content between those two tags into a new file in the *scripts* folders.

Open the file in browser - Tada! 