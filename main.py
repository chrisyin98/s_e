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

    amt_of_found = (last + 1) - first

    for a in range(first,last+1):
      display_terms.append(websites[a])

    frequency = len(display_terms) / amt_of_found
    inverse_frequency = math.log(len(websites)/len(display_terms))
    tfidf = frequency * inverse_frequency
    display_terms = sorted(display_terms)
    self.auto_c_results[tfidf] = display_terms
    print(self.auto_c_results)
    return display_terms

  def first_index_find(self, index, left, right, term, websites):
    while(left <= right):
      mid = int(left + ((right - left) / 2))
      index_word = websites[mid]
      if (len(term) < len(index_word)):
        index_word = websites[mid][0:len(term)]
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
      index_word = websites[mid]
      if (len(term) < len(index_word)):
        index_word = websites[mid][0:len(term)]
      if(index_word <= term):
        left = mid + 1
      else:
        right = mid - 1
      if(term == index_word):
        index = mid
    return index


def main():
  df = pd.read_csv('./dataset/small.csv')
  traffic = df.Avg_Daily_Visitors.tolist()[1:]
  new_list = [x.lower() for x in df.Website.tolist()[1:]]
  websites_list = sorted(new_list)
  print(websites_list)
  s_e = Search_Engine()
  search_query = s_e.search_algorithm("www.g", websites_list)
  print(search_query)


class Term:
  def __init__(self, weight, term):
    self.weight = weight
    self.term = term

  def weight(self):
    return self.weight

  def term(self):
    return self.term

  def add_weight(self):
    self.weight ==


main()