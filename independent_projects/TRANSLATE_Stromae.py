from configparser import ConfigParser
import os
import sys


parser = ConfigParser()
#parser.read('./setup/user.ini')
parser.read('/home/delora/github/data_science_public/setup/user.ini')
local_repo_loc=parser.get('file_locations', 'local_repo_dir')
local_repo_loc=local_repo_loc[1:-1]

sys.path.append(local_repo_loc)
print('The repo is located at')
print(local_repo_loc)

sys.path.append(local_repo_loc+os.sep+'dk_toolboxes')
print('The repo is located at')
print(local_repo_loc+os.sep+'dk_toolboxes')


import dk_toolboxes.web_tools as web_tools
import strategies.inputs_file as InF


##################################################




##################################################
#input: song URL, output: file of lyrics and machine translation

#extract bulk text from the web
URL='https://lyrics.az/stromae/racine-carrie/papaoutai.html'
filename=web_tools.AZ_lyrics_puller(URL)
bulk_text=InF.read_resource(filename)
#############################################
# use transformer to predict bulk_text
#
#
#
