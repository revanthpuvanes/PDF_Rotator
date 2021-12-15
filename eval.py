from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def PDFrotate(origFileName, page, rotation):
 
    # creating a pdf File object of original pdf
    orig = open('./static/uploads/'+origFileName, 'rb')
     
    # creating a pdf Reader object
    pdfReader = PdfFileReader(orig)
 
    # creating a pdf writer object for new pdf
    pdfWriter = PdfFileWriter()
 
    # creating rotated page object
    pageObj = pdfReader.getPage(int(page) - 1)
    pageObj.rotateClockwise(int(rotation))
 
    # adding rotated page object to pdf writer
    pdfWriter.addPage(pageObj)
 
    # new pdf file object
    newFile = open('./new/rotate.pdf', 'wb')
     
    # writing rotated pages to new file
    pdfWriter.write(newFile)
 
    # enter the page to delete
    pages_to_delete = [int(page) - 1]

    infile = PdfFileReader('./static/uploads/'+origFileName, 'rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if i not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)
            # print("##############",output)
            
    with open('./new/new.pdf', 'wb') as f:
        output.write(f)
