import csv
from Linkedlist import LinkedList

#Create a list with all genres from CSV file
def genres():
    genre=[]
    with open(r"Libros resumidos en csv.csv") as file:
        next(file)
        for row in file:
            row = row.rstrip()
            col = row.split(";")  
            if col[3] not in genre:
                genre.append(col[3])  
    return genre

#Create a list of list with books information (Tittle, author, genre) from CSV file
def books():
    all_books=[]
    with open(r"Libros resumidos en csv.csv") as file:
        next(file)
        for row in file:
            row = row.rstrip()
            col = row.split(";")              
            sublist=[col[1], col[2], col[3]]
            all_books.append(sublist)      
    return all_books

#Function to insert genres into a data structure (LinkedList) 
def get_genre():
    list_of_genre= LinkedList()
    genre= []
    with open(r"Libros resumidos en csv.csv") as file:
        next(file)
        for row in file:
            row = row.rstrip()
            col = row.split(";")           
            if col[3] not in genre:
                genre.append(col[3])  
                list_of_genre.insert_beginning(col[3].lower())                
    return list_of_genre

#Function to insert books into a data structure (LinkedList of LinkedLists)
def insert_list_of_books():
    list_of_books= LinkedList()
    genre_list = genres() 
    all_books = books()
    for genre in genre_list:
        books_by_genre= LinkedList()
        for book in all_books:
            if book[2] ==genre:
                books_by_genre.insert_beginning(book) 
        list_of_books.insert_beginning(books_by_genre)
    return list_of_books 


genres_list = get_genre()
books_list = insert_list_of_books()


selected_genre = ""

#User interaction
print("\n")
print("*********************")
print("       WELCOME       ")
print("       TO  THE       ")
print("       LIBRARY       ")
print("*********************")
print("\n")

print("Hi!! Are you ready to start a new reading??")
print("Here you can find a list of the best books by genre.")
print("\n")
print("** GENRES **")
genre_list = genres()
for genre in genre_list:
    print("- " + genre)   

while len(selected_genre) == 0:    
    user_input = str(input(
        "\nWhat kind of book would you like to read?\nType the beginning of the genre and press enter to see if "
        "it's here.\n")).lower()
    
    # Search in genre_list based of user input
    matching_types = []
    genre_list_head = genres_list.get_head_node()
    
    while genre_list_head is not None:        
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_types.append(genre_list_head.get_value())
        genre_list_head= genre_list_head.get_next_node()        
    for genre in matching_types:
        print(genre)

    # Check how many books we have found
    if len(matching_types)==1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_types[0].upper() + ". \nDo you want to look at " +
            matching_types[0].upper() + " books? Enter Y/N \n")).lower()
        
        if select_type == "y" or select_type== "Y":
            selected_genre= matching_types[0]
            print("Selected book genre: "+ selected_genre.upper())
            book_list_head = books_list.get_head_node()            
            while book_list_head.get_next_node() is not None:
                sublist_head= book_list_head.get_value().get_head_node()                
                if sublist_head.get_value()[2].lower() == selected_genre:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[0])
                        print("Author: " + sublist_head.get_value()[1])
                        print("Genre: " + sublist_head.get_value()[2])                        
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                book_list_head = book_list_head.get_next_node()

            # Ask user if they would like to search for other types of books
            repeat_loop = str(input("\nDo you want to find other books? Enter Y/N \n")).lower()
            if repeat_loop == 'y'or repeat_loop=='Y':
                selected_genre = ""   

print("HAPPY READING!!")
