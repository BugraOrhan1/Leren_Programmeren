pizza_list = [
    {"diameter": 20, "toppings": ["kaas", "pepperoni", "champignons"]},
    {"diameter": 25, "toppings": ["tomatensaus", "mozzarella", "basilicum"]},
    {"diameter": 30, "toppings": ["ham", "ananas", "paprika"]},
    {"diameter": 35, "toppings": ["ui", "zwarte olijven", "feta"]},
    {"diameter": 40, "toppings": ["salami", "rucola", "Parmezaanse kaas"]},
    {"diameter": 45, "toppings": ["geitenkaas", "spinazie", "walnoten"]},
    {"diameter": 50, "toppings": ["kip", "barbecuesaus", "ui"]},
    {"diameter": 55, "toppings": ["artisjokken", "pesto", "mozzarella"]},
    {"diameter": 60, "toppings": ["tonijn", "kappertjes", "ansjovis"]},
    {"diameter": 65, "toppings": ["gorgonzola", "vijgen", "honing"]},
]

gesorteerde_pizza_list = sorted(pizza_list, key=lambda x: x["diameter"])

total_diameter = sum(pizza['diameter'] for pizza in gesorteerde_pizza_list)

print("Totale diameter van alle pizza's:", total_diameter, "cm")

print("Gesorteerde lijst van pizza's:")
for pizza in gesorteerde_pizza_list:
    print("Diameter:", pizza['diameter'], "cm - Toppings:", pizza['toppings'])
