# A tool I made so that adding games are easier to add, Will probably be useless for anyone else
import os 
dir_list = os.listdir()
aaaaaaaa = open("dsfsdfsedfgsegesgsedgesgsegsegesgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgsgssssssssss.txt","a")
template = """
    <a href="./AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.html" class="button">
  <figure><img width="100" height="100" src="./AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/splash.png"></figure>
  <div class="text">
    1v1.lol (HARDCODED)
  </div>
</a>

"""
for x in dir_list:
 aaaaaaaa.write(template.replace("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", x))