import pandas as pd 
import pdfkit
from datetime import datetime

# current date
now = str(datetime.now().strftime('%Y-%m-%d'))

# Reading csv file for conversion into html
CSV = pd.read_csv("C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\CombinedReports\CombinedReport"+now+".csv")  

# html converted outputs
CSV.to_html("C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\CombinedReports\CombinedReport"+now+".html")  

# path to wkhtmltopdf installation
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# converting html into pdf for email
pdfkit.from_file("C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\CombinedReports\CombinedReport"+now+".html", "C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\EmailPDF\CombinedReport"+now+".pdf" , configuration=config)