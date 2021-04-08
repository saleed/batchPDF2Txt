from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt


# converts pdf, returns its text content as a string
# from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


# converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir=="":
        print("pdf dir error")
    if txtDir=="":
        os.makedirs(txtDir)

    for pdf_fullname in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
        file_name,fileExtension = os.path.split(pdf_fullname)
        if fileExtension == "pdf":
            pdfFilename = os.path.join(pdfDir,pdf_fullname)
            text = convert(pdfFilename)  # get string of text content of pdf

            txtFilename=os.path.join(txtDir,file_name+".txt")
            textFile = open(txtFilename, "w")  # make text file
            textFile.write(text)  # write text to text file


if __name__ == "__main__":
    # main(sys.argv[1:])
    convertMultiple("", "")




