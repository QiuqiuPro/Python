#!/usr/bin/env python3
import sys
import re
import webbrowser as Safari # http://stackoverflow.com/questions/4752473/opening-and-using-safari

s = sys.argv
url = s[1]

ja_url = re.sub( r'/#[a-zA-Z-_]+/', '/#ja/', url )

Safari.open( ja_url )
