import pandas as pd, math
import json, re
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
import numpy as np
class Search_Engine:

  def __init__(self):
    self.auto_c_results = dict()

  def search_algorithm(self, term, websites):
    index = -1
    left = 0
    right = len(websites) - 1
    display_terms = []

    if(term.endswith('.')):
      term.replace('.', '')

    if(term.startswith('www.')):
      term = term.split('.')[1]
    elif(term.endswith('.com')):
      term = term.split('.')[0]

    if(term.endswith('s')):
      term = term[:-1]
    if(term.endswith('es')):
      term = term[:-2]


    first = self.first_index_find(index, left, right, term, websites)
    last = self.last_index_find(index, left, right, term, websites)

  #  if(first == -1 and last == -1):
  #    display_terms.append(Term('', 0, 'Cannot be found'))
  #  else:
  #    for a in range(first,last+1):
  #      display_terms.append(websites[a])


    display_terms = sorted(display_terms, key= lambda x: x.get_weight())
    #order would be by cosine similiarty
    return display_terms

  def first_index_find(self, index, left, right, term, websites):
    while(left <= right):
      mid = int(left + ((right - left) / 2))
      index_word = websites[mid]
      if(index_word >= term ): # term in index is the diffference between these two methods
        right = mid - 1
      else:
        left = mid + 1
      if(term == index_word):
        index = mid
    return index

  def last_index_find(self, index, left, right, term, websites):
    while(left <= right):
      mid = int(left + ((right - left) / 2))
      index_word = websites[mid]
      if(index_word <= term):
        left = mid + 1
      else:
        right = mid - 1
      if(term == index_word):  # replace with in to see if afghan gets better!!
        index = mid
    return index


def start(user_input_raw):
  s_e = Search_Engine()
  df = pd.read_csv('C:/Users/Christopher/Desktop/python/search_engine/dataset/small.csv')
  #traffic = df.Avg_Daily_Visitors.tolist() #df.Avg_Daily_Visitors.tolist()[1:]
  descriptions = df.Description.tolist()
  website_names = df.Website.tolist()



  #user_input = ""
  #user_input_raw = "scary" #input('Search?')
  refine_input = user_input_raw.replace('.com', '')
  refine_input = refine_input.lower()
  refine_input = refine_input.replace('www.','')
  refine_input = refine_input.replace('.', '')
  refine_input = refine_input.replace(',', '')
  user_input = refine_input.split(' ')


  descriptions.append(user_input_raw)
  descript_to_lower = [x.lower() for x in descriptions]

  default_q_vals = []
  tf_idf_list = []

  for a in range(len(user_input)):
    #default_q_vals.append(1)
    tf_list = []
    count = 0
    for x in range(len(descriptions)):
      remove_period = descript_to_lower[x].replace('.com', ' ')  #filter www in description creation
      remove_period = remove_period.replace('/', ' ')
      remove_period = remove_period.replace('.', ' ')
      descrip_prep = sorted(remove_period.split(" ")) #sorted description in alphabetical order
      first = s_e.first_index_find(-1, 0, len(descrip_prep) - 1, user_input[a], descrip_prep)
      last = s_e.last_index_find(-1, 0, len(descrip_prep) - 1, user_input[a], descrip_prep)
      amt_in_descrip = 0
      if(first > -1 and last > -1):
        amt_in_descrip = (last + 1) - first
      if(amt_in_descrip > 0):
        count = count + 1
        tf = amt_in_descrip / len(descrip_prep)
        tf_list.append(tf)
      else:
        tf_list.append(0)

    idf = 1 # =1 deosn't mean much jsut a place holder
    if(count > 0):
      idf = (math.log(len(descriptions) / count))
    tf_idf_temp_list = []
    for y in range(len(descriptions)):
      tf_idf = tf_list[y] * idf
      tf_idf_temp_list.append(tf_idf)
    tf_idf_list.append(tf_idf_temp_list)

    default_q_vals.append(tf_idf_temp_list[len(tf_idf_temp_list) - 1])


  ordered_list = cos_similarity(default_q_vals, tf_idf_list)

  final_list = []


  for i in range(len(website_names)):
    if(ordered_list[i] > 0):
      final_list.append(Term(descriptions[i], ordered_list[i], website_names[i]))

  display_terms = sorted(final_list, key =lambda x: x.get_weight(), reverse = True)
  #for x in range(len(display_terms)):
   # print(display_terms[x].get_website_nme(), display_terms[x].get_weight())
  #  print(display_terms[x].get_descrip())
  return display_terms


def cos_similarity(default_q_vals, tf_idf_list):

  final_list = []
  for x in range(len(tf_idf_list[0])):
    temp_list = []
    for y in range(len(tf_idf_list)):
      temp_list.append(tf_idf_list[y][x])
    cos_sim = cosine_similarity([default_q_vals], [temp_list])
    refine_cos_sim = np.array(cos_sim).tolist()
    final_list.append(refine_cos_sim[0][0])
  return final_list






class Term:
  def __init__(self,descrip, weight, website_nme):
    self.weight = weight
    self.descrip = descrip
    self.website_nme = website_nme

  def get_weight(self):
    return self.weight

  def get_descrip(self):
    return self.descrip

  def add_weight(self):
    self.weight = self.weight + 1

  def get_website_nme(self):
    return self.website_nme

