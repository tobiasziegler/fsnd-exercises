import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/tobiasziegler/Projects/udacity/fsnd/fsnd-exercises/1-programming-fundamentals-and-the-web/05-use-classes/secret-message/prank")
    print(file_list)

    #(2) for each file, rename filename

rename_files()
