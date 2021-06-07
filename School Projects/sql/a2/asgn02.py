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

def table_info(conn, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = table_info(conn, table_schema)
    Use: rows = table_info(conn, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        table_schema - the database table schema (str)
        table_name - a DCRIS table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, TABLE_TYPE, TABLE_ROWS, 
        and TABLE_COMMENT fields. Order by TABLE_NAME.
        If table_name is None, list all tables. (list of ?)
    -------------------------------------------------------
    """
    
    """ QUERY WHEN PARAMS ARE NONE"""
    
    if table_name is None:
        sql = '''
            SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
            FROM information_schema.TABLES 
            WHERE TABLE_SCHEMA = "''' + table_schema + '''"
            ORDER BY TABLE_NAME
        '''

    else:
        """ QUERY WHEN PARAMS HAS VALUE"""
        sql = '''
            SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
            FROM information_schema.TABLES 
            WHERE TABLE_SCHEMA = "''' + table_schema + '''" AND TABLE_NAME = "'''+ table_name+ '''"
            ORDER BY TABLE_NAME
        '''
        
        
    conn.cursor.execute(sql)
    rows = conn.cursor.fetchall()
    return rows

    
def column_info(conn, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = column_info(conn, table_schema)
    Use: rows = column_info(conn, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        table_schema - the database table schema (str)
        table_name - a DCRIS table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, COLUMN_NAME, IS_NULLABLE, 
        and DATA_TYPE fields. Order by TABLE_NAME, COLUMN_NAME.
        If table_name is None, list all tables and their columns. (list of ?)
    -------------------------------------------------------
    """
    
    """ QUERY WHEN PARAMS ARE NONE"""

    if table_name is None:
        sql = '''
        
            SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = "''' + table_schema + '''"
            ORDER BY TABLE_NAME, COLUMN_NAME
        '''
        

    else:
        """ QUERY WHEN PARAMS HAS VALUE"""
        sql = '''
            SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = "''' + table_schema + '''" AND TABLE_NAME = "'''+ table_name+ '''"
            ORDER BY TABLE_NAME, COLUMN_NAME
        '''
    
    conn.cursor.execute(sql)
    rows = conn.cursor.fetchall()
    return rows
    
def constraint_info(conn, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = constraint_info(conn, table_schema)
    Use: rows = constraint_info(conn, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME, 
        and CONSTRAINT_TYPE. Order by CONSTRAINT_NAME, TABLE_NAME.
        If constraint_type is None, list all constraints. (list of ?)
    -------------------------------------------------------
    """
    
    """ QUERY WHEN PARAMS ARE NONE"""
    
    if constraint_type is None:
        sql = ''' 
            SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
            FROM information_schema.TABLE_CONSTRAINTS
            WHERE TABLE_SCHEMA = "''' + table_schema + '''"
            ORDER BY CONSTRAINT_NAME, TABLE_NAME
            '''
    else:
        """ QUERY WHEN PARAMS HAS VALUE"""
        sql = ''' 
            SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
            FROM information_schema.TABLE_CONSTRAINTS
            WHERE TABLE_SCHEMA = "''' + table_schema + '''" AND CONSTRAINT_TYPE = "'''+ constraint_type+ '''"
            ORDER BY CONSTRAINT_NAME, TABLE_NAME
            '''.format(table_schema, constraint_type)

    conn.cursor.execute(sql)
    rows = conn.cursor.fetchall()
    return rows
    
def foreign_key_info(conn, constraint_schema, table_name = None, ref_table_name = None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = foreign_key_info(conn, constraint_schema)
    Use: rows = foreign_key_info(conn, constraint_schema, table_name=v1)
    Use: rows = foreign_key_info(conn, constraint_schema, ref_table_name=v2)
    Use: rows = foreign_key_info(conn, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        constraint_schema - the database constraint schema (str)
        table_name - a DCRIS table name (str)
        ref_table_name - a DCRIS table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, 
        TABLE_NAME, and REFERENCED_TABLE_NAME fields. Order by CONSTRAINT_NAME.
        If table_name and ref_table_name are None, list all rows. (list of ?)
    -------------------------------------------------------
    """
    
    """ QUERY WHEN PARAMS ARE NONE"""

    if table_name is None and ref_table_name is None:
        sql= ''' 
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''"
            ORDER BY CONSTRAINT_NAME
        '''
        


    elif table_name is not None and ref_table_name is None:
        """ QUERY WHEN FIRST PARAM IS NOT NONE"""
        sql= ''' 
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''" AND TABLE_NAME = "''' + table_name + '''"
            ORDER BY CONSTRAINT_NAME
        '''

        
    
    elif table_name is not None and ref_table_name is not None:
        """ QUERY WHEN SECOND PARAM IS NOT NONE"""
        sql= ''' 
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''" AND REFERENCED_TABLE_NAME = "'''+ref_table_name+'''"
            ORDER BY CONSTRAINT_NAME
        '''
        
    elif table_name is not None and ref_table_name is not None:
        """ QUERY WHEN BOTH PARAM IS NOT NONE"""
        sql= ''' 
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''" AND TABLE_NAME = "''' + table_name + '''" AND REFERENCED_TABLE_NAME = "'''+ref_table_name+'''"
            ORDER BY CONSTRAINT_NAME
        '''
        
    conn.cursor.execute(sql)
    rows = conn.cursor.fetchall()
    return rows
        
    
def key_info(conn, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = key_info(conn, constraint_schema)
    Use: rows = key_info(conn, constraint_schema, table_name=v1)
    Use: rows = key_info(conn, constraint_schema, ref_table_name=v2)
    Use: rows = key_info(conn, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        constraint_schema - the database constraint schema (str)
        table_name - a DCRIS table name (str)
        ref_table_name - a DCRIS table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, 
        REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields. Order by 
        TABLE_NAME, COLUMN_NAME. 
        If table_name and ref_table_name are None, list all rows. (list of ?)
    -------------------------------------------------------
    """

    """ QUERY WHEN PARAMS ARE NONE"""

    if table_name is None and ref_table_name is None:
        sql= ''' 
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''"
        ORDER BY TABLE_NAME, COLUMN_NAME
        '''
        

    elif table_name is not None and ref_table_name is None:
        """ QUERY WHEN FIRST PARAM IS NOT NONE"""
        sql= ''' 
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
            WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''" AND REFERENCED_TABLE_NAME = "'''+ref_table_name+'''"
        ORDER BY TABLE_NAME, COLUMN_NAME
        '''
    
    elif table_name is not None and ref_table_name is not None:
        """ QUERY WHEN SECOND PARAM IS NOT NONE"""
        sql= ''' 
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''" AND REFERENCED_TABLE_NAME = "'''+ref_table_name+'''"
        ORDER BY TABLE_NAME, COLUMN_NAME
        '''
        
    elif table_name is not None and ref_table_name is not None:
        """ QUERY WHEN BOTH PARAM IS NOT NONE"""
        sql= ''' 
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA = "'''+ constraint_schema + '''" AND TABLE_NAME = "''' + table_name + '''" AND REFERENCED_TABLE_NAME = "'''+ref_table_name+'''"
        ORDER BY TABLE_NAME, COLUMN_NAME
        '''
        
        
    conn.cursor.execute(sql)
    rows = conn.cursor.fetchall()
    return rows