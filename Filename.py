Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myfilename=input("Input file name: ")
Input file name: tricks.mp3
>>> myfilename.partition('.')
('tricks', '.', 'mp3')
>>> filename, separator, extension = myfilename.partition('.')
>>> print(extension)
mp3
>>> 