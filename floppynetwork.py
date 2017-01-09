import os 
print
print "BBBBBBBBBBBBBBBBBBBBBBBBBBB"
print "BMB---------------------BBB"
print "BBB----THE--------------BBB"
print "BBB----FLOPPY-----------BBB"
print "BBB----NETWORKS---------BBB"
print "BBB---------------------BBB"
print "BBB----V1.6-------------BBB"
print "BBBBBBBBBBBBBBBBBBBBBBBBBBB"
print "BBBBB++++++++++++++++BBBBBB"
print "BBBBB++BBBBB+++++++++BBBBBB"
print "BBBBB++BBBBB+++++++++BBBBBB"
print "BBBBB++BBBBB+++++++++BBBBBB"
print "BBBBB++++++++++++++++BBBBBB"
print
print "Assembled by Thomas Walskaar 2016"
print "thomas@walska.com"
print 
print "Never underestimate the bandwidth"
print "of a station wagon full of floppy discs" 
print "hurtling down the highway."
# Pick website, store in your own path and run script. Remember to check name of floppy disc volume
print
os.system("pandoc -s -r html /URL/ -o floppy.text")
# HTML to Markdown
os.system("pandoc floppy.text -o floppy.epub")
# Markdown to epub
os.system("pandoc floppy.epub -t plain -o floppy.txt")
# ePub to Textfile
print 
print ">>>>>> SAVING TO FLOPPY"
print
# moving file to floppy disc
os.system("mv /Users/thomaswalskaar/Documents/_Projects/Lust\ Workshop/FN_finished floppy.txt /Volumes/Media/")
print
os.system("rm floppy.text")
# deleting markdown file
os.system("rm floppy.epub")
# deleting epub file
print
print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
print "$$$$$$$$$$   >>> END <<<  $$$$$$$$$"
print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
