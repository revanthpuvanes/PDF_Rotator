# importing necessary packages
from flask import Flask, render_template, request, send_file
import PyPDF2 as pyd
from eval import PDFrotate


app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/upload", methods=['GET','POST'])
def upload():
    # saving input file in the destination folder
    for file in request.files.getlist("file"):
        file_name = file.filename
        destination = "/".join([UPLOAD_FOLDER, file_name])
        file.save(destination)

    # getting inputs from the user
    if request.method == 'POST':
        pageno = request.form.get('pageno')
        # print('#######################################################',pageno)
    if request.method == 'POST':
        angle = request.form.get('angle')
        # print('#######################################################',angle)
    
    # checks filename and apply function
    if file_name == file.filename:
        output = PDFrotate(file_name, pageno, angle)
        # merging final modified files
        modified = './new/new.pdf'
        mergefile = './new/rotate.pdf'
        pdf_merger = pyd.PdfFileMerger()
        pdf_merger.append(modified)
        pdf_merger.merge((int(pageno) - 1), mergefile)
        with open('./final/'+file_name, 'wb') as f:
            pdf_merger.write(f)

    return render_template('result.html',value = file_name)


@app.route("/final/<filename>",methods = ['GET'])
def final(filename):
    file_path = "./final/"+filename
    return send_file(file_path, as_attachment=True, attachment_filename='')


if __name__ == '__main__':  
    app.run(debug = True)