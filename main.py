import PyQt5
import sys
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import pandas as pd
import time as t
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas
import numpy as np
from datetime import date
from PyPDF2 import PdfMerger


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("PatientNama - Add Patient Record")
    win.setWindowIcon(QIcon("Me.jpg"))
    win.setToolTip("PatientNama - Patient Record Management APP")
    win.setStyleSheet('''
        background-color:#232023;
        padding:2px;
        border: none;
        color: white;
        border-radius:10px;
        font-weight:1000;
        ''')
    win.resize(700, 250)

    # 48494B
    formLayout = QFormLayout(win)
    groupbox = QGroupBox()

# ---------------------------------------------------------------------------------------------------------------------------------------------

    def pdfGenerate(wordList):
        temp = ""
        paths=""
        y = os.environ.get('USERNAME')
        my_canvas = canvas.Canvas(
            "C:\\Users\\"+str(y)+"\\Downloads\\"+wordList[0]+"_"+wordList[6]+"(0).pdf", pagesize=A4)
        my_canvas.setLineWidth(.3)
        my_canvas.setFont('Helvetica', 15)
        my_canvas.drawImage("Me.jpg", 30, 770, width=60, height=60)
        my_canvas.drawString(
            100, 800, "Sheikh Zayad Hospital-Surgical Unit-l, Lahore")

        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(470, 780, 'Discharge Summary')
        my_canvas.setFont('Helvetica', 11)
        my_canvas.drawString(420, 730, "Discharge Date: ")
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        my_canvas.drawString(510, 730, d2)
        my_canvas.line(460, 773, 580, 773)

        my_canvas.drawString(440, 750, 'Admit Date:')
        my_canvas.drawString(510, 750, wordList[59])

        my_canvas.drawString(350, 710, 'Consultant Name:')
        my_canvas.drawString(450, 710, wordList[60])
        my_canvas.drawString(350, 710, 'Consultant Name:')
        my_canvas.drawString(450, 710, wordList[60])
# ----------------------------------------------------------------------------------------------
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 680, 'Patient Information:')
        my_canvas.line(30, 670, 580, 670)
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 680, 'Patient Information:')
        my_canvas.line(30, 670, 580, 670)

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(40, 650, 'Name:')
        my_canvas.drawString(100, 650, wordList[0])
        my_canvas.drawString(40, 630, 'Gender:')
        my_canvas.drawString(100, 630, wordList[1])
        my_canvas.drawString(40, 610, 'Address:')
        my_canvas.drawString(100, 610, wordList[2])

        my_canvas.drawString(250, 650, 'Age:')
        my_canvas.drawString(280, 650, wordList[3])
        my_canvas.drawString(250, 630, 'Phone No:')
        my_canvas.drawString(315, 630, wordList[4])
        my_canvas.drawString(250, 610, 'City:')
        my_canvas.drawString(280, 610, wordList[5])

        my_canvas.drawString(430, 650, 'Cnic:')
        my_canvas.drawString(460, 650, wordList[6])
        my_canvas.drawString(430, 630, 'Hospital Number:')
        my_canvas.drawString(520, 630, wordList[7])

# ------------------------------------------------------------------------------------

        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 510+70, 'Clinical Data:')
        my_canvas.line(30, 500+70, 580, 500+70)
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 510+70, 'Clinical Data:')
        my_canvas.line(30, 500+70, 580, 500+70)

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(50, 475+70, 'Present Complaint')
        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(50, 475+70, 'Present Complaint')
        my_canvas.setFont('Helvetica', 9.5)

        temp = str(wordList[8])
        word = temp.split("|")

        for i in range(len(word)):
            my_canvas.drawString(50, (460+70)-((i+1)*12), word[i])
        # my_canvas.rect(40, 440, 530, 120, stroke=1, fill=0)

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(50, 420+70-50, 'Examination Findings')
        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(50, 420+70-50, 'Examination Findings')

        my_canvas.setFont('Helvetica', 9.5)
        temp = ""
        word.clear()
        temp = str(wordList[9])
        word = temp.split("|")
        for i in range(len(word)):
            my_canvas.drawString(50, (400+70-50)-((i+1)*12), word[i])
        # my_canvas.rect(310, 430, 220, 100, stroke=1, fill=0)
# -------------------------------------------------------------------------------------
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 420-100, 'Investigations:')
        my_canvas.line(30, 410-100, 580, 410-100)
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 420-100, 'Investigations:')
        my_canvas.line(30, 410-100, 580, 410-100)

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(30, 390-100, 'CBC:')
        my_canvas.drawString(100, 390-100, wordList[10])
        my_canvas.drawString(30, 375-100, 'LFT:')
        my_canvas.drawString(100, 375-100, wordList[11])
        my_canvas.drawString(30, 360-100, 'Electrolyte:')
        my_canvas.drawString(100, 360-100, wordList[12])
        my_canvas.drawString(30, 345-100, 'Viral Markers:')
        my_canvas.drawString(100, 345-100, wordList[13])
        my_canvas.drawString(30, 330-100, 'Imaging:')
        my_canvas.drawString(100, 330-100, wordList[14])
        my_canvas.drawString(30, 295+20-100, 'Others:')
        my_canvas.drawString(100, 295+20-100, wordList[15])

        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 285-100, 'Operative Notes')
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(30, 285-100, 'Operative Notes')

        temp = ""
        word.clear()
        temp = str(wordList[16])
        word = temp.split("|")
        my_canvas.setFont('Helvetica', 10)
        for i in range(len(word)):
            my_canvas.drawString(40, (265-100)-(12*(i+1)), word[i])
 # -----------------------------------------------------------------------------
        my_canvas.line(30, 280-100, 580, 280-100)
        my_canvas.save()
# ----------------------------------------------------------------------------------------------
        my_canvasT = canvas.Canvas(
            "C:\\Users\\"+str(y)+"\\Downloads\\"+wordList[0]+"_"+wordList[6]+"(1).pdf", pagesize=A4)
        my_canvasT.setLineWidth(.3)
        my_canvasT.setFont('Helvetica', 15)
        my_canvasT.drawImage("Me.jpg", 30, 770, width=60, height=60)
        my_canvasT.drawString(
            100, 800, "Sheikh Zayad Hospital-Surgical Unit-l, Lahore")

        my_canvasT.setFont('Helvetica', 12)
        my_canvasT.drawString(470, 780, 'Discharge Summary')
        my_canvasT.setFont('Helvetica', 11)
        my_canvasT.drawString(420, 730, "Discharge Date: ")
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        my_canvasT.drawString(510, 730, d2)
        my_canvasT.line(460, 773, 580, 773)

        my_canvasT.drawString(440, 750, 'Admit Date:')
        my_canvasT.drawString(510, 750, wordList[59])

        my_canvasT.drawString(350, 710, 'Consultant Name:')
        my_canvasT.drawString(450, 710, wordList[60])
        my_canvasT.drawString(350, 710, 'Consultant Name:')
        my_canvasT.drawString(450, 710, wordList[60])

        my_canvasT.drawString(30, 680, 'Course / Treatment')
        my_canvasT.line(30, 675, 580, 675)
        my_canvasT.drawString(30, 680, 'Course / Treatment')
        my_canvasT.line(30, 675, 580, 675)


        my_canvasT.setFont('Helvetica', 9.5)
        temp = ""
        word.clear()
        temp = str(wordList[16])
        word = temp.split("|")

        for i in range(len(word)):
            my_canvasT.drawString(40, 660-((i+1)*12), word[i])
        # my_canvas.rect(310, 210, 220, 50, stroke=1, fill=0)
# ------------------------------------------------------------------------------
        my_canvasT.setFont('Helvetica', 13)
        my_canvasT.drawString(30, 198+300, 'Discharge Medicines')
        my_canvasT.setFont('Helvetica', 13)
        my_canvasT.drawString(30, 198+300, 'Discharge Medicines')

        my_canvasT.setFont('Helvetica', 13)
        my_canvasT.drawString(30, 40+300, 'FollowUp Instructions')
        my_canvasT.setFont('Helvetica', 13)
        my_canvasT.drawString(30, 40+300, 'FollowUp Instructions')
        my_canvasT.line(30, 195+300, 580, 195+300)
        my_canvasT.line(30, 35+300, 580, 35+300)

        my_canvasT.setFont('Helvetica', 11)
        my_canvasT.drawString(40, 175+300, "Name")
        my_canvasT.drawString(150, 175+300, "Dose")
        my_canvasT.drawString(250, 175+300, "Times")
        my_canvasT.drawString(350, 175+300, "Days")

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 160+300, wordList[19])
        my_canvasT.drawString(150, 160+300, wordList[20])
        my_canvasT.drawString(250, 160+300, wordList[21])
        my_canvasT.drawString(350, 160+300, wordList[22])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 150+300, wordList[23])
        my_canvasT.drawString(150, 150+300, wordList[24])
        my_canvasT.drawString(250, 150+300, wordList[25])
        my_canvasT.drawString(350, 150+300, wordList[26])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 140+300, wordList[27])
        my_canvasT.drawString(150, 140+300, wordList[28])
        my_canvasT.drawString(250, 140+300, wordList[29])
        my_canvasT.drawString(350, 140+300, wordList[30])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 130+300, wordList[31])
        my_canvasT.drawString(150, 130+300, wordList[32])
        my_canvasT.drawString(250, 130+300, wordList[33])
        my_canvasT.drawString(350, 130+300, wordList[34])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 120+300, wordList[35])
        my_canvasT.drawString(150, 120+300, wordList[36])
        my_canvasT.drawString(250, 120+300, wordList[37])
        my_canvasT.drawString(350, 120+300, wordList[38])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 110+300, wordList[39])
        my_canvasT.drawString(150, 110+300, wordList[40])
        my_canvasT.drawString(250, 110+300, wordList[41])
        my_canvasT.drawString(350, 110+300, wordList[42])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 100+300, wordList[43])
        my_canvasT.drawString(150, 100+300, wordList[44])
        my_canvasT.drawString(250, 100+300, wordList[45])
        my_canvasT.drawString(350, 100+300, wordList[46])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 90+300, wordList[47])
        my_canvasT.drawString(150, 90+300, wordList[48])
        my_canvasT.drawString(250, 90+300, wordList[49])
        my_canvasT.drawString(350, 90+300, wordList[50])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 80+300, wordList[51])
        my_canvasT.drawString(150, 80+300, wordList[52])
        my_canvasT.drawString(250, 80+300, wordList[53])
        my_canvasT.drawString(350, 80+300, wordList[54])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(40, 70+300, wordList[55])
        my_canvasT.drawString(150, 70+300, wordList[56])
        my_canvasT.drawString(250, 70+300, wordList[57])
        my_canvasT.drawString(350, 70+300, wordList[58])

        my_canvasT.setFont('Helvetica', 9)
        temp = ""
        word.clear()
        temp = str(wordList[18])
        word = temp.split("|")
        for i in range(len(word)):
            my_canvasT.drawString(40, (25+300)-((i+1)*12), word[i])

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(
            50, 10+100, "Doctor's Signature:_____________________")

        my_canvasT.setFont('Helvetica', 9)
        my_canvasT.drawString(
            330, 10+100, "Consultant's Signature:_____________________")

        my_canvasT.save()
# ----------------------------------------------------------------------------------------------

        # Create an instance of PdfFileMerger() class
        merger = PdfMerger()

        # Create a list with the file paths
        pdf_files = ["C:\\Users\\"+str(y)+"\\Downloads\\"+wordList[0]+"_"+wordList[6]+"(0).pdf",
                     "C:\\Users\\"+str(y)+"\\Downloads\\"+wordList[0]+"_"+wordList[6]+"(1).pdf"]

        # Iterate over the list of the file paths
        for pdf_file in pdf_files:
            # Append PDF files
            merger.append(pdf_file)

        # Write out the merged PDF file
        merger.write("C:\\Users\\"+str(y)+"\\Downloads\\" +
                     wordList[0]+"_"+wordList[6]+".pdf")
        merger.close()

        if os.path.exists("C:\\Users\\"+str(y)+"\\Downloads\\"+wordList[0]+"_"+wordList[6]+"(0).pdf"):
            os.remove("C:\\Users\\"+str(y)+"\\Downloads\\" +
                      wordList[0]+"_"+wordList[6]+"(0).pdf")
        else:
            print("The file does not exist")

        if os.path.exists("C:\\Users\\"+str(y)+"\\Downloads\\"+wordList[0]+"_"+wordList[6]+"(1).pdf"):
            os.remove("C:\\Users\\"+str(y)+"\\Downloads\\" +
                      wordList[0]+"_"+wordList[6]+"(1).pdf")
        else:
            print("The file does not exist")
        
        paths="C:\\Users\\"+str(y)+"\\Downloads\\" +wordList[0]+"_"+wordList[6]+".pdf"
        paths=str(paths)
        if os.path.exists(paths):
            os.rename(paths,paths.replace(" ","_"))
            pass
        else:
            print("The file does not exist")

        print("Path:",paths.replace(" ","_"))
        os. system(paths.replace(" ","_"))

    def search():
        print("Search Button Clicked")
        hos_num = sear.text()
        print(hos_num)
        search_item = -1
        word = [""]
        word.pop()
        excel_data_df = pd.read_excel('Data.xlsx', sheet_name='Sheet1')
        x = excel_data_df["Hospital Number"].tolist()
        try:
            index = int((x.index(int(hos_num))))
        except ValueError:
            index = -1
            print("Error Occuring In Try/Exception.")
        print(index)
        if index != -1:
            finalRow = excel_data_df.loc[index, :]
            word.append(str(finalRow["Name"]))
            word.append(str(finalRow["Gender"]))
            word.append(str(finalRow["Address"]))
            word.append(str(finalRow["Age"]))
            word.append(str(finalRow["Phone Number"]))
            word.append(str(finalRow["Home City"]))
            word.append(str(finalRow["SID"]))
            word.append(str(finalRow["Hospital Number"]))
            word.append(str(finalRow["Present Complaint"]))
            word.append(str(finalRow["Examination Findings"]))

            word.append(str(finalRow["CBC"]))
            word.append(str(finalRow["LFT"]))
            word.append(str(finalRow["Electrolyte"]))
            word.append(str(finalRow["Viral Markers"]))
            word.append(str(finalRow["Imaging"]))
            word.append(str(finalRow["Others"]))
            word.append(str(finalRow["Operative Notes"]))
            word.append(str(finalRow["Course Treatment"]))
            word.append(str(finalRow["FollowUp Instructions"]))

            word.append(str(finalRow["Medicine 1"]))
            word.append(str(finalRow["Dose 1"]))
            word.append(str(finalRow["Times 1"]))
            word.append(str(finalRow["Days 1"]))

            word.append(str(finalRow["Medicine 2"]))
            word.append(str(finalRow["Dose 2"]))
            word.append(str(finalRow["Times 2"]))
            word.append(str(finalRow["Days 2"]))

            word.append(str(finalRow["Medicine 3"]))
            word.append(str(finalRow["Dose 3"]))
            word.append(str(finalRow["Times 3"]))
            word.append(str(finalRow["Days 3"]))

            word.append(str(finalRow["Medicine 4"]))
            word.append(str(finalRow["Dose 4"]))
            word.append(str(finalRow["Times 4"]))
            word.append(str(finalRow["Days 4"]))

            word.append(str(finalRow["Medicine 5"]))
            word.append(str(finalRow["Dose 5"]))
            word.append(str(finalRow["Times 5"]))
            word.append(str(finalRow["Days 5"]))

            word.append(str(finalRow["Medicine 6"]))
            word.append(str(finalRow["Dose 6"]))
            word.append(str(finalRow["Times 6"]))
            word.append(str(finalRow["Days 6"]))

            word.append(str(finalRow["Medicine 7"]))
            word.append(str(finalRow["Dose 7"]))
            word.append(str(finalRow["Times 7"]))
            word.append(str(finalRow["Days 7"]))

            word.append(str(finalRow["Medicine 8"]))
            word.append(str(finalRow["Dose 8"]))
            word.append(str(finalRow["Times 8"]))
            word.append(str(finalRow["Days 8"]))

            word.append(str(finalRow["Medicine 9"]))
            word.append(str(finalRow["Dose 9"]))
            word.append(str(finalRow["Times 9"]))
            word.append(str(finalRow["Days 9"]))

            word.append(str(finalRow["Medicine 10"]))
            word.append(str(finalRow["Dose 10"]))
            word.append(str(finalRow["Times 10"]))
            word.append(str(finalRow["Days 10"]))
            word.append(str(finalRow["Admit Date"]))
            word.append(str(finalRow["Consultant Name"]))

            search_item = 1

        if search_item != -1:
            label2.setStyleSheet("background-color: lightgreen")
            label2.setText("Patient Details Found / Generating PDF...")
            label2.move(1210, 700)
            label2.resize(200, 30)
            pdfGenerate(word)
        else:
            label2.setStyleSheet("background-color: red")
            label2.setText("Patient Details Not Found")
            label2.move(1210, 700)
            label2.resize(200, 30)

    def submit(self):

        Patient_Medicine = list()
        Patient_Dose = list()
        Patient_Times = list()
        Patient_Days = list()

        Patient_Name = pat_name2.text()
        Patient_Gender = pat_gender2.text()
        Patient_Address = pat_address2.text()
        Patient_Age = pat_age_.text()
        Patient_PhoneNo = pat_phone_.text()
        Patient_Home_City = pat_hcity.text()
        Patient_SID = pat_sid.text()
        Patient_Hospital_Number = pat_hn_.text()
        Patient_Present_Complaint = pat_pc_1.text()+" | " + pat_pc_2.text() + \
            " | "+pat_pc_3.text()+" | " + pat_pc_4.text() + \
            " | "+pat_pc_5.text()+" | "+pat_pc_6.text()

        Patient_Examination_Findings = pat_ef_1.text()+" | " + pat_ef_2.text() + \
            " | "+pat_ef_3.text()+" | " + pat_ef_4.text() + \
            " | "+pat_ef_5.text()+" | "+pat_ef_6.text()

        Patient_Ivestigations_CBC = cbc__.text()
        Patient_Ivestigations_LFT = lft_.text()
        Patient_Ivestigations_Electrolyte = electro_.text()
        Patient_Ivestigations_Viral_Markers = vm_.text()
        Patient_Ivestigations_Imaging = imag_.text()
        Patient_Ivestigations_Others = other_.text()
        Patient_Operative_Notes = cbc1.text()+" | " + cbc2.text()+" | "+cbc3.text() + \
            " | "+cbc1_.text()+" | "+cbc2_.text()+" | "+cbc3_.text()

        Patient_Course_Treatment = cbc5.text()+" | " + cbc6.text()+" | "+cbc7__.text() + \
            " | "+cbc5_.text()+" | "+cbc6_.text()+" | "+cbc7_.text()

        Patient_Admit_Date = pat_start_.text()
        Patient_Consultant_Name = pat_con_name2.text()

        if Patient_Ivestigations_CBC=="":
            Patient_Ivestigations_CBC="-"

        if Patient_Ivestigations_LFT=="":
            Patient_Ivestigations_LFT="-"

        if Patient_Ivestigations_Electrolyte=="":
            Patient_Ivestigations_Electrolyte="-"

        if Patient_Ivestigations_Viral_Markers=="":
            Patient_Ivestigations_Viral_Markers="-"

        if Patient_Ivestigations_Imaging=="":
            Patient_Ivestigations_Imaging="-"

        if Patient_Ivestigations_Others=="":
            Patient_Ivestigations_Others="-"
        
        for i in range(rows):
            Patient_Medicine.append(tableWidget.item(i, 0).text())
            Patient_Dose.append(tableWidget.item(i, 1).text())
            Patient_Times.append(tableWidget.item(i, 2).text())
            Patient_Days.append(tableWidget.item(i, 3).text())

        for i in range(rows):
            if Patient_Medicine[i]=="":
                Patient_Medicine[i] = "-"
            if Patient_Dose[i]=="":
                Patient_Dose[i] = "-"
            if Patient_Times[i]=="":
                Patient_Times[i] = "-"
            if Patient_Days[i]=="":
                Patient_Days[i] = "-"


        Patient_Follow_Up_Instructions = cbc71.text()+" | " + cbc8.text() + \
            " | "+cbc9.text()+" | "+cbc712.text()+" | "+cbc81.text()+" | "+cbc91.text()

        if Patient_Age == "":
            Patient_Age = "-1"
        elif (not Patient_Hospital_Number.isdigit()):
            Patient_Hospital_Number = "-1"

        if Patient_Hospital_Number == "":
            Patient_Hospital_Number = "-1"

        if Patient_Name == "":
            label.setStyleSheet("background-color: red")
            label.setText("Name Box Empty")
            label.move(1210, 700)
            label.resize(200, 30)
        elif not Patient_Name.replace(" ","").isalpha():
            label.setStyleSheet("background-color: red")
            label.setText("Patient Name Should Have Only Characters.")
            label.move(1210, 700)
            label.resize(200, 30)
        elif Patient_Consultant_Name == "":
            label.setStyleSheet("background-color: red")
            label.setText("Consultant Name")
            label.move(1210, 700)
            label.resize(200, 30)
        elif not Patient_Consultant_Name.replace(" ","").isalpha():
            label.setStyleSheet("background-color: red")
            label.setText("Consultant's Name Should Have Only Characters.")
            label.move(1210, 700)
            label.resize(200, 30)
        elif Patient_Gender == "":
            label.setStyleSheet("background-color: red")
            label.setText("Gender Empty")
            label.move(1210, 700)
            label.resize(200, 30)
        elif Patient_Address == "":
            label.setStyleSheet("background-color: red")
            label.setText("Address Empty")
            label.move(1210, 700)
            label.resize(200, 30)
        elif int(Patient_Age) < 1 or int(Patient_Age) > 120:
            label.setStyleSheet("background-color: red")
            label.setText("Age Between 0 to 120")
            label.move(1210, 700)
            label.resize(200, 30)
        elif len(Patient_PhoneNo) != 11:
            label.setStyleSheet("background-color: red")
            label.setText("Enter Proper Mobile No.")
            label.move(1210, 700)
            label.resize(200, 30)
        elif Patient_Home_City == "":
            label.setStyleSheet("background-color: red")
            label.setText("Home City Empty")
            label.move(1210, 700)
            label.resize(200, 30)
        elif not Patient_Home_City.isalpha():
            label.setStyleSheet("background-color: red")
            label.setText("Should Have Only Characters.")
            label.move(1210, 700)
            label.resize(200, 30)
        elif Patient_SID == "":
            label.setStyleSheet("background-color: red")
            label.setText("CNIC Empty")
            label.move(1210, 700)
            label.resize(200, 30)
        elif len(Patient_SID) !=13:
            label.setStyleSheet("background-color: red")
            label.setText("Invalid CNIC")
            label.move(1210, 700)
            label.resize(200, 30)
        elif (int(Patient_Hospital_Number) < 0):
            label.setStyleSheet("background-color: red")
            label.setText("Invalid Hospital Number")
            label.move(1210, 700)
            label.resize(200, 30)
        elif Patient_Admit_Date == "":
            label.setStyleSheet("background-color: red")
            label.setText("Invalid Hospital Number")
            label.move(1210, 700)
            label.resize(200, 30)
        else:
            print("Next Clicked.")
            label.setStyleSheet("background-color:lightgreen;")
            label.setText("Record Added")
            label.move(1210, 700)
            label.resize(200, 30)
            # new dataframe with same columns


            df = pd.DataFrame({'Name': [Patient_Name], 'Gender': [Patient_Gender], 'Address': [Patient_Address], 'Age': [Patient_Age], 'Phone Number': [Patient_PhoneNo], 'Home City': [Patient_Home_City],
                               'SID': [Patient_SID], 'Hospital Number': [Patient_Hospital_Number], 'Present Complaint': [Patient_Present_Complaint], 'Examination Findings': [Patient_Examination_Findings],
                               'CBC': [Patient_Ivestigations_CBC], 'LFT': [Patient_Ivestigations_LFT], 'Electrolyte': [Patient_Ivestigations_Electrolyte], 'Viral Markers': [Patient_Ivestigations_Viral_Markers], 'Imaging': [Patient_Ivestigations_Imaging],
                               'Others': [Patient_Ivestigations_Others], 'Operative Notes': [Patient_Operative_Notes], 'Course Treatment': [Patient_Course_Treatment], 'FollowUp Instructions': [Patient_Follow_Up_Instructions],
                               'Medicine 1': [Patient_Medicine[0]], 'Dose 1': [Patient_Dose[0]], 'Times 1': [Patient_Times[0]], 'Days 1': [Patient_Days[0]],
                               'Medicine 2': [Patient_Medicine[1]], 'Dose 2': [Patient_Dose[1]], 'Times 2': [Patient_Times[1]], 'Days 2': [Patient_Days[1]],
                               'Medicine 3': [Patient_Medicine[2]], 'Dose 3': [Patient_Dose[2]], 'Times 3': [Patient_Times[2]], 'Days 3': [Patient_Days[2]],
                               'Medicine 4': [Patient_Medicine[3]], 'Dose 4': [Patient_Dose[3]], 'Times 4': [Patient_Times[3]], 'Days 4': [Patient_Days[3]],
                               'Medicine 5': [Patient_Medicine[4]], 'Dose 5': [Patient_Dose[4]], 'Times 5': [Patient_Times[4]], 'Days 5': [Patient_Days[4]],
                               'Medicine 6': [Patient_Medicine[5]], 'Dose 6': [Patient_Dose[5]], 'Times 6': [Patient_Times[5]], 'Days 6': [Patient_Days[5]],
                               'Medicine 7': [Patient_Medicine[6]], 'Dose 7': [Patient_Dose[6]], 'Times 7': [Patient_Times[6]], 'Days 7': [Patient_Days[6]],
                               'Medicine 8': [Patient_Medicine[7]], 'Dose 8': [Patient_Dose[7]], 'Times 8': [Patient_Times[7]], 'Days 8': [Patient_Days[7]],
                               'Medicine 9': [Patient_Medicine[8]], 'Dose 9': [Patient_Dose[8]], 'Times 9': [Patient_Times[8]], 'Days 9': [Patient_Days[8]],
                               'Medicine 10': [Patient_Medicine[9]], 'Dose 10': [Patient_Dose[9]], 'Times 10': [Patient_Times[9]], 'Days 10': [Patient_Days[9]],
                               'Medicine 11': [Patient_Medicine[10]], 'Dose 11': [Patient_Dose[10]], 'Times 11': [Patient_Times[10]], 'Days 11': [Patient_Days[10]],
                               'Medicine 12': [Patient_Medicine[11]], 'Dose 12': [Patient_Dose[11]], 'Times 12': [Patient_Times[11]], 'Days 12': [Patient_Days[11]],
                               'Medicine 13': [Patient_Medicine[12]], 'Dose 13': [Patient_Dose[12]], 'Times 13': [Patient_Times[12]], 'Days 13': [Patient_Days[12]],
                               'Medicine 14': [Patient_Medicine[13]], 'Dose 14': [Patient_Dose[13]], 'Times 14': [Patient_Times[13]], 'Days 14': [Patient_Days[13]],
                               'Medicine 15': [Patient_Medicine[14]], 'Dose 15': [Patient_Dose[14]], 'Times 15': [Patient_Times[14]], 'Days 15': [Patient_Days[14]],
                               'Medicine 16': [Patient_Medicine[15]], 'Dose 16': [Patient_Dose[15]], 'Times 16': [Patient_Times[15]], 'Days 16': [Patient_Days[15]],
                               'Medicine 17': [Patient_Medicine[16]], 'Dose 17': [Patient_Dose[16]], 'Times 17': [Patient_Times[16]], 'Days 17': [Patient_Days[16]],
                               'Medicine 18': [Patient_Medicine[17]], 'Dose 18': [Patient_Dose[17]], 'Times 18': [Patient_Times[17]], 'Days 18': [Patient_Days[17]],
                               'Medicine 19': [Patient_Medicine[18]], 'Dose 19': [Patient_Dose[18]], 'Times 19': [Patient_Times[18]], 'Days 19': [Patient_Days[18]],
                               'Medicine 20': [Patient_Medicine[19]], 'Dose 20': [Patient_Dose[19]], 'Times 20': [Patient_Times[19]], 'Days 20': [Patient_Days[19]],
                               'Medicine 21': [Patient_Medicine[20]], 'Dose 21': [Patient_Dose[20]], 'Times 21': [Patient_Times[20]], 'Days 21': [Patient_Days[20]],
                               'Medicine 22': [Patient_Medicine[21]], 'Dose 22': [Patient_Dose[21]], 'Times 22': [Patient_Times[21]], 'Days 22': [Patient_Days[21]],
                               'Medicine 23': [Patient_Medicine[22]], 'Dose 23': [Patient_Dose[22]], 'Times 23': [Patient_Times[22]], 'Days 23': [Patient_Days[22]],
                               'Medicine 24': [Patient_Medicine[23]], 'Dose 24': [Patient_Dose[23]], 'Times 24': [Patient_Times[23]], 'Days 24': [Patient_Days[23]],
                               'Medicine 25': [Patient_Medicine[24]], 'Dose 25': [Patient_Dose[24]], 'Times 25': [Patient_Times[24]], 'Days 25': [Patient_Days[24]],
                               'Admit Date': [Patient_Admit_Date], 'Consultant Name': [Patient_Consultant_Name]})

            # read  file content
            reader = pd.read_excel('Data.xlsx')

            # create writer object
            # used engine='openpyxl' because append operation is not supported by xlsxwriter
            writer = pd.ExcelWriter(
                'Data.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")

            # append new dataframe to the excel sheet
            df.to_excel(writer, index=False, header=False,
                        startrow=len(reader) + 1)
            # close file
            writer.close()

            t.sleep(1)
            sear.setText(Patient_Hospital_Number)
            search()

# ---------------------------------------------------------------------------------------------------------------------------------------------
    test_box = QtWidgets.QLabel(win)
    test_box.setText("")
    test_box.setStyleSheet("border:0px;")

    pic = QLabel(win)
    pixmap = QPixmap('Me.jpg').scaled(200, 200)
    pic.setPixmap(pixmap)
    pic.setStyleSheet("border:0px;border-radius:10px;margin-left:500px;")

    hospital_detail = QtWidgets.QLabel(win)
    hospital_detail.setText("Sheikh Zayad Hospital\nSurgical Unit-l, Lahore")
    hospital_detail.setFont(QFont('Roboto', 15))
    hospital_detail.setStyleSheet("font-size:20px;margin-left:500px;")

    discharge = QtWidgets.QLabel(win)
    discharge.setText("Discharge\nSummary")
    discharge.setFont(QFont('Roboto', 15))
    discharge.setStyleSheet("font-size:20px;margin-left:500px;")

    pat = QtWidgets.QLabel(win)
    pat.setText("Patient Information")
    pat.setFont(QFont('Roboto', 12))

    hor_info = QtWidgets.QLabel(win)
    hor_info.setText("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info.setStyleSheet("border:none;")

    formLayout.addRow(pic, test_box)
    formLayout.addRow(hospital_detail, test_box)
    formLayout.addRow(discharge, test_box)
    # formLayout.addRow(discharge)
    formLayout.addRow(pat, test_box)
    formLayout.addRow(hor_info, test_box)
# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_name1 = QtWidgets.QLabel(win)
    pat_name1.setText("Name:")
    pat_name2 = QtWidgets.QLineEdit(win)
    pat_name2.setFont(QFont('Roboto', 10))
    pat_name2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_con_name1 = QtWidgets.QLabel(win)
    pat_con_name1.setText("Consultant Name:")
    pat_con_name2 = QtWidgets.QLineEdit(win)
    pat_con_name2.setFont(QFont('Roboto', 10))
    pat_con_name2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_gender1 = QtWidgets.QLabel(win)
    pat_gender1.setText("")
    pat_gender1.setStyleSheet("border:0px")

    pat_gender2 = QtWidgets.QLineEdit(win)
    pat_gender2.setFont(QFont('Roboto', 10))
    pat_gender2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    def maleselected():
        pat_gender2.setText("Male")

    def femaleselected():
        pat_gender2.setText("Female")

    def other():
        pat_gender2.setText("other")

    # Radio button for male
    radioButton_male = QtWidgets.QRadioButton(win)
    radioButton_male.setStyleSheet("border:0px")
    radioButton_male.setGeometry(QtCore.QRect(180, 120, 95, 20))

    # adding signal and slot
    radioButton_male.toggled.connect(maleselected)

    # Radio button for female
    radioButton_female = QtWidgets.QRadioButton(win)
    radioButton_female.setStyleSheet("border:0px")
    radioButton_female.setGeometry(QtCore.QRect(180, 150, 95, 20))

    # adding signal and slot
    radioButton_female.toggled.connect(femaleselected)

    # Radio button for other
    radioButton_other = QtWidgets.QRadioButton(win)
    radioButton_other.setStyleSheet("border:0px")
    radioButton_other.setGeometry(QtCore.QRect(180, 150, 95, 20))

    # adding signal and slot
    radioButton_other.toggled.connect(other)

    pat_address1 = QtWidgets.QLabel(win)
    pat_address1.setText("Address:")
    pat_address2 = QtWidgets.QLineEdit(win)
    pat_address2.setFont(QFont('Roboto', 10))
    pat_address2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    formLayout.addRow(pat_name1, test_box)
    formLayout.addRow(pat_name2, test_box)

    formLayout.addRow(pat_con_name1, test_box)
    formLayout.addRow(pat_con_name2, test_box)

    formLayout.addRow("Gender:", pat_gender1)
    formLayout.addRow("Male", test_box)
    formLayout.addRow(radioButton_male, test_box)
    formLayout.addRow("Female", test_box)
    formLayout.addRow(radioButton_female, test_box)
    formLayout.addRow("Others", test_box)
    formLayout.addRow(radioButton_other, test_box)


    formLayout.addRow(pat_address1, test_box)
    formLayout.addRow(pat_address2, test_box)

# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_age = QtWidgets.QLabel(win)
    pat_age.setText("Age (Years):")

    pat_age_ = QtWidgets.QLineEdit(win)
    pat_age_.setFont(QFont('Roboto', 10))
    pat_age_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_phone = QtWidgets.QLabel(win)
    pat_phone.setText("Mobile No.:")

    pat_phone_ = QtWidgets.QLineEdit(win)
    pat_phone_.setFont(QFont('Roboto', 10))
    pat_phone_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_hcity_ = QtWidgets.QLabel(win)
    pat_hcity_.setText("Home City:")

    pat_hcity = QtWidgets.QLineEdit(win)
    pat_hcity.setFont(QFont('Roboto', 10))
    pat_hcity.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    formLayout.addRow(pat_age, test_box)
    formLayout.addRow(pat_age_, test_box)

    formLayout.addRow(pat_phone, test_box)
    formLayout.addRow(pat_phone_, test_box)

    formLayout.addRow(pat_hcity_, test_box)
    formLayout.addRow(pat_hcity, test_box)
# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_phone100 = QtWidgets.QLabel(win)
    pat_phone100.setText("Cnic:")

    pat_sid = QtWidgets.QLineEdit(win)
    pat_sid.setFont(QFont('Roboto', 10))
    pat_sid.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_hn = QtWidgets.QLabel(win)
    pat_hn.setText("Hospital Number:")

    pat_hn_ = QtWidgets.QLineEdit(win)
    pat_hn_.setFont(QFont('Roboto', 10))
    pat_hn_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_start = QtWidgets.QLabel(win)
    pat_start.setText("Admit Date:")

    pat_start_ = QtWidgets.QLineEdit(win)
    pat_start_.setFont(QFont('Roboto', 10))
    pat_start_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    hor_info2 = QtWidgets.QLabel(win)
    hor_info2.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info2.setStyleSheet("border:none;")
    formLayout.addRow(pat_phone100, test_box)
    formLayout.addRow(pat_sid, test_box)

    formLayout.addRow(pat_hn, test_box)
    formLayout.addRow(pat_hn_, test_box)

    formLayout.addRow(pat_start, test_box)
    formLayout.addRow(pat_start_, test_box)

# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_info2 = QtWidgets.QLabel(win)
    pat_info2.setText("Clinical Information")
    pat_info2.setFont(QFont('Roboto', 12))

    formLayout.addRow(hor_info2, test_box)
    formLayout.addRow(pat_info2, test_box)
    formLayout.addRow(hor_info2, test_box)

# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_pc = QtWidgets.QLabel(win)
    pat_pc.setText("Present Complaints:")
    pat_pc.setFont(QFont('roboto', 10))

    pat_pc_1 = QtWidgets.QLineEdit(win)
    pat_pc_1.setFont(QFont('Roboto', 10))
    pat_pc_1.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_pc_2 = QtWidgets.QLineEdit(win)
    pat_pc_2.setFont(QFont('Roboto', 10))
    pat_pc_2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_pc_3 = QtWidgets.QLineEdit(win)
    pat_pc_3.setFont(QFont('Roboto', 10))
    pat_pc_3.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_pc_4 = QtWidgets.QLineEdit(win)
    pat_pc_4.setFont(QFont('Roboto', 10))
    pat_pc_4.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_pc_5 = QtWidgets.QLineEdit(win)
    pat_pc_5.setFont(QFont('Roboto', 10))
    pat_pc_5.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_pc_6 = QtWidgets.QLineEdit(win)
    pat_pc_6.setFont(QFont('Roboto', 10))
    pat_pc_6.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_ef = QtWidgets.QLabel(win)
    pat_ef.setText("Examination Findings:")
    pat_ef.setFont(QFont('Roboto', 10))

    pat_ef_1 = QtWidgets.QLineEdit(win)
    pat_ef_1.setFont(QFont('Roboto', 10))
    pat_ef_1.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_ef_2 = QtWidgets.QLineEdit(win)
    pat_ef_2.setFont(QFont('Roboto', 10))
    pat_ef_2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_ef_3 = QtWidgets.QLineEdit(win)
    pat_ef_3.setFont(QFont('Roboto', 10))
    pat_ef_3.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_ef_4 = QtWidgets.QLineEdit(win)
    pat_ef_4.setFont(QFont('Roboto', 10))
    pat_ef_4.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_ef_5 = QtWidgets.QLineEdit(win)
    pat_ef_5.setFont(QFont('Roboto', 10))
    pat_ef_5.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    pat_ef_6 = QtWidgets.QLineEdit(win)
    pat_ef_6.setFont(QFont('Roboto', 10))
    pat_ef_6.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    formLayout.addRow(pat_pc, test_box)
    formLayout.addRow(pat_pc_1, test_box)
    formLayout.addRow(pat_pc_2, test_box)
    formLayout.addRow(pat_pc_3, test_box)
    formLayout.addRow(pat_pc_4, test_box)
    formLayout.addRow(pat_pc_5, test_box)
    formLayout.addRow(pat_pc_6, test_box)

    pat_ef_1.setGeometry(100, 100, 50, 50)
    formLayout.addRow(pat_ef, test_box)
    formLayout.addRow(pat_ef_1, test_box)
    formLayout.addRow(pat_ef_2, test_box)
    formLayout.addRow(pat_ef_3, test_box)
    formLayout.addRow(pat_ef_4, test_box)
    formLayout.addRow(pat_ef_5, test_box)
    formLayout.addRow(pat_ef_6, test_box)


# ----------------------------------------------------------------------------------------------------------------------------------------------

    hor_info3 = QtWidgets.QLabel(win)
    hor_info3.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info3.setStyleSheet("border:none;")
    formLayout.addWidget(hor_info3)
# ----------------------------------------------------------------------------------------------------------------------------------------------

    label = QtWidgets.QLabel(win)
    label.setText("")

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setStyleSheet(
        "background-color:salmon;color:black;border-radius:10px;font-family:roboto;padding:5px;")
    btn_save.setText('SUBMIT')
    btn_save.clicked.connect(submit)

# ************************************************************************************************************

    pat_info11 = QtWidgets.QLabel(win)
    pat_info11.setText("Investigations")
    pat_info11.setFont(QFont('Roboto', 12))

    hor_info11 = QtWidgets.QLabel(win)
    hor_info11.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info11.setStyleSheet("border:none;")

    formLayout.addRow(pat_info11, test_box)
    formLayout.addRow(hor_info3, test_box)
# ----------------------------------------------------------------------------------------------------------------------------------------------

    cbc = QtWidgets.QLabel(win)
    cbc.setText("CBC:")

    cbc__ = QtWidgets.QLineEdit(win)
    cbc__.setFont(QFont('Roboto', 10))
    cbc__.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    lft = QtWidgets.QLabel(win)
    lft.setText("LFTs:")

    lft_ = QtWidgets.QLineEdit(win)
    lft_.setFont(QFont('Roboto', 10))
    lft_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    rft = QtWidgets.QLabel(win)
    rft.setText("RFTs:")

    rft_ = QtWidgets.QLineEdit(win)
    rft_.setFont(QFont('Roboto', 10))
    rft_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    electro = QtWidgets.QLabel(win)
    electro.setText("Electrolytes:")

    electro_ = QtWidgets.QLineEdit(win)
    electro_.setFont(QFont('Roboto', 10))
    electro_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    vm = QtWidgets.QLabel(win)
    vm.setText("Viral Markers:")

    vm_ = QtWidgets.QLineEdit(win)
    vm_.setFont(QFont('Roboto', 10))
    vm_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    imag = QtWidgets.QLabel(win)
    imag.setText("Imaging:")

    imag_ = QtWidgets.QLineEdit(win)
    imag_.setFont(QFont('Roboto', 10))
    imag_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    other__ = QtWidgets.QLabel(win)
    other__.setText("Others:")

    other_ = QtWidgets.QLineEdit(win)
    other_.setFont(QFont('Roboto', 10))
    other_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    formLayout.addRow(cbc, test_box)
    formLayout.addRow(cbc__, test_box)
    formLayout.addRow(lft, test_box)
    formLayout.addRow(lft_, test_box)
    formLayout.addRow(electro, test_box)
    formLayout.addRow(electro_, test_box)
    formLayout.addRow(vm, test_box)
    formLayout.addRow(vm_, test_box)
    formLayout.addRow(imag, test_box)
    formLayout.addRow(imag_, test_box)
    formLayout.addRow(other__, test_box)
    formLayout.addRow(other_, test_box)

# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_info4 = QtWidgets.QLabel(win)
    pat_info4.setText("Operative Notes")
    pat_info4.setFont(QFont('Roboto', 12))

    hor_info4 = QtWidgets.QLabel(win)
    hor_info4.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info4.setStyleSheet("border:none;")

    cbc1 = QtWidgets.QLineEdit(win)
    cbc1.setFont(QFont('Roboto', 10))
    cbc1.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc2 = QtWidgets.QLineEdit(win)
    cbc2.setFont(QFont('Roboto', 10))
    cbc2.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc3 = QtWidgets.QLineEdit(win)
    cbc3.setFont(QFont('Roboto', 10))
    cbc3.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc1_ = QtWidgets.QLineEdit(win)
    cbc1_.setFont(QFont('Roboto', 10))
    cbc1_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc2_ = QtWidgets.QLineEdit(win)
    cbc2_.setFont(QFont('Roboto', 10))
    cbc2_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc3_ = QtWidgets.QLineEdit(win)
    cbc3_.setFont(QFont('Roboto', 10))
    cbc3_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    hor_info40 = QtWidgets.QLabel(win)
    hor_info40.setText("")
    hor_info40.setStyleSheet("border:none;")

    formLayout.addRow(hor_info40, test_box)
    formLayout.addRow(pat_info4, test_box)
    formLayout.addRow(hor_info4, test_box)
    formLayout.addRow("Notes:", test_box)
    formLayout.addRow(cbc1, test_box)
    formLayout.addRow(cbc2, test_box)
    formLayout.addRow(cbc3, test_box)
    formLayout.addRow(cbc1_, test_box)
    formLayout.addRow(cbc2_, test_box)
    formLayout.addRow(cbc3_, test_box)
# ----------------------------------------------------------------------------------------------------------------------------------------------

    pat_info5 = QtWidgets.QLabel(win)
    pat_info5.setText("Course / Treatment")
    pat_info5.setFont(QFont('Roboto', 12))

    hor_info5 = QtWidgets.QLabel(win)
    hor_info5.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info5.setStyleSheet("border:none;")

    cbc5 = QtWidgets.QLineEdit(win)
    cbc5.setFont(QFont('Roboto', 10))
    cbc5.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc6 = QtWidgets.QLineEdit(win)
    cbc6.setFont(QFont('Roboto', 10))
    cbc6.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc7__ = QtWidgets.QLineEdit(win)
    cbc7__.setFont(QFont('Roboto', 10))
    cbc7__.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc5_ = QtWidgets.QLineEdit(win)
    cbc5_.setFont(QFont('Roboto', 10))
    cbc5_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc6_ = QtWidgets.QLineEdit(win)
    cbc6_.setFont(QFont('Roboto', 10))
    cbc6_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc7_ = QtWidgets.QLineEdit(win)
    cbc7_.setFont(QFont('Roboto', 10))
    cbc7_.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    formLayout.addRow(hor_info40, test_box)
    formLayout.addRow(pat_info5, test_box)
    formLayout.addRow(hor_info5, test_box)

    formLayout.addRow("Notes:", test_box)
    formLayout.addRow(cbc5, test_box)
    formLayout.addRow(cbc6, test_box)
    formLayout.addRow(cbc7__, test_box)
    formLayout.addRow(cbc5_, test_box)
    formLayout.addRow(cbc6_, test_box)
    formLayout.addRow(cbc7_, test_box)

# --------------------------------------------------------------------------------------------------------
    rows = 25
    colomns = 4
    hor_info50 = QtWidgets.QLabel(win)
    hor_info50.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info50.setStyleSheet("border:none;")

    pat_info6 = QtWidgets.QLabel(win)
    pat_info6.setText("Discharge Medications")
    pat_info6.setFont(QFont('Roboto', 12))

    # Create a table widget
    tableWidget = QTableWidget(win)
    tableWidget.setRowCount(rows)
    tableWidget.setColumnCount(colomns)
    tableWidget.move(50, 540)
    tableWidget.resize(450, 200)

    # Add column headers
    tableWidget.setHorizontalHeaderLabels(
        ["Medicine Name", "Dose", "Times", "Days"])
    tableWidget.setStyleSheet('''border-radius:5px;color:black;
                              background-color:#FDF6E4;height:390px;
                              width:215px;padding:0px;
                              border:1px solid white;''')

    # Add data to the table
    for row in range(rows):
        for column in range(colomns):
            item = QTableWidgetItem()
            tableWidget.setItem(row, column, item)

# ----------------------------------------------------------------------------------------------------------------------------------------------
    formLayout.addRow(hor_info40, test_box)
    formLayout.addRow(pat_info6, test_box)
    formLayout.addRow(hor_info50, test_box)
    formLayout.addRow(tableWidget, test_box)
# --------------------------------------------------------------------------------------------------------------

    pat_info7 = QtWidgets.QLabel(win)
    pat_info7.setText("Follow-Up Instructions")
    pat_info7.setFont(QFont('Roboto', 12))

    hor_info7 = QtWidgets.QLabel(win)
    hor_info7.setText("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info7.setStyleSheet("border:none;")

    hor_info7 = QtWidgets.QLabel(win)
    hor_info7.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    hor_info7.setStyleSheet("border:none;")

    cbc71 = QtWidgets.QLineEdit(win)
    cbc71.setFont(QFont('Roboto', 10))
    cbc71.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc8 = QtWidgets.QLineEdit(win)
    cbc8.setFont(QFont('Roboto', 10))
    cbc8.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc9 = QtWidgets.QLineEdit(win)
    cbc9.setFont(QFont('Roboto', 10))
    cbc9.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc712 = QtWidgets.QLineEdit(win)
    cbc712.setFont(QFont('Roboto', 10))
    cbc712.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc81 = QtWidgets.QLineEdit(win)
    cbc81.setFont(QFont('Roboto', 10))
    cbc81.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    cbc91 = QtWidgets.QLineEdit(win)
    cbc91.setFont(QFont('Roboto', 10))
    cbc91.setStyleSheet('''  width: 300px;
                        padding: 12px;
                        margin: 8px 0;
                        border: none;
                        background-color: #3CBC8D;
                        color: #333333;
                        border-radius:10px;
                                     ''')

    line_horizontal = QtWidgets.QLabel(win)
    line_horizontal.setText("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    line_horizontal.setStyleSheet("border:none;")

    sear_label = QtWidgets.QLabel(win)
    sear_label.setText("Search")
    sear_label.setFont(QFont('Roboto', 12))
    sear_label.setStyleSheet("color:white;background-color:red;")

    sear = QtWidgets.QLineEdit(win)
    sear.setFont(QFont('Roboto', 9))
    sear.setStyleSheet('''  width: 100px;
                        border: none;
                        background-color: #3CBC8D;
                        color: white;
                        border-radius:10px;
                        background-image: url("searchicon.png");
                        background-repeat: no-repeat;
                        padding: 10px;
                                     ''')

    label2 = QtWidgets.QLabel("red", win)
    label2.setText("")

    btn_pdf = QtWidgets.QPushButton(win)
    btn_pdf.setStyleSheet(
        "background-color:salmon;color:black;border-radius:10px;font-family:roboto;padding:5px;")
    btn_pdf.setText('SEARCH')
    btn_pdf.clicked.connect(search)
    btn_pdf.move(1210, 670)
# -------------------------------------------------------------------------------------------------------------
    formLayout.addRow(hor_info40, test_box)
    formLayout.addRow(pat_info7, test_box)
    formLayout.addRow(hor_info7, test_box)
    formLayout.addRow("Instructions:", test_box)
    formLayout.addRow(cbc71, test_box)
    formLayout.addRow(cbc8, test_box)
    formLayout.addRow(cbc9, test_box)
    formLayout.addRow(cbc712, test_box)
    formLayout.addRow(cbc81, test_box)
    formLayout.addRow(cbc91, test_box)

    formLayout.addRow(btn_save, test_box)
    formLayout.addRow(label, test_box)

    formLayout.addRow(hor_info40, test_box)
    formLayout.addRow(sear_label, test_box)
    formLayout.addRow(line_horizontal, test_box)
    formLayout.addRow("Enter Hospital Number:", test_box)
    formLayout.addRow(sear, test_box)
    formLayout.addRow(btn_pdf, test_box)
    formLayout.addRow(label2, test_box)

    formLayout.setVerticalSpacing(10)
    groupbox.setLayout(formLayout)
    groupbox.setStyleSheet("width:100px")

    scroll = QScrollArea(win)
    scroll.setWidget(groupbox)
    scroll.setWidgetResizable(True)

    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    print(width, height)

    scroll.setFixedHeight(height-20)
    scroll.setFixedWidth(width-20)
    scroll.setWidgetResizable(True)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

# ***************************************************************************************************************
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
