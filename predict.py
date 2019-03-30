import re
import nltk
import numpy as np
nltk.download('stopwords')
from nltk.corpus import stopwords
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences





def article_preprocess(article):
  """ Converting to lower case """
  article = article.lower()
  
  """ To remove punctuations and special characters """
  cleaned = re.sub(r'[?|!|\'|"|#]', r'', article)
  cleaned = re.sub(r'[.|,|)|(|\|/]', r' ', article)
  cleaned = cleaned.strip()
  cleaned = cleaned.replace('\n',' ')
  
  """ To remove non-alphabetic characters """
  alpha_sent=''
  for word in cleaned.split():
    alpha_word=re.sub('[^a-z A-Z]+', ' ', word)
    alpha_sent+=alpha_word
    alpha_sent+=' '
  alpha_sent=alpha_sent.strip()
  
  """ Removing stop words """
  stop_words=set(stopwords.words('english'))
  stop_words.update(['zero','one','two','three','four','five','six','seven',
                   'eight','nine','ten','may','also','across','among','beside','however','yet','within'])
  re_sw=re.compile(r'\b('+'|'.join(stop_words)+')\\W',re.I)
  article = re_sw.sub(' ', alpha_sent)
  
  """ Taking 1st 100 words for prediction """
  article = list(article.split())[:100]
  article = ' '.join(article)
  
  return article

def build_sequence(article):
  maxlen = 100 # cut off articles after 100 words or pad articles 
  max_words = 10000 # only top 10000 words in dataset
  texts = [article]
  tokenizer = Tokenizer(num_words=max_words)
  tokenizer.fit_on_texts([article])
  sequences = tokenizer.texts_to_sequences(texts)
  data = pad_sequences(sequences, maxlen=maxlen)
  print(data)
  return data

def fake_score(sequence):
  loaded_model = load_model('best-model-05-0.96.hdf5')
  loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
  score = loaded_model.predict_proba(sequence)[0][0]
  return score
