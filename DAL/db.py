import os
import mysql.connector


# Generic Data Utilities
class DB(object):
    def __init__(self):
        try:
            self.config_file = "./.my.cnf"
            # self.config_file = os.path.expanduser('~') + '\\.my.cnf'
            # x = os.path.expanduser('~') + '\\.my.cnf' # C:/users/your_user_name/.my.cnf

            self.connection = mysql.connector.connect(option_files=self.config_file)
        except mysql.connector.Error as e:
            print(e)
            self.close()

    def execute_select_query(self, db_name, table_name, params=None):
        return_set = []
        cursor = self.connection.cursor(dictionary=True)
        if params is None:
            cursor.execute("select * from {}.{}".format(db_name, table_name))
        else:
            where_clause = 'WHERE ' + ' AND '.join(['`' + k + '` = %s' for k in params.keys()])
            values = list(params.values())
            sql = "SELECT * FROM {}.{} ".format(db_name, table_name) + where_clause
            cursor.execute(sql, values)
        for x in cursor:
            return_set.append(x)
        cursor.close()
        return return_set

    def __del__(self):
        self.close()

    def close(self):
        self.connection.close()
