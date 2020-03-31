from pathlib import Path

from lxml import etree

# file path
xml_file_path = Path('out_xml/out_file.xml')

# root xml (level 0) with attributes
root = etree.Element('Root', attribute_1='attr 1', attribute_2='attr 2')

for _ in range(5):
    # element for root (level 1)
    element = etree.SubElement(root, 'Element')

    # sub_element for element (level 2)
    sub_element_1 = etree.SubElement(element, 'Sub_element_1')
    # content for sub_element
    sub_element_1.text = 'content for sub element 1'

    sub_element_2 = etree.SubElement(element, 'Sub_element_2')
    sub_element_2.text = 'content for sub element 2'

    sub_element_3 = etree.SubElement(element, 'Sub_element_3')
    sub_element_3.text = 'content for sub element 3'

# indents
etree.indent(root, space=' ' * 4)

# bytes
handle = etree.tostring(root, pretty_print=True, encoding='utf-8',
                        xml_declaration=True)

# mkdir
Path(xml_file_path).parent.mkdir(exist_ok=True)

# save
with open(xml_file_path, 'bw') as f_out:
    f_out.write(handle)
