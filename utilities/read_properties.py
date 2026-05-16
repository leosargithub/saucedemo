import  configparser


config = configparser.RawConfigParser()

config.read(".\\configurations\\config.ini")

class Read_Config:
     @staticmethod
     def get_page_url():
        url = config.get('common info','page_url')
        return url

     @staticmethod
     def get_username():
         username = config.get('common info', 'username')
         return username

     @staticmethod
     def get_password():
         password = config.get('common info', 'password')
         return password

     @staticmethod
     def get_invalid_password():
         invalid_password = config.get('common info', 'invalid_password')
         return invalid_password