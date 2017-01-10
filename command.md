# Copy & paste this command in terminal
# BUG:Import OS in python is not working due to '$' hence can't be integrated with python 
# Open terminal in the forked folder




# {1..225} downloads all pages from 1-225
for i in {1..225}; do wget      --recursive      --no-clobber --html-extension      --convert-links      --restrict-file-names=windows      --domains ebook-dl.com      --include /item      --reject *.jpg,*.zip      --reject-regex http://ebook-dl.com/download      http://ebook-dl.com/computer/page/$i;done


