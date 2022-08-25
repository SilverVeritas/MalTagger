class Characters:
    def get_characters(self, soup):
        character = soup.find(class_="detail-characters-list clearfix")

        found_character_names = None
        found_character_va = None
        found_character_role = None

        if character:
            char_search = character.find_all(class_="h3_characters_voice_actors")
            found_character_names = [name.text for name in char_search]

            char_search = character.find_all(class_="spaceit_pad")
            found_character_role = [r.text.strip() for r in char_search]

            char_search = character.find_all(class_="va-t ar pl4 pr4")
            found_character_va = [va.text.strip().split('\n')[0] for va in char_search]

            self.characters = []
            for i in range(len(found_character_names)):
                try:
                    va_if_known = found_character_va[i]
                except:
                    va_if_known = None

                self.characters.append({
                    'Name' : found_character_names[i],
                    'Voice Actor' : va_if_known,
                    'Role' : found_character_role[i]
                    })
            return
        self.characters = []
        return