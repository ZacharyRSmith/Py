class lexicon(object):
    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(self, usr_in):
        rslt = []
        directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left',
                      'right', 'back']
        verbs      = ['go', 'stop', 'kill', 'eat']
        stops      = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns      = ['door', 'bear', 'princess', 'cabinet']
        words = usr_in.split()
        for word in words:
            if word in directions:
                rslt.append(('direction', word))
            elif word in verbs:
                rslt.append(('verb', word))
            elif word in stops:
                rslt.append(('stop', word))
            elif word in nouns:
                rslt.append(('noun', word))
            elif self.convert_number(word):
                rslt.append(('number', self.convert_number(word)))
            else:
                # FIXME Try int
                rslt.append(('N/A', word))
        return rslt

# class lexicon(object):

#     def scan(self, direction):
#         pass