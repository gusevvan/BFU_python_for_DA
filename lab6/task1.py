import xmlschema

if __name__ == "__main__":
    with open("ex_1.xsd") as shemaFile:
        schema = xmlschema.XMLSchema(shemaFile)
        print(schema.is_valid('ex_1.xml'))
        print(schema.is_valid('err_ex_1.xml'))
