from pathlib import Path

import requests
from lxml import etree
from lxml.etree import fromstring


#######################################
# from file
# in_xml_file_name = 'in_xml/sitemap.xml'
#
# tree = etree.parse(in_xml_file_name)
# root = tree.getroot()
#######################################
# from url
url = 'https://www.selver.ee/sitemap.xml'
response = requests.get(url)
root = fromstring(response.content)
#######################################

# indents
etree.indent(root, space=' ' * 4)

# bytes
handle = etree.tostring(root, pretty_print=True, encoding='utf-8',
                        xml_declaration=True)

# save
out_xml_file = Path('out_xml/out_sitemap.xml')
with open(out_xml_file, 'bw') as f_out:
    f_out.write(handle)
