import pandas as pd
import numpy as np

class StyleRecommender:
    
    def __init__(self, sim_mtx, bookid_to_ind, ind_to_bookid, metadata):
        self.simtx = sim_mtx
        self.bookid_to_ind = bookid_to_ind
        self.ind_to_bookid = ind_to_bookid
        self.metadata = metadata

    def give_titles(self):
        indeces = np.random.choice([i for i in range(len(self.ind_to_bookid))], 3)
        return [
            (   
                ind,
                self.metadata.loc[self.ind_to_bookid[ind]]["title"],
                self.metadata.loc[self.ind_to_bookid[ind]]["author"],
                self.metadata.loc[self.ind_to_bookid[ind]]["plot"],
                self.metadata.loc[self.ind_to_bookid[ind]]["link"],  
            ) for ind in indeces
        ]

    def give_similar_titles(self, ind, num=3): 
        pref = self.simtx[ind] 
        candidates = (np.argsort(pref)[::-1]).tolist()
        candidates.remove(ind)
        candidates = candidates[:num]
        return [
            (   
                self.metadata.loc[self.ind_to_bookid[ind]]["title"],
                self.metadata.loc[self.ind_to_bookid[ind]]["author"],
                self.metadata.loc[self.ind_to_bookid[ind]]["link"],
            ) for ind in candidates
        ] 
