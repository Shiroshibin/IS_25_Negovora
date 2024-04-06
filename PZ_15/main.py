"""
Вариант 21
Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для
некоторой организации. БД должна содержать таблицу Обязанности со следующей
структурой записи: ФИО работника, вид дополнительной работы, сумма оплаты, срок.
"""

import sqlite3

class DB_AGENT():
    def __init__(self):
        with sqlite3.connect("PZ_15/DB.db") as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""create table if not exists resp(
                        f_name text not null,
                        type_resp text not null,
                        price real not null,
                        deadline text
            )""")

    def add_worker(self, f_name: str, type_resp: str, price: float, deadline: str):
        self.cur.execute("insert into resp values(?, ?, ?, ?)", (f_name, type_resp, price, deadline))
    
    def get_resp_by_worker(self, f_name: str):
        res: list = self.cur.execute("select * from resp where f_name == ?", (f_name,)).fetchall()
        return res
    
    def get_all_worker_by_resp(self, type_resp: str):
        res: list = self.cur.execute("select * from resp where type_resp == ?", (type_resp,)).fetchall()
        return res
    
    def get_all_resp_by_deadline(self, deadline: str):
        res: list = self.cur.execute("select * from resp where deadline == ?", (deadline,)).fetchall()
        return res
    
    def clear_db(self):
        self.cur.execute("delete from resp")

    def get_all_db(self):
        res: list = self.cur.execute("select * from resp").fetchall()
        return res
    
    def del_resp_by_name_and_deadline(self, f_name, deadline):
        self.cur.execute("delete from resp where f_name == ? and deadline == ?", (f_name, deadline))

    def __del__(self):
        self.con.commit()
        self.con.close()

if __name__ == "__main__":
    agent = DB_AGENT()

    # agent.clear_db()

    # agent.add_worker("Иван", "уборка", 29.99, "завтра")
    # agent.add_worker("Вася", "уборка", 29.99, "завтра")
    # agent.add_worker("Вася", "уборка", 29.99, "послезавтра")
    # agent.add_worker("Аркадий", "уборка", 29.99, "послезавтра")

    # print(agent.get_resp_by_worker("Вася"))

    # print(agent.get_all_worker_by_resp("уборка"))

    # print(agent.get_all_resp_by_deadline("завтра"))

    # print(agent.get_all_db())
    # agent.clear_db()
    # print(agent.get_all_db())

    
