# New-York-Times-new-clue-generator

A program that generates new clues for New York Times Mini crossword puzzle. The entire code in written in Python. 

The task was to generate new clues for New York Times Mini crossword puzzle. To complete it, the solution to each clue was used as a search parameter on different online dictionaries and initially the definitions as taken as clues. Selenium and BeautifulSoup4 were used for Web scraping.

The online dictionaries used were:

cambridge dictionary
lexico.com
wordnet 
dictionary.com
merriam webbster

A rule based system which considered the length of the clue, similarity to original clue etc was used to select the best clue. The algorithm also involved elements of Depth First Search to select the best clue from the options. After the best clue was selected the results were shown in a GUI made using Tkinter.
