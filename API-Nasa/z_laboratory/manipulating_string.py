import re

string = "estimated_diameter"
tabela_dicionaria = str.maketrans("_", " ")
nova_string = string.translate(tabela_dicionaria)
print(nova_string)

string = "estimated_diameter"
nova_string = string.replace("_", " ")
print(nova_string)


string = "estimated_diameter"
nova_string = re.sub("_", " ", string)
print(nova_string)
