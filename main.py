import os
import csv
import sys
import fileinput

class Books:
	"""
	Class that defines a book object with its title, author, year
	of pubblication, editor, position in bookshelf and whether or
	not the book has been lent or is missing.
	"""
	def __init__(self, author, title, year_of_publ, editor, position,author_nationality, language, genre,
		lent=False, missing=False, read=False, rating=-1, comment=''
		):
		self.author = author
		self.title = title
		self.year_of_publ = year_of_publ
		self.editor = editor
		self.position = position
		self.author_nationality	= author_nationality
		self.language = language
		self.genre = genre
		self.lent = lent
		self.missing = missing
		self.read = read
		self.rating = rating
		self.comment = comment
		

	def getTitle(self):
		return	self.title

	def getAuthor(self):
		return self.author

	def getYearOfPublication(self):
		return self.year_of_publ

	def getEditor(self):
		return self.editor

	def getPositionInShelf(self):
		return self.position

	def isLent(self):
		return self.lent

	def isMissing(self):
		return self.missing

	def lendingBook(self):
		self.lent = True

	def lostBook(self):
		self.missing = True

	def returningBook(self):
		self.lent = False

	def foundBook(self):
		self.missing = False

	def readBook(self):		
		self.read = True
	
	def getReadStatus(self):
		return self.read

	def getRating(self):
		return self.rating

	def getComment(self):
		return self.comment

	def getAuthorNationality(self):
		return self.author_nationality

	def getLanguage(self):
		return self.language

	def getGenre(self):
		return self.genre

	def setRating(self, newrating):
		self.rating = newrating

	def setComment(self, newcomment):
		self.comment = newcomment

	def __str__(self):
		return "Books[author=" + self.author + \
		"title=" + self.title + \
		",year_of_publ=" + self.year_of_publ + \
		",editor=" + self.editor + \
		",position=" + self.position + \
		",author_nationality=" + self.author_nationality + \
		",language=" + self.language + \
		",genre=" + self.genre + \
		",lent=" + str(self.lent) + \
		",missing=" + str(self.missing) + \
		",read=" + str(self.read) + \
		",rating=" + str(self.rating) + \
		",comment=" + str(self.comment) +\
		"]"

def insert_book():
	new_book = []
	author = input("Insert author of the book (last name first) ")
	title = input("Type title of the book: ")
	year_p = input("Type year of pubblication: ")
	editor = input("Type editor: ")
	position = input("Position in bookshelf: ")
	author_national = input("What\'s the author nationality? ")
	language_book = input("What language is the book written? ")
	book_genre = input("What is the genre of the book? ")
	lent = False
	missing = False
	read_status = input("Have you read this book? [Y/n] ")
	if (read_status == "Y" or read_status == 'y'):
		read_status = "True"
	else:
		read_status = "False"
	rating_status = input("If yes how would you rate it from 1 to 5? (Press Enter if you have not read it yet): ")
	comment_status = input("Would you like to add a note or comment about this book? Type it here or press Enter to continue: ")
	
	new_book.append(author)
	new_book.append(title)
	new_book.append(year_p)
	new_book.append(editor)
	new_book.append(position)
	new_book.append(author_national)
	new_book.append(language_book)
	new_book.append(book_genre)
	new_book.append(lent)
	new_book.append(missing)
	new_book.append(read_status)
	new_book.append(rating_status)
	new_book.append(comment_status)
	
	return new_book

def write_book_to_collection(l):
	# Open a file
	path = "/Users/franco/PythonProjects/PythonExer/lib.csv"
	with open(path,'a') as file:
		for i in l:
			file.write("%s," % i)
		file.write("\n")
			#file.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))
	# Close opend file
	file.close()

def search_book(myBookslist):
	found = False
	name_of_book = input("Type the title of the book: ")
	for i in myBookslist:
		if name_of_book in i.getTitle():
			print ("")
			print ("* * * The book {} by {} was found in shelf {} *  * *".format(name_of_book,
			 i.getAuthor(), i.getPositionInShelf()))
			print ("You rated this book {} out of 5".format(i.getRating()))
			if (i.getReadStatus() == 'True'):
				print ("and you have already read it.")
			else:
				print ("as you haven\'t read it yet.")
			print ("")
			if (i.isLent() == "True"):
				print ("The book has been lent. ")
				print ("")
			if (i.isLent() == "False"):
				#print ("The book has not been lent. ")
				print ("")
			if (i.isLent() == "False" and i.isMissing() == "True"):
				print ("It looks like the book has not been lent but is not in your bookshelf")
			if (i.isMissing() == "True"):
				print ("I\'m sorry, but the book is missing from your bookshelf and it may be lost. ")
				print("")
			else:
				print ("")
			found = True
	if not found:
		print ("Book not found in library")

def input_lent_book_title():
	return  input("Type the title of the book you have lent: ")

def input_missing_book_title():
	return  input("Type the title of the book that is missing: ")

def input_returning_book_title():
	return  input("Type the title of the book you has been returned: ")

def input_found_book_title():
	return  input("Type the title of the book that has been found: ")

def input_read_book_title():
	return  input("Type the title of the book that you have just read: ")

def input_rate_book_title():
	return  input("Type the title of the book that you want to rate: ")

def input_comment_book_title():
	return  input("Type the title of the book that you want to comment or add a note to: ")




def lent(myBookslist):
	global name_of_book_lent 
	name_of_book_lent = input_lent_book_title()
	for i in myBookslist:

		if name_of_book_lent in i.getTitle():
			i.lendingBook()

def missing_b(myBookslist):
	global name_of_book_missing
	name_of_book_missing = input_missing_book_title()
	for i in myBookslist:

		if name_of_book_missing in i.getTitle():
			i.lostBook()

def returning_b(myBookslist):
	global name_of_book_returning
	name_of_book_returning = input_returning_book_title()
	for i in myBookslist:

		if name_of_book_returning in i.getTitle():
			i.returningBook()

def read_b(myBookslist):
	global name_of_book_read
	name_of_book_read = input_read_book_title()
	for i in myBookslist:

		if name_of_book_read in i.getTitle():
			i.readBook()

def rate_b(myBookslist):
	global name_of_book_rate
	name_of_book_rate = input_rate_book_title()
	global new_rate
	new_rate = input("How would you rate this book from 1 to 5?")
	for i in myBookslist:

		if name_of_book_rate in i.getTitle():
			i.setRating(new_rate) 

def comment_b(myBookslist):
	global name_of_book_comment
	name_of_book_comment = input_comment_book_title()
	global new_comment
	new_comment = input("Add your comment or not here: ")
	for i in myBookslist:

		if name_of_book_comment in i.getTitle():
			i.setComment(new_comment) 

def found_b(myBookslist):
	global name_of_book_found
	name_of_book_found = input_found_book_title()
	for i in myBookslist:

		if name_of_book_found in i.getTitle():
			i.foundBook()

def lentbooks(l):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_lent):
				i[8] = "True"
			print (i)
			fi.write(",".join(i))
			fi.write("\n")
	fi.close()	

def lostbooks(l):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_missing):
				i[9] = "True"
			print (i)
			fi.write(",".join(i))
			fi.write("\n")
	fi.close()	

def returningbooks(l):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_returning):
				i[8] = "False"
			print (i)
			fi.write(",".join(i))
			fi.write("\n")
	fi.close()	

def foundbooks(l):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_found):
				i[9] = "False"
			print (i)
			fi.write(",".join(i))
			fi.write("\n")
	fi.close()

def readbooks(l):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_read):
				i[10] = "True"
			print (i)
			fi.write(",".join(i))
			fi.write("\n")
	fi.close()

def ratebooks(l, new_rating):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_rate):
				i[11] = new_rating
			print (i)
			fi.write(",".join(i)) # Aggiungere exception in ogni write 
			fi.write("\n")        #perche' ogni volta che c'e' un errore, ad esempio
	fi.close()		#prova a sostituire new_rating con new_comment sopra, si cancella il database

def commentbooks(l, new_comment):
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'w') as fi:
		for i in l:
			if (i[1]==name_of_book_comment):
				i[12] = new_comment
			print (i)
			fi.write(",".join(i))
			fi.write("\n")
	fi.close()
#def sort_books(l):

#Main function
def main():
	open('/Users/franco/PythonProjects/PythonExer/lib.csv', 'a').close()
	print ("Welcome to your bookshelf management program!")
	print ("********************************************")
	print ("")
	print ("********************************************")
	running = True
	other_options = True
	myBooks = []
	books_list = []
	with open('/Users/franco/PythonProjects/PythonExer/lib.csv') as f:
			reader = csv.reader(f)
			for row in reader:
				#print (row)
				myBooks.append(Books(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
					row[7], row[8], row[9], row[10], row[11], row[12]))
				books_list.append(row)
	while (running and other_options):
		
		print ("How can I help? ")
		print ("")
		print ("1) Show all my books        2) Insert new book        3) Search for books")
		print ("4) Set book as lent         5) Set book as missing    6) Set book as returning")
		print ("7) Set book as found        8) Set book as read       9) Rate book")
		print ("10) Add comment or note     11) Show Stats and Plots  Type q to quit ") 
		option = input("> ")
		counter = 1
		if (option == "1"):
			with open('/Users/franco/PythonProjects/PythonExer/lib.csv') as f:
				reader = csv.reader(f)
				#lines reader.readlines()
				for row in sorted(reader):
#					row.sort()
					print (str(counter) +") " + row[0] + ", " + row[1])
					counter += 1
			another_op1 =input("Would you like to do something else? [Y/n]: ")
			if (another_op1 == 'Y' or another_op1 == 'y'):
				print ("")
			elif (another_op1 == 'N' or another_op1 == 'n'):
				print ("Quitting the program.")
				option == 'q'
				other_options = False
			else:
				print ("Invalid option. Please type Y or n: ")
				another_op1 =input()
		elif (option == "2"):
		
			book = insert_book()
			write_book_to_collection(book)
			another_op2 =input("Would you like to do something else? [Y/n]: ")
			if (another_op2 == 'Y' or another_op2 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False
		
		elif (option == "3"):
			search_book(myBooks)
			another_op3 =input("Would you like to do something else? [Y/n]: ")
			if (another_op3 == 'Y' or another_op3 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False
		elif (option == "4"):
			lent(myBooks)
			lentbooks(books_list)
			another_op4 =input("Would you like to do something else? [Y/n]: ")
			if (another_op4 == 'Y' or another_op4 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False
		elif (option == "5"):
			missing_b(myBooks)
			lostbooks(books_list)
			another_op5 =input("Would you like to do something else? [Y/n]: ")
			if (another_op5 == 'Y' or another_op5 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False
		elif (option == "6"):
			returning_b(myBooks)
			returningbooks(books_list)
			another_op6 =input("Would you like to do something else? [Y/n]: ")
			if (another_op6 == 'Y' or another_op6 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False
		elif (option == "7"):
			found_b(myBooks)
			foundbooks(books_list)
			another_op7 =input("Would you like to do something else? [Y/n]: ")
			if (another_op7 == 'Y' or another_op7 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False

		elif (option == '8'):
			read_b(myBooks)
			readbooks(books_list)
			another_op8 =input("Would you like to do something else? [Y/n]: ")
			if (another_op8 == 'Y' or another_op8 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False

		elif (option == '9'):
			rate_b(myBooks)
			ratebooks(books_list, new_rate)
			another_op9 =input("Would you like to do something else? [Y/n]: ")
			if (another_op9 == 'Y' or another_op9 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False

		elif (option == '10'):
			comment_b(myBooks)
			commentbooks(books_list, new_comment)
			another_op10 =input("Would you like to do something else? [Y/n]: ")
			if (another_op10 == 'Y' or another_op10 == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False

		elif (option == '11'):
			print ('Show stats and plots')
			another_op11 =input("Would you like to do something else? [Y/n]: ")
			if (another_op11 == 'Y' or another_op11  == 'y'):
				print ("")
			else:
				print ("Quitting the program. ")
				option == 'q'
				other_options = False
		elif (option == "q"):
			running =False
		else:
			print ("Please type again. ")
	

	
	for i in range(len(myBooks)):
		print(myBooks[i])
		

if __name__ == "__main__":
	main()


