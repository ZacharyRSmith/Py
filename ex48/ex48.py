class lexicon(object):
    def scan(self, usr_in):
        rslt = []
        directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left',
                      'right', 'back']
        verbs      = ['go', 'stop', 'kill', 'eat']
        stops      = ['the', 'in', 'of', 'from', 'at', 'it']
        words = usr_in.split()
        for word in words:
            if word in directions:
                rslt.append(('direction', word))
            elif word in verbs:
                rslt.append(('verb', word))
            elif word in stops:
                rslt.append(('stop', word))
            else:
                # FIXME Try int
                rslt.append(('N/A', word))
        return rslt

# class lexicon(object):

#     def scan(self, direction):
#         pass