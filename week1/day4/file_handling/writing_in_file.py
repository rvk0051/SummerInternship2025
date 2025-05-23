'''
Writing to a File

Writing to a file is done using file.write() which writes the specified string to the file.
If the file exists, its content is erased. If it doesn't exist, a new file is created.

'''
# Example:
file = open("python.txt", "w")  # file can't be read due to 'w' mode
file.write("Hello, World!")  # all the previous content is erased
file.close()

'''
Writing to a File in Append Mode (a)

It is done using file.write() which adds the specified string to the end of the file 
without erasing its existing content.

'''
# Example:
file = open('python.txt', 'a+')
file.write("This will add this line")
file.close()
