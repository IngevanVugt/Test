item1 = float(input("prijs item 1"))
item2 = float(input("prijs item 2"))
item3 = float(input("prijs item 3"))
item4 = float(input("prijs item 4"))
item5 = float(input("prijs item 5"))

subtotaal = item1 + item2 + item3 + item4 + item5
print("subtotaal is", subtotaal)

belasting = subtotaal * 0.07
print ("de belasting is", belasting)

totaalbedrag = subtotaal + belasting

print("het totaal bedrag is", totaalbedrag)
