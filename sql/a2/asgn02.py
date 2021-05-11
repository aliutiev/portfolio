"""
-------------------------------------------------------
asgn02.py
[¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯]
-------------------------------------------------------
Author:  Andrew Liutiev
ID:      180635320    
Email:   liut5320@mylaurier.ca 
updated = "2020-03-10"
-------------------------------------------------------
"""




def publications(conn, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = publications(conn)
    Use: rows = publications(conn, title=v1)
    Use: rows = publications(conn, pub_type_id=v2)
    Use: rows = publications(conn, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Preconditions:
        conn - a database connection (Connect)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Postconditions:
        returns:
        rows - a list with a members's last name, a member's first
                name, the title of a publication, and the full publication
                type (i.e. 'article' rather than 'a';
        the entire table if title and pub_type_id are None,
        else rows matching the partial title and pub_type_id 
        if given 
                sorted by last name, first name, title (list of ?)
    -------------------------------------------------------
    """
    
    """ 
    //// search query if title and pub id is none ////
    """

    if title is None and pub_type_id is None:

        the_search_query = """SELECT M.last_name, M.first_name, P.p_title, PT.pt_desc
       FROM (member M JOIN pub P ON P.member_id = M.member_id) JOIN pub_type PT ON P.pub_type_id = P.pub_type_id
       ORDER BY last_name, first_name, p_title
       """

        """ 
        //// search query if title is none and title is not ////
        """
    elif title is None and pub_type_id is not None:

        the_search_query = """SELECT M.last_name, M.first_name, P.p_title, PT.pt_desc
       FROM (member M JOIN pub P ON P.member_id = M.member_id) JOIN pub_type PT ON P.pub_type_id = P.pub_type_id
       WHERE PT.pub_type_id = %s
       ORDER BY M.last_name, M.first_name, P.p_title
       """
       
        the_condition_for_query = [pub_type_id,]


        """ 
        //// search query if there's a title and pub id is none ////
        """
    elif title is not None and pub_type_id is None:

        the_search_query = """SELECT M.last_name, M.first_name, P.p_title, PT.pt_desc
       FROM (member M JOIN pub P ON P.member_id = M.member_id) JOIN pub_type PT ON P.pub_type_id = P.pub_type_id
       WHERE P.p_title LIKE %s
       ORDER BY M.last_name, M.first_name, P.p_title
       """

        the_condition_for_query = ["%" + title + "%",]

        """ 
        //// search query if title and pub id is not none ////
        """
    elif title is not None and pub_type_id is not None:

        the_search_query = """SELECT M.last_name, M.first_name, P.p_title, PT.pt_desc
       FROM (member M JOIN pub P ON P.member_id = M.member_id) JOIN pub_type PT ON P.pub_type_id = P.pub_type_id
       WHERE PT.pub_type_id = %s AND P.p_title LIKE %s
       ORDER BY M.last_name, M.first_name, P.p_title
       """

        the_condition_for_query = [pub_type_id, "%" + title + "%"]
     
    conn.cursor.execute(the_search_query, the_condition_for_query)
    
    rows = conn.cursor.fetchall()
     
    return rows


def pub_counts(conn,  member_id,  pub_type_id = None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_counts(conn, member_id=v1)
    Use: rows = pub_counts(conn, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Preconditions:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Postconditions:
        returns:
        rows - a list with a members's last name, a member's first
        first name, and the number of publications of type pub_type
        if given, if not number of all their publications (list of ?)
    -------------------------------------------------------
    """

    if member_id and pub_type_id:

        the_search_query = """SELECT m.last_name ,m.first_name, pt.pt_desc,
        COUNT(pt.pub_type_id) 
        FROM pub AS p
        INNER JOIN member AS m 
        ON m.member_id = p.member_id
        INNER JOIN pub_type AS pt
        ON pt.pub_type_id = p.pub_type_id
        WHERE p.member_id = %s AND p.pub_type_id = %s
        """


        """ 
        //// search query for the condition where member & public id is used ////
        """

        the_condition_for_query = (member_id, pub_type_id)



    elif member_id and pub_type_id == None:


        """ 
        //// search query for the condition where member & public id is none ////
        """

        the_search_query = """SELECT m.last_name ,m.first_name, pt.pt_desc,
        COUNT(pt.pub_type_id) 
        FROM pub AS p
        INNER JOIN member AS m 
        ON m.member_id = p.member_id
        INNER JOIN pub_type AS pt
        ON pt.pub_type_id = p.pub_type_id
        WHERE p.member_id = %s 
        """





        """ 
        //// search query for the condition where public id is none ////
        """
        the_condition_for_query = (member_id,)


    """ 
    //// more searching  ////
    """


    conn.cursor.execute(the_search_query, the_condition_for_query)
    rows = conn.cursor.fetchall()
    conn.cursor.close()
    return rows


def member_expertise_count(conn, member_id=None):

    """
    -------------------------------------------------------
    Queries the v_member_keyword view.
    Use: rows = member_expertise_count(conn)
    Use: rows = member_expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Preconditions:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Postconditions:
        returns:
        rows - a list with a members's last name, a member's first
        first name, and the count of the number of expertises they
                hold (i.e. keywords)
        all records member_id is None, 
            sorted by last name, first name
        (list of ?)
    -------------------------------------------------------
    """

    """ 
    //// member id is none ////
    """

    if member_id == None:

        the_search_query = """SELECT m.last_name ,m.first_name, 
            COUNT(p.keyword_id)
            FROM member_keyword AS p
            INNER JOIN member AS m 
            ON m.member_id= p.member_id
            GROUP BY first_name, last_name """
        """ 
        //// search query condition where member & public id is none ////
        """
        the_condition_for_query = ()

        """ 
        //// member id is valid ////
        """

    else:

        the_search_query = """SELECT m.last_name ,m.first_name, 
            COUNT(p.keyword_id)
            FROM member_keyword AS p
            INNER JOIN member AS m 
            ON m.member_id= p.member_id
            WHERE p.member_id = %s
            GROUP BY first_name, last_name
            """
        """ 
        //// new condition without pub type id ////
        """    
        the_condition_for_query = (member_id,)

    conn.cursor.execute(the_search_query, the_condition_for_query)
    rows = conn.cursor.fetchall()
    conn.cursor.close()
    return rows


def all_expertise(conn, member_id=None):

    """
    -------------------------------------------------------
    Queries the v_keyword_supp_key view.
    Use: rows = all_expertise(conn)
    Use: rows = all_expertise(conn, member_id=v1)
    -------------------------------------------------------
    Preconditions:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Postconditions:
        returns:
        rows - a list with a members's last name, a member's first
        first name, a keyword descrption, and a supplementary keyword description
        all records if member_id is None, 
        sorted by lst)name, first_name, keyword description, supplementary 
                keyword description
    -------------------------------------------------------
    """

    if member_id:

        the_search_query = """ SELECT m.last_name, m.first_name, k.k_desc, sk.sk_desc
        From member as m
        INNER JOIN member_supp_key as msy
        ON msy.member_id = m.member_id
        INNER JOIN supp_key as sk
        ON msy.supp_key_id = sk.supp_key_id 
        INNER JOIN keyword as k
        ON k.keyword_id= sk.keyword_id
        WHERE m.member_id = %s
        GROUP BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
        """

        """ 
        //// new condition for without pub id ////
        """
        the_condition_for_query = (member_id,)

    else:

        the_search_query = """SELECT m.last_name, m.first_name, k.k_desc, sk.sk_desc
        From member as m
        INNER JOIN member_supp_key as msy
        ON msy.member_id = m.member_id
        INNER JOIN supp_key as sk
        ON msy.supp_key_id = sk.supp_key_id 
        INNER JOIN keyword as k
        ON k.keyword_id= sk.keyword_id
        GROUP BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
        """

        """ 
        //// new condition no member & no pub id ////
        """

        the_condition_for_query = ()


    """ 
    //// fetch queries ////
    """

    conn.cursor.execute(the_search_query, the_condition_for_query)
    rows = conn.cursor.fetchall()
    conn.cursor.close()
    return rows