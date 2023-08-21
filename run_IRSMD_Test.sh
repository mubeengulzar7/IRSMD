#!/bin/bash
#!/bin/python

figlet -c IRSMD #banner

echo "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"

printf "\n"

mkdir Output/ScanReportsTest/"ProductionScanReports$(date +"%Y-%m-%d")" # creating a directory for Scan Reports with current Date

dir_path=$(ls -t Output/ScanReportsTest/ |grep ProductionScanReports | head -1) # storing the name of the newly created directory for Output Path

echo "Scans Directory Path = Output/ScanReportsTest/$dir_path"

input="queriestest.txt" #reading queries line by line from this text file

while IFS= read -r line
do
  printf "\n"
  echo "Query = $line"
  printf "\n"
  python search_engines_cli.py -q $line -e google,bing -p 3 -n Output/ScanReportsTest/$dir_path/$line -o csv -f host  #Adjust input according to the desired output
  printf "\n"
  echo "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
  printf "\n"
done < "$input"

python csvMerger_Test.py # merging all the csv reports into 1 and storing it into a specified location

printf "\n"

echo "Cutting and Grepping..."

printf "\n"

sleep 1

cut -d "," -f1-4 Output/CombinedReportsTest/CombinedReport$(date +"%Y-%m-%d").csv > Output/CombinedReportsTest/CombinedReportsCutTest/CombinedReport$(date +"%Y-%m-%d").csv

sleep 1

#cut -d "," -f1-4 Output/CombinedReports/CombinedReport$(date +"%Y-%m-%d").csv | grep -i -v 'doodle' > Output/CombinedReports/CombinedReport$(date +"%Y-%m-%d").csv 

#echo "Outputfile: Output/CombinedReports/"

printf "\n"

# PDF conversion

echo "PDF conversion"

#python csvtoPDF.py
python csvtoPDF_RETest.py

sleep 1
#echo "Outputfile: Output/EmailPDF/"

# Sending Email

python EmailSender_Test.py

#echo "Email has been Sent"