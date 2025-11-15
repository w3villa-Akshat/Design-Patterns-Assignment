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
    