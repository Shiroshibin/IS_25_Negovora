import json



class data_agent():
    
    def __init__(self):
        self.data_dict: dict = self.read_data()

    def read_data(self):
        with open("data/data.json", "r+", encoding="UTF-8") as file:
            data:dict = json.load(file)
        return data

    def save_data(self):
        with open("data/data.json", "r+", encoding="UTF-8") as file:
            data:dict = json.load(file)
        with open("data/data.json", "w+", encoding="UTF-8") as file:
            data.update(self.data_dict)
            json.dump(data, file, indent = 4)

    def check_reg(self, user_id):
        if str(user_id) in self.data_dict.keys(): return True
        else: self.data_dict[str(user_id)] = {"score": 0}



data_agent = data_agent()