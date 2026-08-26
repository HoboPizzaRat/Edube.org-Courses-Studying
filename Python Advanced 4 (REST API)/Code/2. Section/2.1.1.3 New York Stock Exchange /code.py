import xml.etree.ElementTree
tree = None

try:
    tree = xml.etree.ElementTree.parse("nyse.xml")
except FileNotFoundError as e:
    print("The file was not found!")
except xml.etree.ElementTree.ParseError as e:
    print("The parsing was unsuccessfull")

stocks = tree.getroot()
stockitems = []

print(F"{"COMPANY".ljust(50)}{"LAST".ljust(10)}{"CHANGE".ljust(10)}{"MIN".ljust(10)}{"MAX".ljust(10)}")
print("-" *90)
for stockxml in stocks.findall("quote"):
    stockname = stockxml.text
    attr = stockxml.attrib

    last = attr["last"]
    change = attr["change"]
    min = attr["min"]
    max = attr["max"]

    print(f"{stockname.ljust(50)}{last.ljust(10)}{change.ljust(10)}{min.ljust(10)}{max.ljust(10)}")
    

for item in stockitems:
    for last, change, min, max in item:
        print(last, change, min, max)


