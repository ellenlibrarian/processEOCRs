# processEOCRs
This script goes through a file of EOCR records from YBP (in MARC format) and writes unique purchase order ids to a text file. It also splits the large file of records into smaller files with only one PO per file. This is useful for us because we have multiple records associated with one PO.

Requires os, pymarc
