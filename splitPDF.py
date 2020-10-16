#!/usr/bin/python3

# -*- coding: utf-8 -*-
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def split_pdf(filename, slices):
  pdf_reader = PdfFileReader(open(filename, "rb"))
  slicesList = open(slices)

  for line in slicesList:
    try:
      sliceArr = line.strip().split(':')
      startPage = int(sliceArr[0]) - 1
      finishPage = int(sliceArr[1])

      assert startPage > 0
      assert finishPage < pdf_reader.numPages
      pdf_writer = PdfFileWriter()

      for page in range(startPage, finishPage):
        pdf_writer.addPage(pdf_reader.getPage(page))

      left = ""
      right = ""

      if len(sliceArr[0]) == 1:
        left = "00" + sliceArr[0]
      elif len(sliceArr[0]) == 2:
        left = "0" + sliceArr[0]
      elif len(sliceArr[0]) == 3:
        left = sliceArr[0]

      if len(sliceArr[1]) == 1:
        right = "00" + sliceArr[1]
      elif len(sliceArr[1]) == 2:
        right = "0" + sliceArr[1]
      elif len(sliceArr[1]) == 3:
        right = sliceArr[1]

      output = left + "-" + right + ".pdf"
      print(output)

      f = open(output, "wb")
      pdf_writer.write(f)
      f.close()


    except AssertionError as e:
      print("Error: The PDF you are cutting has less pages than you want to cut!")

filename = sys.argv[1]
slices =  sys.argv[2]
split_pdf(filename, slices)
