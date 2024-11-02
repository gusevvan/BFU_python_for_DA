import json

if __name__ == "__main__":
    with open("ex_3.json") as jsonFile, open("ex_3_new.json", 'w') as jsonNewFile:
        jsonDict = json.load(jsonFile)
        invoiceExample = jsonDict['invoices'][0].copy()
        invoiceExample["id"] = 3
        invoiceExample["total"] = 150.0
        exampleItem = invoiceExample["items"][0].copy()
        invoiceExample["items"] = []
        exampleItem["name"] = "item 4"
        exampleItem["quantity"] = 1
        exampleItem["price"] = 60.0
        invoiceExample["items"].append(exampleItem.copy())
        exampleItem["name"] = "item 5"
        exampleItem["quantity"] = 2
        exampleItem["price"] = 90.0
        invoiceExample["items"].append(exampleItem)
        jsonDict["invoices"].append(invoiceExample)
        json.dump(jsonDict, jsonNewFile, indent=2)
