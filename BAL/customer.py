import DAL.db as d

dta = d.DB()


def get_all_customers():
    return dta.execute_select_query("sales", "Customer")


def get_customer(_id: int):
    return dta.execute_select_query("sales", "Customer", params={'Id': _id})


def get_customer_by_last_name(_name: str):
    return dta.execute_select_query("sales", "Customer", params={'Last_Name': _name})

def get_students_data():
    return dta.execute_select_query("StatsCan", "WorkStatus", params={'is_student': True})

def get_full_dataset():
    return dta.execute_select_query("StatsCan", "WorkStatus")


    # @app.route('/v1/stats/data/province/<province>', methods=['GET'])
    # def get_data_per_province():
    #     return 'It works'
def get_province_data(_province: str):
    return dta.execute_select_query("StatsCan", "WorkStatus", params={'prov_name': _province})

def get_data_per_lfs_code(_lfs_code: str):
    return dta.execute_select_query("StatsCan", "WorkStatus", params={'lfsstat': _lfs_code})