import sqlite3

class DataBase:
    def __init__(self, table_name) -> None:
        # เชื่อมต่อกับ SQLite
        self.conn = sqlite3.connect('Panyaon.db', timeout=5)
        # self.conn = sqlite3.connect(r'\\10.97.1.48\SEL_Monitor\Got_TE\example.db')
        self.table_name = table_name
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}(
                id INTEGER NOT NULL UNIQUE,
                name TEXT NOT NULL,
                answer INTEGER NOT NULL,
                input TEXT,
                usernum INTEGER,
                endgame INTEGER
            )""")
        self.conn.commit()

    def fetchAllData(self):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        return self.cursor.fetchall()

    def fetchUserNum(self):
        self.cursor.execute(f'SELECT usernum FROM {self.table_name}')
        return self.cursor.fetchone()

    def fetchOne(self, id_name):
        self.cursor.execute(f'SELECT * FROM {self.table_name} WHERE id = {id_name}')
        return self.cursor.fetchone()

    def fetchAllExcept(self, id_name):
        self.cursor.execute(f'SELECT * FROM {self.table_name} WHERE id != {id_name}')
        return self.cursor.fetchall()

    def fetchDictData(self):
        self.cursor.execute(f'SELECT id, name, answer, input FROM {self.table_name}')
        return dict(self.cursor.fetchall()) 

    def closeDataBase(self):
        self.conn.close()
        return True


class selectDatabase(DataBase):
    def __init__(self, table_name):
        super().__init__(table_name)

    def selectFromDatabase(self) -> dict:
        self.cursor.execute(f'SELECT Item, Value FROM {self.table_name} WHERE FuncType=?', ('HWInfo',))
        return dict(self.cursor.fetchall())

    def getValueFromDatabase(self, param):
        return self.selectFromDatabase().get(param)


class insertDatabase(DataBase):
    def __init__(self, table_name, param_one=None, param_many=None):
        self.paramOne = param_one
        self.paramMany = param_many
        super().__init__(table_name)

    @property
    def _new_data_many(self) -> list:
        return self.paramMany

    def executeOneApply(self):
        self.cursor.execute(
            f'INSERT INTO {self.table_name} (id, name, answer, usernum) VALUES (?, ?, ?, ?)',
            self.paramOne
        )
        self.conn.commit()

    def executeMany(self):
        self.cursor.executemany(
            f'INSERT INTO {self.table_name} (id, name, answer, input) VALUES (?, ?, ?, ?)',
            self._new_data_many
        )
        self.conn.commit()


class updateDatabase(DataBase):
    def __init__(self, table_name, param_field, param_update):
        self.param_field = param_field
        self.param_update = param_update
        super().__init__(table_name)

    def UpdateInput(self):
        update_data = (self.param_update, self.param_field)
        self.cursor.execute(f'UPDATE {self.table_name} SET input=? WHERE id=?', update_data)
        self.conn.commit()
        print("UPDATE Result: Value updated successfully")

    def UpdateEndGame(self):
        update_data = (self.param_update, self.param_field)
        self.cursor.execute(f'UPDATE {self.table_name} SET endgame=? WHERE id=?', update_data)
        self.conn.commit()
        print("UPDATE Result: Value updated successfully")

    def UpdateCountRound(self):
        update_data = (self.param_update, self.param_field)
        self.cursor.execute(f'UPDATE {self.table_name} SET countround=? WHERE id=?', update_data)
        self.conn.commit()
        print("UPDATE Result: Value updated successfully")

    def fetchDataByField(self):
        self.cursor.execute(f'SELECT Item, Value FROM {self.table_name} WHERE Item=?', (self.param_field,))
        return dict(self.cursor.fetchall())


class deleteDataFromDB(DataBase):
    def __init__(self, table_name, param_item, param_data_list):
        self.field = param_item
        self.data_list = param_data_list
        super().__init__(table_name)

    def deleteData(self):
        placeholders = ','.join(['?'] * len(self.data_list))
        delete_query = f'DELETE FROM {self.table_name} WHERE {self.field} IN ({placeholders})'
        self.cursor.execute(delete_query, self.data_list)
        self.conn.commit()
        print("DELETE Result: Records deleted successfully")


if __name__ == '__main__':
    # for first time create app
    db = DataBase('testgot11')
    # # db.create_table()
    ret = db.fetchUserNum()
    print(ret)
    # db.closeDataBase()
    ret = db.fetchAllData()
    print(ret)
    print(len(ret))
    db.closeDataBase()


    # # for select user
    # # insert = insertDatabase('rungsudo', param_one=(1, "Rung", 3546))
    # # insert.executeOneApply()

    # # update input
    db = updateDatabase(table_name='testgot11', param_field=1, param_update='[2879\n5/9\n5789]')
    db.UpdateInput()


    # ret = db.fetchAllData()
    # print(ret)
    # db.closeDataBase()