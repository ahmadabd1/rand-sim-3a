from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)


print("Articles with a title of t4:")
print(filter_CSV("title", "t4"))
print('')
print("Articles of a1 author:")
print(filter_CSV("author", "a1"))

# reader = CSV_Manager("./articles.csv") extraaaaaaaaaaaaa
# reader.find_by_type()

#func 1
def count_articles(filter_field, value):
    return len(filter_CSV(filter_field, value))
print(count_articles('title', 't4'))
print(count_articles('category', 'c1'))

# func 2
def is_article(filter_field, value):
    return len(filter_CSV(filter_field, value))!=0
print(is_article('title', 't4'))
print(is_article('author', 'a0'))

#func 3
from operator import itemgetter

def longest_article(filter_field, value):
    sorted_list = sorted(filter_CSV(filter_field, value), key=itemgetter('pages'))
    return sorted_list[-1]

print(longest_article('author', 'a1'))
print(longest_article('category', 'c1'))
