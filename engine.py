import pandas as pd, math

class Search_Engine:

  def __init__(self):
    self.auto_c_results = dict()

  def search_algorithm(self, term, websites):
    index = -1
    left = 0
    right = len(websites) - 1
    display_terms = []

    first = self.first_index_find(index, left, right, term, websites)
    last = self.last_index_find(index, left, right, term, websites)

    for a in range(first,last+1):
      display_terms.append(websites[a])


    display_terms = sorted(display_terms, key= lambda x: x.get_weight())
    #self.auto_c_results[tfidf] = display_terms
    #print(self.auto_c_results)
    return display_terms

  def first_index_find(self, index, left, right, term, websites):
    while(left <= right):
      mid = int(left + ((right - left) / 2))
      index_word = websites[mid].get_term()
      if (len(term) < len(index_word)):
        index_word = websites[mid].get_term()[0:len(term)]
      if(index_word >= term):
        right = mid - 1
      else:
        left = mid + 1
      if(term == index_word):
        index = mid
    return index

  def last_index_find(self, index, left, right, term, websites):
    while(left <= right):
      mid = int(left + ((right - left) / 2))
      index_word = websites[mid].get_term()
      if (len(term) < len(index_word)):
        index_word = websites[mid].get_term()[0:len(term)]
      if(index_word <= term):
        left = mid + 1
      else:
        right = mid - 1
      if(term == index_word):
        index = mid
    return index


def start(user_input):
  df = pd.read_csv('C:/Users/Christopher/Desktop/python/search_engine/dataset/small.csv')
  traffic = df.Avg_Daily_Visitors.tolist() #df.Avg_Daily_Visitors.tolist()[1:]
  total_avg_visitors = df.Avg_Daily_Visitors.sum() / 100000
  new_list = [x.lower() for x in df.Website.tolist()]  # in df.Website.tolist()[1:]
  websites_prep = sorted(new_list)
  websites_list = []
  for x in range(len(websites_prep)):
    freq_prep = (traffic[x]) / 100000
    frequency = freq_prep / total_avg_visitors
    inverse_frequency = math.log(total_avg_visitors / freq_prep)
    tfidf = frequency * inverse_frequency
    websites_list.append(Term(websites_prep[x], tfidf))


  s_e = Search_Engine()
#  user_input = ""
#while(user_input != '$'):
# user_input = input('Search?')
  search_query = s_e.search_algorithm(user_input, websites_list)
  return search_query
  #for x in range(len(search_query)):
  #  print(search_query[x].get_term())



class Term:
  def __init__(self,term, weight):
    self.weight = weight
    self.term = term

  def get_weight(self):
    return self.weight

  def get_term(self):
    return self.term

  def add_weight(self):
    self.weight = self.weight + 1
