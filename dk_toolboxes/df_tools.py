import pandas as pd
import numpy as np

#SECTION:EXTRACT
################################################################################

def make_keywords(df,y_key):
    #only diaster positive keywords
    keyword_list=df.loc[df[df.keys()[y_key]] == 1].keyword.unique()
    keyword_str=str(keyword_list).replace("'", "").replace('nan', " ")[1:-1]
    return keyword_list,keyword_str

def make_keywords_all(df,y_key):
    #all of the keywords
    keyword_list=df.keyword.unique()
    keyword_str=str(keyword_list).replace("'", "").replace('nan', " ")[1:-1]
    return keyword_list,keyword_str

def post_proc_truth_tweet(y_predicted,X_test_pre,y_test):
    column_names=['text','predicted','truth']
    post_check=pd.DataFrame(columns=column_names)
    post_check['text']= X_test_pre['text']
    post_check['predicted']= y_predicted
    post_check['truth']= y_test.astype('int').astype(int)
    post_check['id']= X_test_pre['id']

    positives=post_check.loc[post_check['truth'] == 1]
    false_neg=positives.loc[post_check['truth'] != post_check['predicted']]
    true_pos=positives.loc[post_check['truth'] == post_check['predicted']]
    negatives=post_check.loc[post_check['truth'] == 0]
    false_pos=negatives.loc[post_check['truth'] != post_check['predicted']]
    true_neg=negatives.loc[post_check['truth'] == post_check['predicted']]


def df_remove_duplicates(df,text_key,truth_key):
    # drop repeated tweets with the same truth and all tweets with truth discrepancies
    duplicates=pd.concat(g for _, g in df.groupby(text_key) if len(g) > 1)

    #remove copies of text with the same target value
    identicaltargetdrop=duplicates.drop_duplicates(subset=[text_key,truth_key], keep='first')
    #display(identicaltargetdrop.groupby('text').head(10))
    # print(identicaltargetdrop.shape)

    #remove all duplicates of text that have differing truth values
    identicaltextdrop=identicaltargetdrop.drop_duplicates(subset=[text_key], keep=False)
    #display(identicaltextdrop.groupby('text').head(10))

    #collect the ids to take from the training data set
    EVERY_dup=duplicates.id.unique()
    sub1=identicaltargetdrop.id.unique()
    sub2=identicaltextdrop.id.unique()

    to_remove=list(EVERY_dup.copy())
    for item in sub2:
        to_remove.remove(item)
    to_remove=np.array(to_remove)
    df_proc=df[~df['id'].isin(to_remove)]

    report=list(sub1.copy())
    #report the truthmismatches
    for item in sub2:
        report.remove(item)
    report=np.array(report)
        #summary
    print(f'{duplicates.shape[0]} total duplicates')
    print(f'{identicaltargetdrop.shape[0]} have the same text and target values')
    print(f'{identicaltextdrop.shape[0]} pairs have the same text and opposite values')
    print( f'dropped {df.shape[0]-df_proc.shape[0]} repeats ')

    return df_proc,report
