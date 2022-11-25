# Using latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant.
# Make a Restauran instance.
# Call methods from the Restaurant class.


from restaurant import Restaurant

hungry_angry = Restaurant('hungry angry', 'street food')

lido = Restaurant('lido', 'home made cuisine')

hesburger = Restaurant('hesburger', 'fast food')

hungry_angry.describe_restaurant()
hungry_angry.open_restaurant()
print("\n")

lido.describe_restaurant()
lido.open_restaurant()
print("\n")

hesburger.describe_restaurant()
hesburger.open_restaurant()
