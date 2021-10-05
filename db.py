import ast

import mysql.connector
from PyQt5 import QtWidgets


class DB:

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="root", database="customer",
                                                auth_plugin='mysql_native_password')
        except Exception as e:
            raise Exception("db load failed : ", e)
        try:
            self.mydb.cursor().execute("CREATE TABLE IF NOT EXISTS cust_details( cust_ref INT UNIQUE, cust_name "
                                       "VARCHAR(50), people_cnt INT, gender VARCHAR(15), pincode INT, mobile VARCHAR(11) "
                                       "UNIQUE, email VARCHAR(60) UNIQUE, nationality VARCHAR(20), id_proof_type "
                                       "VARCHAR(20), id_number VARCHAR(20) PRIMARY KEY, cust_address VARCHAR(80));")
            self.mydb.commit()
        except Exception as e:
            raise Exception("Create table failed : ", e)

    def insert_data(self, cust):
        query = "INSERT INTO cust_details(cust_ref, cust_name, people_cnt, gender, pincode, mobile, email, " \
                "nationality, id_proof_type, id_number, cust_address) VALUES(" + cust.cust_ref + ", '" + cust.cust_name + "', " + cust.people_cnt + ", '" + cust.gender + "', " + cust.pincode + ", " + cust.mobile + ", '" + cust.email + "', '" + cust.nationality + "', '" + cust.id_proof_type + "', '" + cust.id_number + "', '" + cust.cust_address + "')"
        try:
            self.mydb.cursor().execute(query)
            self.mydb.commit()
            print('Record inserted successfully...')
        except Exception as e:
            raise Exception(e)

    def update_data(self, old_cust, new_cust):
        query = "UPDATE cust_details SET cust_ref=" + new_cust.cust_ref + ", cust_name='" + new_cust.cust_name + "', people_cnt=" + new_cust.people_cnt + ", gender='" + new_cust.gender + "', pincode=" + new_cust.pincode + ", mobile=" + new_cust.mobile + ", email='" + new_cust.email + "', nationality='" + new_cust.nationality + "', id_proof_type='" + new_cust.id_proof_type + "', id_number='" + new_cust.id_number + "', cust_address='" + new_cust.cust_address + "' WHERE cust_ref=" + old_cust.cust_ref + " AND id_number='" + old_cust.id_number + "';"
        try:
            self.mydb.cursor().execute(query)
            self.mydb.commit()
            print('Record updated successfully...')
        except Exception as e:
            raise Exception("Unable to update record, Error : ", e)

    def delete_data(self, cust):
        query = "DELETE FROM cust_details WHERE cust_ref=" + cust.cust_ref + " OR id_number='" + cust.id_number + "';"
        try:
            self.mydb.cursor().execute(query)
            self.mydb.commit()
            print('Record deleted successfully...')
        except Exception as e:
            raise Exception("Unable to delete record, Error : ", e)

    def search(self, key_dict):
        cur = self.mydb.cursor()
        query = "select * from cust_details"
        if len(key_dict) > 0:
            query += " where"
            first = True
            for key, value in key_dict.items():
                key_search = ""
                if key == 'cust_ref' or key == 'people_cnt' or key == 'pincode' or key == 'mobile':
                    key_search += " " + key + "=" + value
                else:
                    key_search += " " + key + "='" + value + "'"
                if not first:
                    query += " and" + key_search
                else:
                    query += " " + key_search
                    first = False

        res = cur.execute(query)

        row_res = cur.fetchall()

        return row_res
