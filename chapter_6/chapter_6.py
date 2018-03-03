import urllib.parse
import urllib.request
import re
import sys

link_regex = re.compile(r'<a href="[a-zA-Z0-9/:\.-]+">')

class LinkCollector():
	def __init__(self, url):
		self.url = 'http://' + urllib.parse.urlparse(url).netloc
		self.collected_links = {}
		self.visited_links = set()

	def normalize(self, link):
		if link.startswith('http://'):
			return link.rstrip('/')
		elif link.startswith('/'):
			return self.url + link.rstrip('/')
		else:
			return self.url + '/' + link.rstrip('/')

	def collect_links(self, path='/'):
		url = self.url
		self.visited_links.add(url)
		content = str(urllib.request.urlopen(url).read())
		links = link_regex.findall(content)
		links = {self.normalize(link) for link in links}
		self.collect_links[url] = links
		for link in links:
			self.collect_links.setdefault(link, set())
		for k, v in self.collected_links:
			print('{}: {}'.format(k, v))

if __name__ == '__main__':
	li = LinkCollector('http://0.0.0.0:8000/index.html')
	li.collect_links()




