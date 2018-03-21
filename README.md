### SaleSavant Web Scraping Exercise
##### By Simon Zhang
##### (832) 857-3826
##### simonczhang@gmail.com

In this exercise I write a Python script to parse out all the Kennet Investment Team members from the page. Then I find the ones that are living in the Bay Area and ones living in London.

Run the script in command line or terminal and the results will be printed.


##### SideNote
Below is the exact text instructions for the exercise I received:
1. Build a python app that scrapes the Kennet team website (www.kennet.com) and is able to parse out the names and titles of the people who live in the Bay Area vs. team members in London.

The instructions are a bit unclear as to whether to parse out all members first, or to only parse out the Bay Area and London members. I opted to parse out names, title, and location for all members, then looks for the ones in Bay Area and ones in London. The reason I did decided to grab all members first is that it could be useful to add all members to a database in the future.

If the instructions intended for me to only parse out the selected locations, I would have just written a conditional statement when looking at the location and only grab the Bay Area and London members and leave the members from other locations out.
