#!/bin/python3

import sys, os


def install():
    """
    Installs the script on /usr/local/bin
    """


def search(arguments):
    """
    Search looks for the following arguments:
    -d 'directory' if unspecified then use current working folder
    -e 'extension' search for the string on files with this extension. This is required!
    -s 'search string' this is the search string you are looking for. This is also required!
    """

    find = lambda d, e, s: os.system('find directory -type f -name "*.extension" -exec grep -l "$search_string" {} + 2>/dev/null'.replace('extension', e))
    
    search_string="<script>"

# Using find to locate all .py files and then using grep to search for the string
find . -type f -name "*.html" -exec grep -l "$search_string" {} + 2>/dev/null

# Check if any files were found
if [ $? -eq 0 ]; then
  echo "String found in the above file(s)."
else
  echo "String not found in any files."
fi
    pass


if __name__ == "__main__":
    search(sys.argv)
