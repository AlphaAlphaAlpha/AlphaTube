#!/usr/bin/env python
#
from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear && clear && clear")
logo = '''
    \033[0m  \033[32m   \033[1m              .oo 8        8               ooooo        8             
    \033[0m  \033[32m   \033[1m             .P 8 8        8                 8          8             
    \033[0m  \033[32m   \033[1m            .P  8 8 .oPYo. 8oPYo. .oPYo.     8   o    o 8oPYo. .oPYo. 
    \033[0m  \033[32m   \033[1m           oPooo8 8 8    8 8    8 .oooo8     8   8    8 8    8 8oooo8 
    \033[0m  \033[32m   \033[1m          .P    8 8 8    8 8    8 8    8     8   8    8 8    8 8.     
    \033[0m  \033[32m   \033[1m         .P     8 8 8YooP' 8    8 `YooP8     8   `YooP' `YooP' `Yooo' 
    \033[0m  \033[32m   \033[1m        ..:::::.... 8 ....:..:::..:.....:::::..:::.....::.....::.....:
    \033[0m  \033[32m   \033[1m        ::::::::::: 8 ::::::::::::::::::::::::::::::::::::::::::::::::
    \033[0m  \033[32m   \033[1m        :::::::::::...::::::::::::::::::::::::::::::::::::::::::::::::

   \033[0m  \033[34m   \033[1m     }--{+} Coded By Manisso the original pytube creator. }--{+} 		    
   \033[0m  \033[34m   \033[1m     }--{+} Updatet by Alpha                              }--{+}	         	     
   \033[0m  \033[34m   \033[1m     }--{+} Lets download some stuff. 		            }--{+} 	     
   \033[0m  \033[34m   \033[1m     }--{+} supported platforms see Text                  }--{+}
'''
menu = '''\033[5m \033[31m \033[1m
    {1}--Video Download
    {2}--Audio Download
    {3}--Audio PlayList Download

    {0}-Exit
 '''
print logo
print menu


def quit():
    con = raw_input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        print logo
        print menu
        select()


def select():
    try:
        choice = input("SnapTub~# ")
        if choice == 1:
            os.system("clear")
            print """
  \033[5m  \033[36m   \033[1m  o     o  o      8               
  \033[5m  \033[36m   \033[1m  8     8         8               
  \033[5m  \033[36m   \033[1m  8     8  8 .oPYo8 .oPYo. .oPYo. 
  \033[5m  \033[36m   \033[1m  `b   d'  8 8    8 8oooo8 8    8 
  \033[5m  \033[36m   \033[1m   `b d'   8 8    8 8.     8    8 
  \033[5m  \033[36m   \033[1m    `8'    8 `YooP' `Yooo' `YooP' 
  \033[5m  \033[36m   \033[1m  :::..::::..:.....::.....::.....:
  \033[5m  \033[36m   \033[1m  ::::::::::::::::::::::::::::::::
  \033[5m  \033[36m   \033[1m  ::::::::::::::::::::::::::::::::
PUT URL HERE: https://www.youtube.com/watch?v=PYJHFVBsmeQ
"""
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            print("")
            quit()
        elif choice == 2:
            os.system("clear")
            print """
\033[5m  \033[36m   \033[1m   /$$$$$$                  /$$ /$$
\033[5m  \033[36m   \033[1m  /$$__  $$                | $$|__/
\033[5m  \033[36m   \033[1m | $$  \ $$ /$$   /$$  /$$$$$$$ /$$  /$$$$$$
\033[5m  \033[36m   \033[1m | $$$$$$$$| $$  | $$ /$$__  $$| $$ /$$__  $$
\033[5m  \033[36m   \033[1m | $$__  $$| $$  | $$| $$  | $$| $$| $$  \ $$
\033[5m  \033[36m   \033[1m | $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$
\033[5m  \033[36m   \033[1m | $$  | $$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$/
\033[5m  \033[36m   \033[1m |__/  |__/ \______/  \_______/|__/ \______/

PUT URL HERE: https://www.youtube.com/watch?v=PYJHFVBsmeQ
"""
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            quit()
        elif choice == 3:
            os.system("clear")
            print("""
\033[5m  \033[36m   \033[1m  /$$$$$$$  /$$                     /$$ /$$             /$$
\033[5m  \033[36m   \033[1m | $$__  $$| $$                    | $$|__/            | $$
\033[5m  \033[36m   \033[1m | $$  \ $$| $$  /$$$$$$  /$$   /$$| $$ /$$  /$$$$$$$ /$$$$$$
\033[5m  \033[36m   \033[1m | $$$$$$$/| $$ |____  $$| $$  | $$| $$| $$ /$$_____/|_  $$_/
\033[5m  \033[36m   \033[1m | $$____/ | $$  /$$$$$$$| $$  | $$| $$| $$|  $$$$$$   | $$
\033[5m  \033[36m   \033[1m | $$      | $$ /$$__  $$| $$  | $$| $$| $$ \____  $$  | $$ /$$
\033[5m  \033[36m   \033[1m | $$      | $$|  $$$$$$$|  $$$$$$$| $$| $$ /$$$$$$$/  |  $$$$/
\033[5m  \033[36m   \033[1m |__/      |__/ \_______/ \____  $$|__/|__/|_______/    \___/
\033[5m  \033[36m   \033[1m                          /$$  | $$
\033[5m  \033[36m   \033[1m                         |  $$$$$$/
\033[5m  \033[36m   \033[1m                          \______/

PUT URL HERE: https://www.youtube.com/watch?v=lp-EO5I60KA&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj
""")
            d3 = raw_input('playlist URL: ')
            os.system("clear")
            os.system("youtube-dl -cit --extract-audio --audio-format mp3 " + d3)
            print("")
            quit()
    except(KeyboardInterrupt):
        print ""


select()
