from cards import *
import json

land1 = Land(color=Green)
land1.tap()
creature1 = Creature(2, Green, 2, 2)
creature1.tap()

t = open("AllPrintings.json", "r")
json.decoder(t)


