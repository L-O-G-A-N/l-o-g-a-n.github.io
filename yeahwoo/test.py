# A tool I made so that adding games are easier to add, Will probably be useless for anyone else
import os
from pathlib import Path
import shutil
bigfile = """
   <!DOCTYPE html>
<html>
  <head>
    <title>🎮LFGAN'S GAMES🎮 - APPS</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    body, h1,h2,h3,h4,h5,h6 {font-family: "Montserrat", sans-serif}
    .w3-row-padding img {margin-bottom: 12px}
    /* Set the width of the sidebar to 120px */
    .w3-sidebar {width: 120px;background: #222;}
    /* Add a left margin to the "page content" that matches the width of the sidebar (120px) */
    #main {margin-left: 120px}
    /* Remove margins from "page content" on small screens */
    @media only screen and (max-width: 600px) {#main {margin-left: 0}}
    {
  boz-sizing: border-box;
}

.button {
  background: #fff;
  border-radius: 6px;
  display: inline-block;
  padding: 10px;
  text-align: center;
  max-width: 150px;
  text-decoration: none;
}

.button figure {
  margin: 0 0 15px;
}

.button figure img {
  border-radius: 100%;
}

.button .text {
  font-weight: bold;
  text-transform: uppercase;
  color: #1d368a;
  margin: 0 0 15px;
  font-size: 16px;
}
    </style>
  </head>
<body class="w3-black">

<!-- Icon Bar (Sidebar - hidden on small screens) -->
<nav class="w3-sidebar w3-bar-block w3-small w3-hide-small w3-center">
  <!-- Avatar image in top left corner -->
  <img src="https://i.imgur.com/9nAjbup.png" style="width:100%">

  <a href="./index.html" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
    <i class="fa fa-home w3-xxlarge"></i>
    <p>Home</p>
  </a>
  <a href="./Games.html" class="w3-bar-item w3-button w3-padding-large w3-black">
    <i class="fa fa-keyboard-o w3-xxlarge"></i>
    <p>Games</p>
  </a>
  <a href="./Apps.html" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
    <i class="fa fa-laptop w3-xxlarge"></i>
    <p>Apps & Bookmarklets</p>
  </a>
  <a href="./LegalContact.html" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
    <i class="fa fa-envelope w3-xxlarge"></i>
    <p>Legal & Contact</p>
  </a>
</nav>

<!-- Navbar on small screens (Hidden on medium and large screens) -->
<div class="w3-top w3-hide-large w3-hide-medium" id="myNavbar">
  <div class="w3-bar w3-black w3-opacity w3-hover-opacity-off w3-center w3-small">
    <a href="./index.html" class="w3-bar-item w3-button" style="width:25% !important">Home</a>
    <a href="./Apps.html" class="w3-bar-item w3-button" style="width:25% !important">Games</a>
    <a href="./Games.html" class="w3-bar-item w3-button" style="width:25% !important">Apps & Bookmarklets</a>
    <a href="./LegalContact.html" class="w3-bar-item w3-button" style="width:25% !important">Legal & Contact</a>
  </div>
</div>

<!-- Page Content -->
<div class="w3-padding-large" id="main">
  <!-- Header/Home -->
  <header class="w3-container w3-padding-32 w3-center w3-black" id="home">
    <h1 class="w3-jumbo"><span class="w3-hide-small">Lfgan's</span> Games</h1>
    <p>Free, Unblocked Games</p>
    <iframe src="https://raw.githack.com/3kh0/3kh0-assets/main/PLEASEREPLACEMEWITHTHEGAMETHATYOUARETRYINGTOREPLACEMEWITHAWUFIAWUIFIGUWAFGIUAW" width="1200" height="800" />
    <img src="https://i.imgur.com/9nAjbup.png" alt="boy" class="w3-image" width="992" height="1108">
  </header>

  <!-- About Section -->
    
    <!-- Grid for pricing tables -->

  


</body>
</html>
"""

empty = 0


def yeah(path):
     path = path.replace("\\", "/")
         # Get list of all files only in the given directory
     fun = lambda x : os.path.isfile(os.path.join(path,x))
     files_list = filter(fun, os.listdir(path))
 
     # Create a list of files in directory along with the size
     size_of_file = [
        (f,os.stat(os.path.join(path, f)).st_size)
        for f in files_list
        ]
     for f,s in size_of_file: # file and size
             gamename = Path(path).absolute().name
             if round(s/(1*1),3) > 10000000:

                    if os.path.isfile(path+'\index.html'):
                     index12321 = "index.html"
                    elif os.path.isfile(path+r"\\"+ gamename + ".html"):
                        index12321 = gamename + ".html"
                    else:
                     index12321 = input("Couldn't Find index.html in " + path+" Please enter the correct file name: ")
                    f = open("{}.html".format(gamename),"w",encoding="utf-8")
                    f.write(bigfile.replace("PLEASEREPLACEMEWITHTHEGAMETHATYOUARETRYINGTOREPLACEMEWITHAWUFIAWUIFIGUWAFGIUAW","{}/{}".format(gamename,index12321)))
                    f.close()
                    shutil.rmtree(path)
                    print("Deleted Path: "+path)
                    print("Created: " + gamename + ".html")
             else:
             
                     if not os.path.isfile(gamename + ".html"):
                      if os.path.isfile(path+'\index.html'):
                       index12321 = "index.html"
                      elif os.path.isfile(path+r"\\"+ gamename + ".html"):
                        index12321 = gamename + ".html"
                      else:
                       index12321 = input("Couldn't Find index.html in " + path+" Please enter the correct file name: ")
                      f = open("{}.html".format(gamename),"w",encoding="utf-8")
                      f.write(bigfile.replace("https://raw.githack.com/3kh0/3kh0-assets/main/PLEASEREPLACEMEWITHTHEGAMETHATYOUARETRYINGTOREPLACEMEWITHAWUFIAWUIFIGUWAFGIUAW",'./{}/{}'.format(gamename,index12321) ))
                      f.close()
                      print("Created: " + gamename + ".html")
                     elif os.path.isfile(gamename + ".html"):
                         empty = 0




rootdir =  (r'C:\Users\Logan\Desktop\Newfolder')
for it in os.scandir(rootdir):
    if it.is_dir():
          yeah(it.path)
