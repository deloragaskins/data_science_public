##################################################
########################################################
benchmark_text_en=["Hello my friends! How are you doing today?",
"Sir, please sit down. ",
"sister, sit down please.",
"chill out, bro.",
"I'll have a coffee.",
"Follow the rules.",
"watch out!"]
###################################################################
#https://www.machinecurve.com/index.php/2021/02/16/easy-machine-translation-with-machine-learning-and-huggingface-transformers/
# from transformers import pipeline
#
# # Init translator
# translator = pipeline("translation_en_to_fr")
#
# # Translate text
# text = benchmark_text_en
# translation = translator(text)
#
# # Print translation
# print(translation)
##########################################################
# translation=[{'translation_text': "Bonjour, mes amis, comment allez-vous aujourd'hui?"},
#  {'translation_text': "Monsieur le Président, s'il vous plaît vous asseoir"},
#  {'translation_text': 'sur, sil vous plaît sasseoir'},
#  {'translation_text': "J'ai un café"},
#  {'translation_text': 'Suivre les règles'},
#  {'translation_text': 'surveiller !'}]

#observations:
#formality levels aren't caught, and very informal isn't translated
#phrases which require the verbs to change in translation arent caught
#shift of prnouns from  mes amis to les amis isn't caught
# "watch out", which indicates potential danger, should probably be "attention"

#Overall, the text is being translated in a literal manner, rather than a more natural rendering that would occur
# further to the right of the folloeing translation tyoes:
#INTERLINEAR-LITERAL-FAITHFUL-BALANCED-FREE

#for more details about the scale refer to:
#English-French Translation: A Practical Manual
#Christophe Gagne, Emilia Wilton-Godberfforde
#############################################################3
# "Bonjour mes amis ! Comment allez-vous aujourd'hui ?",
# "Monsieur, asseyez-vous s'il vous plaît",
# "soeur, asseyez-vous s'il vous plaît",
# "Détendez-vous, mon frère",
# "Je vais prendre un café",
# "Suivez les règles",
# "Fais attention !"

#https://www.deepl.com/translator





##########################################################

# Next step try pretrained tokenizer and model on benchmark sentences
#works for single sentences

from transformers import MarianTokenizer, AutoModelForSeq2SeqLM

text = benchmark_text_en[4]
print(text)
mname = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(mname)
model = AutoModelForSeq2SeqLM.from_pretrained(mname)
input_ids = tokenizer.encode(text,return_tensors="pt")
outputs = model.generate(input_ids)
decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded)

#################################################################
#next step try for multiple sentences
#https://huggingface.co/course/chapter2/5?fw=pt

# from transformers import MarianTokenizer, AutoModelForSeq2SeqLM
#
# text = ' '.join([str(elem) for elem in benchmark_text_en[:2]])
# #text=benchmark_text_en[0]
# print(text)
# mname = 'Helsinki-NLP/opus-mt-en-fr'
# tokenizer = MarianTokenizer.from_pretrained(mname)
# model = AutoModelForSeq2SeqLM.from_pretrained(mname)
# input_ids = tokenizer.encode(text,padding="longest",return_tensors="pt")
# print(input_ids)
# outputs = model.generate(input_ids)
# decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print(decoded)

#################################################################

#next step: fine tuning
#https://huggingface.co/course/chapter3?fw=pt
#https://medium.com/@tskumar1320/how-to-fine-tune-pre-trained-language-translation-model-3e8a6aace9f

#################################################################
