# class OfficeDatabase:
#     __instance = None

#     def __init__(self):
#         if OfficeDatabase.__instance is not None:
#             raise Exception("This class is a Singleton!")
#         print("Database Connected")

#     @staticmethod
#     def get_instance():
#         if OfficeDatabase.__instance is None:
#             OfficeDatabase.__instance = OfficeDatabase()
#         return OfficeDatabase.__instance


class OfficeDatabase:
    __instance = None 
    
    def __inti__(self):
        if OfficeDatabase.__instance is not None:
            raise Execption("This Class is a Singleton!")
        print("Database Connected")
        
    @staticmethod
    def get_instance():
        if OfficeDatabase.__instance is None:
            OfficeDatabase.__instance = OfficeDatabase()
        return OfficeDatabse.__instance
    