class Title:
    def get_title(self,soup):
        #Title Data
        self.title =  soup.find("h1").text

    def get_title_en(self,soup):
        try:
            self.title_en = soup.find(class_="title-english title-inherit").text
        except:
            self.title_en = None
       