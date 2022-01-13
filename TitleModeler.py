from itertools import islice
import random
import numpy as np

class TitleModeler:
    
    def __init__(self,):
        pass

    def _intersection_text(self, db, ind1, ind2, column, splitter=","):
        set1 = set(db.iloc[ind1][column].lower().split(splitter))
        set2 = set(db.iloc[ind2][column].lower().split(splitter))
        if len(set1.intersection(set2)) > 0:
            return True
        return False  

    def _chunk(self, it, size):
        it = iter(it)
        return iter(lambda: tuple(islice(it, size)), ())

    def get_titles_poll(self, titles, user_vec, db, column, splitter=",", how_many=3, final=False):
    
        out_titles = []
        user_titles = np.argwhere(user_vec > 0.0)#.squeeze()
        temp_titles = titles
        for user_title in user_titles:
            for title in temp_titles:
                check = self._intersection_text(db, user_title[0], title[1][1], column, splitter)
                if not check:
                    out_titles.append(title)
            temp_titles = out_titles
            out_titles = []
 
        out_titles = temp_titles

        if final:
            return out_titles[:how_many]

        parts = list(self._chunk(out_titles, len(out_titles) // how_many))
        result = []
    
        for part in parts:
            result.append(random.choice(part))
    
        return result[:how_many]