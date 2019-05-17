# -*- coding: UTF-8 -*-
from lxml import etree

# Create the root element
page = etree.Element('results' )

# Make a new document tree
doc = etree.ElementTree(page)

# Add the subelements
pageElement1 = etree.SubElement(page, 'country', name='Германия', code='DE', continent='Европа')
pageElement2 = etree.SubElement(page, 'country', name='Россия', code='RU', continent='Европа')

print(etree.tostring(page, encoding='unicode'))  # Don't forget about correct encoding
print(etree.tostring(pageElement1, encoding='unicode'))
print(etree.tostring(pageElement2, encoding='unicode'))

"""
<results><country code="DE" continent="Европа" name="Германия"/><country code="RU" continent="Европа" name="Россия"/></results>
<country code="DE" continent="&#x415;&#x432;&#x440;&#x43E;&#x43F;&#x430;" name="&#x413;&#x435;&#x440;&#x43C;&#x430;&#x43D;&#x438;&#x44F;"/>
<country code="RU" continent="&#x415;&#x432;&#x440;&#x43E;&#x43F;&#x430;" name="&#x420;&#x43E;&#x441;&#x441;&#x438;&#x44F;"/>
"""
