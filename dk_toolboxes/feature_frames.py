from sklearn.feature_extraction.text import CountVectorizer
import textmanip_tools as dk_TM

def ff_preproc(train_data,keywords):

    #additional_words=str(' ')
    count_vect = CountVectorizer()
#   feature_frame=count_vect.fit_transform(df['text']).copy()
    count_vect.fit([keywords])
    return count_vect
################################################################################
def feature_frame_creator_disastertweets2(df,count_vect,keyword_list):
    df['cleaned_text']=df['text'].apply(dk_TM.df_txt_cleaner)
    extracted_keywords_text=df["cleaned_text"].apply(dk_TM.collect_keywords_simplified2,args=(keyword_list))
    feature_frame=count_vect.transform(extracted_keywords_text).copy()
    feature_frame_array=feature_frame.toarray()
    return feature_frame_array
