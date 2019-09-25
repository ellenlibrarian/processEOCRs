# This script goes through a file of EOCR records from YBP (in MARC format) and writes unique PO ids to a text file. It also splits the large file of records into smaller files with only one PO per file. If a record is missing a PO, it writes an error message to the text file and writes the records to a file.

# Requires datetime, pymarc

def extractRecords():
    nowname = "0"
    with open(fname, "rb") as fh:
        reader = MARCReader(fh)
        for record in reader:
            try :
                newname = record['961']['a']
                if newname != nowname :
                    with open(newname + ".mrc", "ab") as out:
                        out.write(record.as_marc())
            except :
                with open ("UL__NoPO-" + str(shortdate) + ".mrc", "ab") as out:
                    out.write(record.as_marc())
        nowname = newname

def extractPOs():
    nowname = "0"
    count = 0
    with open(fname, "rb") as fh:
        reader = MARCReader(fh)
        for record in reader:
            count = count + 1
            try :
                newname = record['961']['a']
                if newname != nowname :
                    with open("UL___POs-" + str(shortdate) + ".txt", "a") as fout:
                        fout.write(newname + "\n")
                nowname = newname
            except :
                with open("UL___POs-" + str(shortdate) + ".txt", "a") as fout:
                    fout.write("***PO missing from record*** Record written to UL___POs-" + str(shortdate) + ".txt" + "\n")
        with open("UL___POs-" + str(shortdate) + ".txt", "a") as fout:
                fout.write("\nTotal records: " + str(count) + "\n")

from pymarc import MARCReader
from datetime import date

fname = input("Enter file name: ")
today = date.today()
shortdate = today.strftime("%m-%d-%y")

extractRecords()
extractPOs()
