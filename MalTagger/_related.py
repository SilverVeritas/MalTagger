class Related:
    def get_related(self, soup):
        related = soup.find(class_="anime_detail_related_anime")
        if related:
            related_categories = related.find_all('td', class_="ar fw-n borderClass")
        else:
            related_categories = []
            
        self.adaptation = None
        self.alternate_version = None
        self.side_story = None
        self.summary = None
        self.prequel = None
        self.sequel = None

        for elem in related_categories:
            try:
                if 'Adaptation:<' in str(elem):
                    self.adaptation = [adp.text for adp in elem.nextSibling.find_all('a')]
                if 'Alternative version:<' in str(elem):
                    self.alternate_version = [av.text for av in elem.nextSibling.find_all('a')]
                if 'Side story:<' in str(elem):
                    self.side_story = [ss.text for ss in elem.nextSibling.find_all('a')]
                if 'Summary:<' in str(elem):
                    self.summary = [s.text for s in elem.nextSibling.find_all('a')]
                if 'Prequel:<' in str(elem):
                    self.prequel = [p.text for p in elem.nextSibling.find_all('a')]
                if 'Sequel:<' in str(elem):
                    self.sequel = [se.text for se in elem.nextSibling.find_all('a')]
            except:
                continue