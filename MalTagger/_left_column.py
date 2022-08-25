class Left_Column:
    def get_lc(self, soup):
        self.synonyms = None
        self.native_name = None
        self.english_name = None

        self.video_type = None
        self.episodeCount = None
        self.primiered = None
        self.source = None

        self.studio = None
        self.producer = None
        self.genres = None
        self.themes = None 


        left_column = soup.find(class_ = "leftside")
        left_column_entries = left_column.find_all(class_="spaceit_pad")
        for elem in left_column_entries:
            if 'Synonyms:<' in str(elem):
                self.synonyms = elem.find('span').nextSibling.strip()
            if 'Japanese:<' in str(elem):
                self.native_name = elem.find('span').nextSibling.strip()
            if 'English:<' in str(elem):
                self.english_name = elem.find('span').nextSibling.strip()

            if 'Type:<' in str(elem):
                self.video_type = elem.find('a').text.strip()
            if 'Episodes:<' in str(elem):
                self.episode_count = elem.find('span')
                if self.episode_count:
                    self.episode_count = self.episode_count.nextSibling.strip()
            if 'Premiered:<' in str(elem):
                self.primiered = elem.find('a')
                if self.primiered:
                    self.primiered = self.primiered.text.strip()
            if 'Source:<' in str(elem):
                self.source = elem.find('span')
                if self.source:
                    self.source = self.source.nextSibling.strip()
            if 'Studios:<' in str(elem):
                self.studio = [studio.text for studio in elem.find_all('a', recursive=False)]
                if 'add some' in self.studio:
                    self.studio = []
            if 'Producers:<' in str(elem):
                self.producer = [prod.text for prod in elem.find_all('a', recursive=False)]
                if 'add some' in self.producer:
                    self.producer = []
            if 'Licensors:<' in str(elem):
                self.licensor = [lic.text for lic in elem.find_all('a', recursive=False)]
                if 'add some' in self.licensor:
                    self.licensor = []
            if 'Genres:<' in str(elem):
                self.genres = [g.text for g in elem.find_all('span')[1:]]
            if 'Themes:<' in str(elem):
                self.themes = [t.text for t in elem.find_all('span')[1:]]

        if not self.primiered:
            self.season = None
            self.seasonYear = None
        else:
            self.season = self.primiered.split()[0]
            self.seasonYear = int(self.primiered.split()[1])

        if self.episode_count.isnumeric():
            self.episode_count = int(self.episode_count)