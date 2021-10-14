from transformers import MarianTokenizer, AutoModelForSeq2SeqLM
import sys

from configparser import SafeConfigParser
parser = SafeConfigParser()
parser.read('./setup/user.ini')
repo_loc=parser.get('file_locations', 'local_repo_dir')
repo_loc=repo_loc[1:-1]
sys.path.append(repo_loc)


import dk_toolboxes.web_tools as web_tools
import strategies.inputs_file as InF


#extract text to use for translation( and save to file)
URL ='https://lyrics.az/stromae/racine-carrie/papaoutai.html'
filename=web_tools.AZ_lyrics_puller2(URL)
text =InF.read_resource(filename)
translated_text=text.copy()



# #setup the ML model
mname = 'Helsinki-NLP/opus-mt-fr-en'
tokenizer = MarianTokenizer.from_pretrained(mname)
model = AutoModelForSeq2SeqLM.from_pretrained(mname)

#loop through and translate the text
for counter1 in range(len(text)):
    #print(text[counter1])
    input_ids = tokenizer.encode(text[counter1],return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    translated_text[counter1]=decoded

#print(translated_text)


# save output to file
filename_out=filename[:-4]+'en_trans.txt'
with open(filename_out, 'w+') as f:
     # f.write(translated_text)
     for counter2 in range(len(text)):
         f.write('\n')
         f.write(text[counter2] +'/'+translated_text[counter2])
         f.write('\n')


print('text saved at: ' +'\n'+filename)
