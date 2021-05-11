"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Andrew Liutiev
ID:    180635320
Email:    liut5320@mylaurier.ca
__updated__ = "2020-03-27"
-------------------------------------------------------
"""

from Connect import Connect

def pub_counts_all(conn, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(conn)
    Use: rows = pub_counts(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of each type. Name these
        three fields "articles", "papers", and "books". List the results
        as appropriate in order by member last name and first name.
        If member_id is None, list all members. (list of ?)
    -------------------------------------------------------
    """
    
    if member_id is None:
        
        """ case for when member ID is non existent"""
        
        sql = """SELECT last_name, first_name,
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
            AND pub_type_id = 'a') AS articles, 
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
            AND pub_type_id = 'p') AS papers, 
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
            AND pub_type_id = 'b') AS books 
            FROM member AS m ORDER BY last_name, first_name"""
            
        """"SQL execution with the parameters excluding the non existent ID"""
        
        conn.cursor.execute(sql)
    else:
        
        """ case for when there is a member ID for the SQL"""
        
        sql = """SELECT last_name, first_name,
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
            AND pub_type_id = 'a') AS articles, 
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
            AND pub_type_id = 'p') AS papers, 
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
            AND pub_type_id = 'b') AS books 
            FROM member AS m
            WHERE member_id = %s"""
            
        """"SQL execution with the parameters"""
        
        params = (member_id, )
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows


def expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = expertise_count(conn)
    Use: rows = expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of keywords and supplementary keywords
        for the member. Name these fields "keywords" and "supp_keys".
        List the results as appropriate in order by member last 
        name and first name. If member_id is None, list all members.
        (list of ?)
    -------------------------------------------------------
    """
    
    if member_id is None:
        
        """ case for when member ID is non existent"""
        
        sql = """SELECT last_name, first_name,
            (SELECT COUNT(*) FROM member_keyword AS mk WHERE m.member_id = mk.member_ID) AS keywords, 
            (SELECT COUNT(*) FROM member_supp_key AS msk WHERE m.member_id = msk.member_ID) AS supp_keys
            FROM member AS m ORDER BY last_name, first_name"""
            
        """"SQL execution with the parameters excluding the non existent ID"""
        
        conn.cursor.execute(sql)
    else:
        
        """ case for when there is a member ID for the SQL"""
        
        sql = """SELECT last_name, first_name,
            (SELECT COUNT(*) FROM member_keyword AS mk WHERE m.member_id = mk.member_ID) AS keywords, 
            (SELECT COUNT(*) FROM member_supp_key AS msk WHERE m.member_id = msk.member_ID) AS supp_keys
            FROM member AS m
            WHERE member_id = %s"""
            
        """"SQL execution with the parameters"""
        
        params = (member_id,)
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    
    return rows
    

def keyword_count(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_count(conn)
    Use: rows = keyword_count(conn, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
        supplementary keywords that belong to it. Name the second field
        "supp_key_count".
        List the results as appropriate in order by keyword description. 
        If keyword_id is None, list all keywords. (list of ?)
    -------------------------------------------------------
    """
    if keyword_id is None:
        
        """ case for when keyword ID is non existent"""
        
        sql = """SELECT k_desc, COUNT(sk.supp_key_id) AS supp_key_count
            FROM keyword AS k LEFT OUTER JOIN supp_key AS sk
            ON k.keyword_id = sk.keyword_id
            GROUP BY k.keyword_id
            ORDER BY k_desc"""
            
        """"SQL execution with the parameters excluding the non existent ID"""
        
        conn.cursor.execute(sql)
    else:
        
        """ case for when there is a keyword ID for the SQL"""
        
        sql = """SELECT k_desc, COUNT(sk.supp_key_id) AS supp_key_count
            FROM keyword AS k LEFT OUTER JOIN supp_key AS sk
            ON k.keyword_id = sk.keyword_id
            WHERE k.keyword_id = %s
            GROUP BY k.keyword_id"""
        
        """"SQL execution with the parameters"""
        
        params = (keyword_id, )
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows

def keyword_member_count(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_member_count(conn)
    Use: rows = keyword_member_count(conn, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
        members that have it. Name the second field
        "member_count".
        List the results as appropriate in order by keyword description. 
        If keyword_id is None, list all keywords. (list of ?)
    -------------------------------------------------------
    """
    
    if keyword_id is None:
        
        """ case for when member ID is non existent"""
        
        sql = """SELECT k_desc, COUNT(mk.keyword_id) AS member_count
            FROM keyword AS k LEFT OUTER JOIN member_keyword AS mk
            ON k.keyword_id = mk.keyword_id
            GROUP BY k.keyword_id
            ORDER BY k_desc"""
            
        """"SQL execution with the parameters excluding the non existent ID"""
        
        conn.cursor.execute(sql)
    else:
        
        """ case for when there is a keyword ID for the SQL"""
        
        sql = """SELECT k_desc, COUNT(mk.keyword_id) AS member_count
            FROM keyword AS k LEFT OUTER JOIN member_keyword AS mk
            ON k.keyword_id = mk.keyword_id
            WHERE k.keyword_id = %s
            GROUP BY k.keyword_id"""
            
        """"SQL execution with the parameters"""
            
        params = (keyword_id, )
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows
    

def supp_key_member_count(conn, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = supp_key_member_count(conn)
    Use: rows = supp_key_member_count(conn, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - a list with a keyword's description, a supplementary
        keyword description, and the number of members that have it. 
        Name the last field "member_count".
        List the results as appropriate in order by keyword description
        and then supplementary keyword description.
        If supp_key_id is None, list all keywords and supplementary
        keywords. (list of ?)
    -------------------------------------------------------
    """
    if supp_key_id is None:
        
        """ case for when suppkey ID is non existent"""
        
        sql = """SELECT k_desc, sk_desc, COUNT(msk.member_id) AS member_count
            FROM keyword AS k JOIN supp_key AS sk
            ON k.keyword_id = sk.keyword_id
            LEFT OUTER JOIN member_supp_key AS msk
            ON sk.supp_key_id = msk.supp_key_id
            GROUP BY msk.supp_key_id
            ORDER BY k_desc, sk_desc"""
            
        """"SQL execution with the parameters excluding the non existent ID"""
        
        conn.cursor.execute(sql)
    else:
        
        """ case for when there is a suppkey ID for the SQL"""
        
        sql = """SELECT k_desc, sk_desc, COUNT(msk.member_id) AS member_count
            FROM keyword AS k JOIN supp_key AS sk
            ON k.keyword_id = sk.keyword_id
            LEFT OUTER JOIN member_supp_key AS msk
            ON sk.supp_key_id = msk.supp_key_id
            WHERE sk.supp_key_id = %s
            GROUP BY msk.supp_key_id
            ORDER BY k_desc, sk_desc"""
        
        """"SQL execution with the parameters"""
        
        params = (supp_key_id, )
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows
