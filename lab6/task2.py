import xml.etree.ElementTree as ET

if __name__ == "__main__":
    xmlTree = ET.parse('ex_2.xml')
    root = xmlTree.getroot()
    summ, summrows = 0, 0
    for child in root:
        if child.tag == "Detail":
            child[-1].tail = "\n        "
            newItem = ET.Element('Item')
            newItem.tail = "\n    "
            newItem.text = "\n            "
            newItemArtName = ET.SubElement(newItem, 'ArtName')
            newItemArtName.text = "Сыр Гауда"
            newItemArtName.tail = "\n            "
            newItemBarcode = ET.SubElement(newItem, 'Barcode')
            newItemBarcode.text = "2000000000082"
            newItemBarcode.tail = "\n            "
            newItemQNT = ET.SubElement(newItem, 'QNT')
            newItemQNT.text = "237,6"
            newItemQNT.tail = "\n            "
            newItemQNTPack = ET.SubElement(newItem, 'QNTPack')
            newItemQNTPack.text = "237,6"
            newItemQNTPack.tail = "\n            "
            newItemUnit = ET.SubElement(newItem, 'Unit')
            newItemUnit.text = "шт"
            newItemUnit.tail = "\n            "
            newItemSN1 = ET.SubElement(newItem, 'SN1')
            newItemSN1.text = "00000003"
            newItemSN1.tail = "\n            "
            newItemSN2 = ET.SubElement(newItem, 'SN2')
            newItemSN2.text = "12.06.2018"
            newItemSN2.tail = "\n            "
            newItemQNTRows = ET.SubElement(newItem, 'QNTRows')
            newItemQNTRows.text = "21"
            newItemQNTRows.tail = "\n        "
            child.append(newItem)
            for item in child:
                for param in item:
                    if param.tag == "QNT":
                        summ += float(param.text.replace(',', "."))
                    if param.tag == "QNTRows":
                        summrows += int(param.text)
    for child in root:
        if child.tag == "Summary":
            for param in child:
                if param.tag == "Summ":
                    param.text = str(summ).replace('.', ',')
                if param.tag == "SummRows":
                    param.text = str(summrows)
    xmlTree.write('new_ex2.xml', encoding='UTF-8')