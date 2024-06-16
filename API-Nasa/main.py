from api_data.all_neows.Betulia import betulia_all_data
from objects.NeoWs import NeoWs

neows = NeoWs(betulia_all_data)

print(neows)

basic_neows_data = neows.basic_data()

for i in basic_neows_data:
    string = f"{i}: {basic_neows_data[i]}"
    print(string)

print(neows.orbital_data)

