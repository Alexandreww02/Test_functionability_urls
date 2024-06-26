import requests
from bs4 import BeautifulSoup
import pytest




wunder = requests.get("https://aerooshield.com/sitemap_index.xml")
parcala = BeautifulSoup(wunder.content, "xml")

urls_from_xml = []

loc_tags = parcala.find_all('loc')

for loc in loc_tags:
    urls_from_xml.append(loc.get_text()) 
        
print(urls_from_xml)

    
def test_functionalitate_siteuri():   

    assert wunder.status_code == 200, f"The status code is {wunder.status_code} and we waiting 200"

    assert len(wunder.text) > 0, "The response content is empty"