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


def pdfGenerate(wordList):
    if 1:
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
        my_canvas.setFont('Helvetica', 9.5)
        my_canvas.drawString(50, 460+70, wordList[8])
        # my_canvas.rect(40, 440, 530, 120, stroke=1, fill=0)

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(50, 420+70-50, 'Examination Findings')
        my_canvas.setFont('Helvetica', 9.5)
        my_canvas.drawString(50, 400+70-50, wordList[9])
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

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawString(40, 265-100, wordList[16])
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

        my_canvasT.setFont('Helvetica', 9.5)
        my_canvasT.drawString(40, 660, wordList[17])
        # my_canvas.rect(310, 210, 220, 50, stroke=1, fill=0)
# ------------------------------------------------------------------------------
        my_canvasT.setFont('Helvetica', 13)
        my_canvasT.drawString(30, 198+300, 'Discharge Medicines')

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
        # my_canvasT.rect(30, 60+300, 550, 135, stroke=1, fill=0)
        my_canvasT.drawString(40, 25+300, wordList[18])

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

        os. system("C:\\Users\\"+str(y)+"\\Downloads\\" +
                   wordList[0]+"_"+wordList[6]+".pdf")


word = []
for i in range(61):
    word.append("")
pdfGenerate(word)
