#!/bin/bash
#!/bin/python

figlet -c IRSMD #banner

echo "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"

printf "\n"

mkdir Output/ScanReports/"ProductionScanReports$(date +"%Y-%m-%d")" # creating a directory for Scan Reports with current Date

dir_path=$(ls -t Output/ScanReports/ |grep ProductionScanReports | head -1) # storing the name of the newly created directory for Output Path

echo "Scans Directory Path = Output/ScanReports/$dir_path"

input="queries.txt" #reading queries line by line from this text file
while IFS= read -r line
do
  printf "\n"
  echo "Query = $line"
  printf "\n"
  python search_engines_cli.py -q $line -e google,bing,dogpile,duckduckgo,aol,ask,yahoo,mojeek,startpage -p 20 -o csv -n Output/ScanReports/$dir_path/$line -f host  #Adjust input according to the desired output
  printf "\n"
  echo "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
  printf "\n"
done < "$input"

sleep 1

echo "Merging CSV Reports"

printf "\n"

python csvMerger.py # merging all the csv reports into 1 and storing it into a specified location

printf "\n"

sleep 1

echo "Cutting Unnecessary Data"

printf "\n"

# Applying cut and grep to extract only the required columns and links
# cut -d "," -f1-4 Output/CombinedReports/CombinedReport$(date +"%Y-%m-%d").csv | grep -i -v '/login' > Output/CombinedReports/CombinedReport$(date +"%Y-%m-%d").csv 

sleep 1

cut -d "," -f1-4 Output/CombinedReports/CombinedReport$(date +"%Y-%m-%d").csv > Output/CombinedReports/CombinedReportsCut/CombinedReport$(date +"%Y-%m-%d").csv

sleep 1

echo "Cutting Done"

sleep 1

printf "\n"

# PDF conversion

echo "PDF conversion"

#python csvtoPDF.py
python csvtoPDF_RE.py

sleep 1

printf "\n"

echo "Conversion Done"

printf "\n"

#echo "Outputfile: Output/EmailPDF/"

echo "Sending Email"

sleep 1

python EmailSender.py
