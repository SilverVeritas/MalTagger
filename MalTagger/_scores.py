class Score:
    def get_scores(self, soup):
        score_soup = soup.find(class_="stats-block po-r clearfix")

        try:
            self.score_overall = float(score_soup.find(class_="score-label score-8").text)
        except:
            self.score_overall = 0

        scores = score_soup.find(class_="di-ib ml12 pl20 pt8").find_all('strong')
        scores = [score.text for score in scores]
        try:
            self.rank_by_score = int(scores[0].strip('#'))
        except:
           self.rank_by_score = 0
        self.rank_by_popularity = int(scores[1].strip('#'))
        self.user_population = int(scores[2].replace(',', ''))

    