import json

def formatJson(fileName):
    jsonDict = {}
    with open(fileName, 'r') as jsonReadFile:
        jsonDict = json.load(jsonReadFile)
    with open(fileName, 'w') as jsonWriteFile:
        json.dump(jsonDict, jsonWriteFile, indent=2)
        
if __name__ == "__main__":
    formatJson("ex_2.json")
    with open("ex_2.json", 'r') as jsonFile:
        users = json.load(jsonFile)
        for user in users:
            print(f'{user["name"]}: {user["phoneNumber"]}')
