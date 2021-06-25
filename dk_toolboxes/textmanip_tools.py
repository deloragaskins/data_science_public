from re import search
import re
###############################################################################
################################################################################
#SECTION: REFORMAT
################################################################################
#rext to text
def remove_URL(text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'URL',text)
def relabel_mention(text):
    at=re.compile(r'@')
    return at.sub(r'USRTAG ',text)
def remove_newline(text):
    at=re.compile(r'\n')
    return at.sub(r' ',text)
def replace_separators(text):
    at1=re.compile(r'ÛÒ')
    at2=re.compile(r'ÛÓ')
    at1.sub(r'***',text)
    return at2.sub(r'***',text)

def df_txt_cleaner(text):
    text=remove_URL(text)
    text=relabel_mention(text)
    text=remove_newline(text)
    text=replace_separators(text)

    return text
################################################################################
#rext to int
def name_to_id(name):
        id=[]
        firstandlast3=[0, 1, 2,-3, -2, -1]
        for letter in firstandlast3:
            str(name)
            let=name[letter]
            id.append(ord(let))

        strings = [str(integer) for integer in id]
        a_string = "".join(strings)
        an_integer = int(a_string)

        return an_integer

################################################################################
################################################################################
#SECTION:EXTRACT
################################################################################

def collect_keywords_simplified2(text,keyword_list):
    keyword_list=keyword_list.split()
#     print(keyword_list)
    keyword_collected=' '
    tokencounter=0

    doc = text.split()
    for token in doc:

        for keyword in keyword_list:
            if search('%20', str(keyword)):
                if tokencounter<len(doc)-1:
                    combi=token.lower()+'%20'+doc[tokencounter+1].lower()
                    if combi==keyword:
                         keyword_collected=keyword_collected+' '+str(keyword)
            elif search(str(keyword), token.lower()):
                keyword_collected=keyword_collected+' '+str(keyword)
        tokencounter+=1

    if keyword_collected==' ':
#         text=np.nan  #if want to drop by NaNs
        text=' '
    else:
        text=keyword_collected
        text.lower
    return text
