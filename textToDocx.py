# This file takes a text file provided by the user
# And converts it to a .docx file allowing the user 
# open in word easily. 

from docx import Document
import os

<<<<<<< HEAD
text_file = input("Please provide path pointing to your textfile: ")
=======
text_file = "your_text_file_path.txt"
>>>>>>> 7ebc59d74f146640ac898cb0eb7dbcfdb04a22c2

# opens document to add text to
document = Document()

# adds the entire contents of file to a list that will
# then be used to add to the document we just created
fileContents = []
for line in open(text_file):
    fileContents += line

# adds all the text we just added to fileContents to the document as a paragraph
paragraph = document.add_paragraph(fileContents)

# gets .txt file extention to replace for renaming to .docx
text_file_ext = os.path.splitext(text_file)[1].lower()

# updates path & filename for for .docx format
new_filename = os.path.basename(text_file).replace(text_file_ext, '.docx')
new_path = os.path.split(text_file)[0]
new_docx_file_path = new_path + "/" + new_filename

# saves the document with all the under the name of the 
# original text file name
document.save(new_docx_file_path)
print("New .docx document created & saved.")
