class DataStore:
    def __init__(self, books_db, ind_to_bookid,
                 bookid_to_ind, ind_to_userid, userid_to_ind,
                 ratings_for_csr, R, bookid_to_title,
                 title_to_bookid, id_name, title_name):
        
        self.books_db = books_db
        self.ind_to_bookid = ind_to_bookid
        self.bookid_to_ind = bookid_to_ind
        self.ind_to_userid = ind_to_userid
        self.userid_to_ind = userid_to_ind
        self.ratings_for_csr = ratings_for_csr
        self.R = R
        self.bookid_to_title = bookid_to_title
        self.title_to_bookid = title_to_bookid
        self.id_name = id_name
        self.title_name = title_name