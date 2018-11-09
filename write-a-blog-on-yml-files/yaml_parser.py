# To get this example working you have to install pyyaml
# To do this execute: pip install -r requirements.txt
# Enjoy :)

import yaml

yaml_file = open("example.yml", "r") # Opening a yaml file
parsed_yaml = yaml.load(yaml_file) # yaml.load instruction returns yaml file to simple dictionary :)

print(type(parsed_yaml)) # Proof :)
print(parsed_yaml) # Print dictionary generated from your YAML

age = parsed_yaml['Age'] # Now you can use your yaml as normal dictionary
baguettes = parsed_yaml['shop_list'][4]['baguettes'] # Keys inside lists aren' t that easy to parse :(
print("Bagguetes to buy: {}".format(baguettes))