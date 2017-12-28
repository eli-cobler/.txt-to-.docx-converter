from docx import Document


text_file = "/Users/elicobler/tiny_dancer/BackEnd/TextFiles/12.18.18 - Monday - Hr 2 - Seg 1.txt"

#opens document to add text to
document = Document()

#adds the entire contents to a list that we will
#then use to add to the document we just created
fileContents = []
for line in open(text_file):
    row = line.split(' ')
    fileContents += list(row)

#adds all the text we just created to the document as a paragraph
paragraph = document.add_paragraph(fileContents)

#saves the document with all the under the name we give it
document.save('test.docx')
print("Document saved.")