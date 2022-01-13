import numpy as np # LA tools
import pandas as pd # Data processing tools

from User import UserError

class InputProcessor:
    
    def __init__(self, ):
        pass
    
    def _find_title(self, ser, col, my_title):
        set_my_title = set(my_title.lower().split(" "))
        set_possible_title = set(ser[col].lower().split(" "))
        result = len(set_my_title.intersection(set_possible_title))
    
        if result > 0:
            return (True, result)
        else:
            return (False, result)
    
    
    def _get_books(self, books_db, user, book_var, title_name):
        try:
            book_mask = books_db.apply(self._find_title, axis=1, args=(title_name, user.db[book_var]))
            book_mask_result = book_mask.map(lambda x: x[1])
            book_mask_result_max = book_mask_result.max()
            
            if book_mask_result_max == 0:
                raise UserError(f"No title: \"{user.db[book_var]}\" intersections!!!")
            return books_db[book_mask_result == book_mask_result_max]
        
        except UserError as f: 
            print(f.str_err + "funct: _get_book")
            raise f

    def _titles_to_vec_pos(self, data_store, user, book_var, title_name, user_vec):
        
        try:
            books = self._get_books(
                data_store.books_db, user,
                user.keys[book_var], data_store.title_name,
            )
            book = books.iloc[0]
            user_vec[data_store.bookid_to_ind[book[data_store.id_name]]] = 1.0
        
        except UserError as f:
            print(f.str_err + "funct: _titles_to_vec_pos")

        return 

    def _get_user_vector(self, user, data_store):
        
        n_books = len(data_store.ind_to_bookid)
        user_vec = np.zeros(shape=(n_books, ))

        for title in range(3):
            self._titles_to_vec_pos(data_store, user, title, data_store.title_name, user_vec)

        if user_vec.sum() < 1.0:
            user_vec[np.random.choice(np.arange(n_books), 3)] = 1.0

        return user_vec
    
    def process_user(self, user, data_store):
        
        user_vec = self._get_user_vector(user, data_store)
        return user_vec
    
class OutputProcessor:
    
    def __init__(self,):
        pass

    def _in(self, set1, set2):
        l1 = list(set1)
        counting = 0
        for i in l1:
            if i in set2:
                counting += 1       
        if counting == len(l1):
            return True
        return False            

    
    def _check_title(self, title, user):
        set_my_title = set(title.lower().split(" "))
        set_possible_titles = [set(user.db[i].lower().split(" ")) for i in ["book1", "book2", "book3"]]
        
        for i in set_possible_titles:
            if self._in(i, set_my_title):
                return False
        return True
    
    def give_results(self, recommendations, data_store, user, pref_scores):
        
        result = {
            data_store.bookid_to_title[data_store.ind_to_bookid[rec]]: (pref_scores[rec], rec)\
             for rec in recommendations
        }
        
        output = []
        for title, score in result.items():
            if self._check_title(title, user):
                output.append((title, score))
        return output