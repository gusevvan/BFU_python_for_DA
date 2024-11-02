import json
from jsonschema import validate

def validateJson(jsonDict, schemaDict):
    try:
        validate(jsonDict, schemaDict)
        return "Ok"
    except Exception as e:
        return f"Error:\n{e}"

if __name__ == "__main__":
    with open("ex_1.json") as trueJsonFile, open("ex_1_err.json") as errJsonFile, open("ex_1_schema.json") as schemaFile:
        trueJsonDict = json.load(trueJsonFile)
        errJsonDict = json.load(errJsonFile)
        schemaDict = json.load(schemaFile)
        print(validateJson(trueJsonDict, schemaDict))
        print(validateJson(errJsonDict, schemaDict))
