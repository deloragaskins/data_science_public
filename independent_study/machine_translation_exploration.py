##################################################
########################################################
#https://huggingface.co/t5-base
# from transformers import AutoTokenizer, AutoModelWithLMHead
# tokenizer = AutoTokenizer.from_pretrained("t5-base")
# model = AutoModelWithLMHead.from_pretrained("t5-base")

#https://arxiv.org/pdf/1910.10683.pdf

###################################################################
#https://www.machinecurve.com/index.php/2021/02/16/easy-machine-translation-with-machine-learning-and-huggingface-transformers/
from transformers import pipeline

# Init translator
translator = pipeline("translation_en_to_fr")

# Translate text
text = ["Hello my friends! How are you doing today?",
"Sir, please sit down ",
"sister, sit down please",
"chill out, bro",
"I'll have a coffee",
"Follow the rules",
"watch out!"]
translation = translator(text)

# Print translation
print(translation)
##########################################################
# translation=[{'translation_text': "Bonjour, mes amis, comment allez-vous aujourd'hui?"},
#  {'translation_text': "Monsieur le Président, s'il vous plaît vous asseoir"},
#  {'translation_text': 'sur, sil vous plaît sasseoir'},#https://www.machinecurve.com/index.php/2021/02/16/easy-machine-translation-with-machine-learning-and-huggingface-transformers/
#  {'translation_text': 'chill out, bro'},
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
##########################################################

# Next step try pretrained tokenizer and model on benchmark sentences
# Below is cut and paste from :
# https://www.machinecurve.com/index.php/2021/02/16/easy-machine-translation-with-machine-learning-and-huggingface-transformers/


# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#
# # Initialize the tokenizer
# tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-nl")
#
# # Initialize the model
# model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-nl")
#
# # Tokenize text
# text = "Hello my friends! How are you doing today?"
# tokenized_text = tokenizer.prepare_seq2seq_batch([text])
#
# # Perform translation and decode the output
# translation = model.generate(**tokenized_text)
# translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
#
# # Print translated text
# print(translated_text)
