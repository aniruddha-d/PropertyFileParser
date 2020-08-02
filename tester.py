
from PropertyFileReader.PropertyFileToDictConverter import PropertyFileToDictConverter
from PropertyFileReader.PropertyReader import PropertyReader

fl = 'sample.properties'
d = PropertyFileToDictConverter.parse(fl)
print(d)


reader = PropertyReader(fl)
print(reader.get_value('name3'))

