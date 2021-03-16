import requests
from bs4 import BeautifulSoup as BS

""" All Recipes """

# Get url


#url = 'https://www.bbcgoodfood.com/recipes/vegan-chilli'
#url = 'https://www.bbcgoodfood.com/recipes/satay-sweet-potato-curry'
#url = 'https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli'
url = 'https://www.bbcgoodfood.com/recipes/vegan-burritos'
source = requests.get(url).text


soup = BS(source, 'lxml')
# print(soup.prettify()).body

heading = soup.find('h1').text

image = soup.find('img', {'title': heading}).get('src').split('?')[0]

servings = soup.find('div', class_="post-header__servings").text
ingredients = soup.find('section', class_="recipe__ingredients")
ing_headings = ingredients.find('h3').text
ingredient_item = []
for item in ingredients('li'):
    ingredient_item.append(item.text)


directions = []
method = soup.find('section', {'class': 'recipe__method-steps'})
for item in method('li'):
    directions.append(item.p.text)


print()
print(heading)

print()
print(image)

print("Ingredients (" + servings + ")")
print()
for item in ingredient_item:
    print(item)

print()
print("Method:")
print()

for item in directions:
    print(item)
    print()
