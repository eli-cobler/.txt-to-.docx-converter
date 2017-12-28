from docx import Document
import os

text_file = "/Users/elicobler/tiny_dancer/BackEnd/TextFiles/12.18.18 - Monday - Hr 2 - Seg 1.txt"

#opens document to add text to
document = Document()

#adds the entire contents to a list that we will
#then use to add to the document we just created
fileContents = []
for line in open(text_file):
    fileContents += line

#adds all the text we just created to the document as a paragraph
paragraph = document.add_paragraph(fileContents)

#gets .txt file extention to replace for renaming to .docx
text_file_ext = os.path.splitext(text_file)[1].lower()

#updates path & filename for for .docx format
new_filename = os.path.basename(text_file).replace(text_file_ext, '.docx')
new_path = os.path.split(text_file)[0]
new_docx_file_path = new_path + "/" + new_filename

#saves the document with all the under the name of the 
#original text file name
document.save(new_docx_file_path)
print("Document saved.")