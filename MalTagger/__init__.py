import requests
from bs4 import BeautifulSoup

import _title
import _left_column
import _songs
import _related
import _characters
import _scores
import _base

class MalTagger(_title.Title, _left_column.Left_Column, _songs.Song,
                _related.Related, _characters.Characters, _scores.Score,
                ):
    # Public and Viewable Data
    url = ''

    title = ''
    title = None

    synonyms = None
    native_name = None
    english_name = None

    score_overall = None
    rank_by_score = None
    rank_by_popularity = None
    user_population = None

    video_type = None
    episode_count = None
    primiered = None
    season = None
    seasonYear = None
    source = None

    studio = None
    producer = None
    genres = None
    themes = None

    adaptation = None
    alternate_version = None
    side_story = None
    summary = None
    prequel = None
    sequel = None

    songlist_op = None
    songlist_ed = None

    characters = None

    mal_url = None
    mal_code = None
    # /Public and Viewable Data

    # Private Data
    _soupMain = None




    def __init__(self, mal_url):
        self.url = mal_url
        try:
            self._get_soup()
        except:
            raise _base.InvalidUrl
        self.get_title(self._soupMain)
        self.get_title_en(self._soupMain)
        self.get_lc(self._soupMain)
        self.get_openings(self._soupMain)
        self.get_endings(self._soupMain)
        self.get_related(self._soupMain)
        self.get_characters(self._soupMain)
        self.get_scores(self._soupMain)


    
    def _get_soup(self):
        request = requests.get(self.url)
        self._soupMain = BeautifulSoup(request.content,'html.parser')
        self.mal_url = self._soupMain.find('meta', {'property':'og:url'}).get('content')
        if '/anime/' not in self.mal_url:
            raise _base.WrongTypeOfMalLink
        self.mal_code = int(self.mal_url.split('/')[-2])

    def json(self):
        full_json_dict = {
        'title' : self.title,
        'titleEn' : self.title_en,

        'synonyms' : self.synonyms,
        'nativeName' : self.native_name,
        'englishName' : self.english_name,

        'scoreOverall' : self.score_overall,
        'rankByScore' : self.rank_by_score,
        'rankByPopularity' : self.rank_by_popularity,
        'userPopulation' : self.user_population,

        'videoType' : self.video_type,
        'episodeCount' : self.episode_count,
        'seasonPremiere' : self.primiered,
        'season' : self.season,
        'seasonYear' : self.seasonYear,
        'source' : self.source,
        'studios' : self.studio,
        'producers' : self.producer,
        'licensors' : self.licensor,
        'genres' : self.genres,
        'themes' : self.themes,

        'openings' : self.songlist_op,
        'ending' : self.songlist_ed,

        'adaptation' : self.adaptation,
        'alternateVersion' : self.alternate_version,
        'sideStory' : self.side_story,
        'summary' : self.summary,
        'prequel' : self.prequel,
        'sequel' : self.sequel,
        
        'characters' : self.characters,

        'malUrl' : self.mal_url,
        'malCode' : self.mal_code
        }
        return full_json_dict


if __name__ == '__main__':
    tagger = MalTagger('https://myanimelist.net/anime/21')
    a = tagger.json()

    for x in a:
        print(f'{x}: {a[x]}')