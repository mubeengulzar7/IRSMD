import encodings
import pandas as pd 
#import pdfkit
from fpdf import FPDF
from csv2pdf import convert
import csv
from datetime import datetime



# current date
now = str(datetime.now().strftime('%Y-%m-%d'))


convert("C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\CombinedReportsTest\CombinedReportsCutTest\CombinedReport"+now+".csv", "C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\EmailPDFTest\CombinedReport"+now+".pdf", align="L")