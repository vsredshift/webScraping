import requests
from bs4 import BeautifulSoup as BS

""" All Recipes """

# Get url

#url = 'https://www.allrecipes.com/recipe/256867/honey-garlic-chicken-wraps/'
url = 'https://www.allrecipes.com/recipe/240559/traditional-gyros/'
# url = 'https://www.allrecipes.com/recipe/234182/cashew-chicken-stir-fry/'
# url = 'https://www.allrecipes.com/recipe/245993/soba-noodle-salad-with-chicken-and-sesame/'
source = requests.get(url).text


soup = BS(source, 'lxml')
#print(soup.prettify())

# Get the heading/recipe name
heading = soup.find('h1').text

# Get the images with recipe name. Limit to 4
images = []
for image in soup.find_all('img'):
    try:
        if heading in image.get('alt'):
            photo = image.get('src')
            images.append(photo)
    except Exception as e:
        image = None


# Get the ingredients
#ingredients = soup.find('div', class_='section-headline').h2.text
#print(ingredients)

servings = int(soup.find('div', class_='recipe-adjust-servings__size-quantity').text)

ingredients = []
for ingredient_item in soup.find_all('span', class_='ingredients-item-name'):
    ingredients.append(ingredient_item.text.strip())


# Get the method
#directions = soup.find('section', class_='recipe-instructions').h2.text
#print(directions.strip())

steps = []
for step in soup.find_all('li', class_='instructions-section-item'):
   steps.append(step.p.text)


# Get recipe note
note = soup.find('div', class_='recipe-note').p.text


# Console Log
print(heading)
print()

try:
    print(images[:4])
except Exception as e:
    print(images)
print()

print("Ingredients for " + str(servings) + " servings:")
print()
for item in ingredients:
    print(item)
print()
print()

print("Directions:")
print()

for step in steps:
    print(step)
    print()
print()
print("Notes:")
print(note)
