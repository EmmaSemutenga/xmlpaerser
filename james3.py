from xml.etree import ElementTree
tree = ElementTree.parse('A0A.xml')
root = tree.getroot()

# print(root.tag)
for child in root:
    if child.tag == 'wtext':
        for divs in child:
            for items in divs:
                for item in items:
                    myword=''       
                    for a in item:
                        if a.tag == 'w' or a.tag == "c":
                            myword = myword + a.text + ' '
                        elif a.tag in ["hi" , "mw" , "s"]:
                            mywordTWO='' 
                            for z in a:
                                if z.tag == 'w' or z.tag == "c":
                                    mywordTWO = mywordTWO + z.text + ' '  
                            myword+=mywordTWO
                            # print(a.tag)
                    with open('readme.txt', 'a') as f:
                        f.writelines(myword+'\n')
