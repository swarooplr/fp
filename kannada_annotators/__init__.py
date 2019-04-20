class Trie:
    def __init__(self):
        self.level_node = {}
        self.pos = set()
        self.is_word = False


    def insert(self,word):
        if len(word.text) == 0:
            self.is_word = True
            self.pos.add(word.pos)
            return


        if not self.level_node.has_key(word.text[0]):
            new_node = Trie()
            self.level_node[word.text[0]] = new_node
            new_node.insert(Word(word.text[1:len(word.text)], word.pos))
        else:
            (self.level_node[word.text[0]]).insert(Word(word.text[1:len(word.text)], word.pos))




    def is_present(self,text):

        if len(text) == 0:
            return self.is_word

        elif self.level_node.has_key(text[0]):
            return (self.level_node[text[0]]).is_present(text[1:len(text)])
        else:
            return False

    def prefix_matches(self,text):
        matches = []
        if len(text) == 0:
            return matches
        if self.level_node.has_key(text[0]):
            temp = (self.level_node[text[0]]).prefix_matches(text[1:len(text)])
            for i in temp:
                prefix = text[0]+i
                matches.append(prefix)

            if (self.level_node[text[0]]).is_word:
                matches.append(text[0])

        return matches



    def find_tense(self,text):

        if len(text) == 0:
            if self.is_word:
                return self.pos
            else:
                return None

        elif self.level_node.has_key(text[0]):
            return (self.level_node[text[0]]).find_tense(text[1:len(text)])
        else:
            return None


class Word:
    def __init__(self,text,pos):
        self.text = text
        self.pos = pos





