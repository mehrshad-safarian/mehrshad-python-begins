def city_search(search_item, cities =["new york", "shanghai", "munich", "tokyo", "tehran"] ) :
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            pass
    return False
visited_cities = ["new york", "kelardasht", "calous", "shiraz", "boushehr"]
search = input("enter a city visited:")
print()

print (search.title(), "in default cities is", city_search(search))

print(search.title(), "in visited_cites list is", city_search(search,visited_cities))