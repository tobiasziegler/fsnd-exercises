def read_text():
    quotes = open("/Users/tobiasziegler/Projects/udacity/fsnd/fsnd-exercises/1-programming-fundamentals-and-the-web/08-use-classes-profanity-editor/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
