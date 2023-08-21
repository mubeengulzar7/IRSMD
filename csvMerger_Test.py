import pandas as pd
import glob
import os

from datetime import datetime

# current date
now = str(datetime.now().strftime('%Y-%m-%d')) 

# setting the path for joining multiple files
files = os.path.join("C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\ScanReportsTest\ProductionScanReports"+now, "*.csv")

# list of merged files returned
files = glob.glob(files)

print("Joining all CSV files at the specified location...");

#print("Resultant CSV after joining all CSV files at the specified location...: Output\CombinedReports\CombinedReport"+now+".csv");

# joining files with concat and read_csv
combinecsv = pd.concat(map(pd.read_csv, files), ignore_index=True)
#print(combinecsv)
# saving the combined csv in a specified location
combinecsv.to_csv( "C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\CombinedReportsTest\CombinedReport"+now+".csv", index=False, encoding='utf-8')