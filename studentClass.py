from datetime import date


class Student:
    def __init__(self, stuID, name, dob, classification):
        self.__stuID = stuID
        self.__name = name
        self.__dob = dob
        self.__classification = classification

    def set_age(self, dob):
        self.__dob = dob
        if dob == 14:
            classification = "F"
        elif dob == 15:
            classification = "S"
        elif dob == 16:
            classification = "Jr"
        elif dob == 17:
            classification = "Sr"

    def set_class(self, classification):
        self.__classification = classification

    def set_dates(self, classification):
        if classification == "F":
            reg_date = "4/10 thru 4/12"

    def get_age(self):
        return self.__dob

    def get_class(self):
        return self.__classification

    def get_date(self):
        return reg_date
