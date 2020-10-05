import requests
from bs4 import BeautifulSoup
import os

URL = 'https://www.openschool.bc.ca/k12/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

teen_levels = {'Primary', 'Intermediate', 'Secondary'}
adult_levels = {'Mathematics', 'Science'}


def filter_headings(heading):
    return heading in teen_levels or heading in adult_levels

def create_headings():
    headings = [heading.get_text() for heading in soup.find_all('h3')]
    headings = list(filter(filter_headings, headings))
    return headings


def create_resources_arr(headings):
    resources_map = {}
    for index, panel_group in enumerate(soup.select('div.panel-group')):
        resources_map[headings[index]] = {}
        for panel in panel_group.select('div.panel.panel-default'):
            subtopic = panel.select('h4 a')[0].get_text()
            resources_map[headings[index]][subtopic] = []
            for a in panel_group.select('li a'):
                link = a.get('href') if a.get('href').startswith('http://') else 'https://www.openschool.bc.ca/' + a.get('href')
                resource = {'title': a.get_text(), 'link': link}
                resources_map[headings[index]][subtopic].append(resource)

    return resources_map


def parse_website():
    return create_resources_arr(create_headings())


print(parse_website())
