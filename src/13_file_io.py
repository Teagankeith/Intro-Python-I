"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

foofile = open("foo.txt", "r")
with open("foo.txt") as foofile:
    file_contents = foofile.read()
    print(file_contents)
foofile.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

barfile = open("bar.txt", "w")
barfile.write("Content one")
barfile.write("Content two ")
barfile.write("Content three ")
barfile.close()
with open("bar.txt") as barfile:
    file_contents = barfile.read()
    print(file_contents)
