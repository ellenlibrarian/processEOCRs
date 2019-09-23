# This script goes through a file of EOCR records from YBP (in MARC format) and writes unique PO ids to a text file. It also splits the large file of records into smaller files with only one PO per file.
# requires os, pymarc

def extractPOs() :
  import os
  # get rid of an old PO file if present
  if os.path.exists("POs.txt") :
      os.remove("POs.txt")
  nowname = "0"
  with open(fname, "rb") as fh:
    reader = MARCReader(fh)
    # loop through records and find PO - write to file if it has not already been found and written.
    for record in reader:
        newname = record['961']['a']
        if newname != nowname :
            with open("POs.txt", "a") as fout:
              fout.write(newname + "\n")
        nowname = newname

def splitEOCRS() :
  with open(fname, "rb") as fh:
    reader = MARCReader(fh)
    for record in reader:
        newname = record['961']['a']
        nowname = newname
        if newname == nowname :
            with open(nowname + '.mrc', 'ab') as out:
                  out.write(record.as_marc())
        nowname = newname

from pymarc import MARCReader
fname = input("Enter file name: ")
extractPOs()
splitEOCRS()
