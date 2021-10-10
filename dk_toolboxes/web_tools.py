import requests
from bs4 import BeautifulSoup
import urllib.request
import nltk



import strategies.outputs_file as OutF



def AZ_lyrics_puller(URL):
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open(URL)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    #print(soup.p)
    all_tags=soup.find_all("p")
    for counter1 in range(len(all_tags)):
        #print(counter1)
        printery=all_tags[counter1].attrs
        printery=type(printery)
        #print(printery)

        #print(counter1)
        tag_text_counter=all_tags[counter1].get_text()
        key='class'
        if all_tags[counter1].has_attr(key):
            #print(all_tags[counter1].get(key))
            if all_tags[counter1].get(key)== ['lyric-text']:
                #print(tag_text_counter)
                text_block=tag_text_counter
        #if div_text_counter=='LYRICS.AZ APPLICATION':
        #  text_block=all_divs[counter1+1].get_text()
        #  print(text_block)

    websourcechoice='AZ_lyrics'
    outpath=OutF.outpath_websource(websourcechoice)
    #
    identifier=soup.title.string
    identifier=identifier.replace("AZ Lyrics.az | ", "")

    print(identifier)
    filename=outpath+identifier+'.txt'

    sentences_list=nltk.sent_tokenize(text_block)
    with open(filename, 'w+') as f:
        # for sentence in sentences_list:
        #     f.write(sentence)
        #     f.write('\n')

         f.write(text_block)

    print('text saved at: ' +'\n'+filename)

    return filename
