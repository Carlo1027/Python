import xml.etree.ElementTree as ET

data = '''<person>
    <name>Carlo</name>
    <phone type="intl">
        +1 961 775 503
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
