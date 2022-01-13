import numpy as np # LA tools
import pandas as pd # Data processing tools

from Processors import InputProcessor, OutputProcessor

class RecSys:
    
    def __init__(self, model, data_store):
        
        self.input_processor = InputProcessor()
        self.model = model
        self.data_store = data_store
        self.output_processor = OutputProcessor()
        
    def recommend(self, user, num=30):
        
        user_vec = self.input_processor.process_user(user, self.data_store)
        pref = user_vec @ self.model.item_factors @ self.model.item_factors.T
        recommendations = np.argsort(pref)[::-1][:num]
        pref_scores = {i:pref[i] for i in recommendations}
        
        result = self.output_processor.give_results(recommendations, self.data_store, user, pref_scores)
        return result, user_vec