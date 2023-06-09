from datetime import date

class Jwan:
    persons = [{"ethel": {"birth_date": date(2004, 5, 4), "gender": "female", "fullname": "Ethel Densing"}},
        {"kylle": {"birth_date": date(2003, 11, 7), "gender": "male", "fullname": "Kylle Aliño"}},
        {"john marlie": {"birth_date": date(2004, 5, 23), "gender": "male", "fullname": "John Marlie Compas"}},
        {"emarie": {"birth_date": date(2004, 8, 16), "gender": "female", "fullname": "Emarie Tulod"}},
        {"josuan": {"birth_date": date(2004, 2, 21), "gender": "male", "fullname": "Josuan Leonardo Hulom"}}]

    def __init__(self, gname: str = None,password = None):
        self.password = password
        if gname is not None:
            self.person(gname.lower())
            if gname.lower() == "josuan":
                print("The dev who created this code.")
        self.congratulate()

    def congratulate(self):
        today = date.today()
        for person in self.persons:
            for name, info in person.items():
                age = today.year - info["birth_date"].year
                birthday_passed = today.month > info["birth_date"].month or (
                        today.month == info["birth_date"].month and today.day >= info["birth_date"].day
                )
                if birthday_passed and today.month == info["birth_date"].month and today.day == info["birth_date"].day:
                    print(f"Happy birthday, {name.capitalize()}! You are now {age} years old.")
    
    def N_n(self,jname):
        if jname.lower() == "ethel n. densing" or jname.lower() == "ethel densing" or jname.lower() == "densing ethel" or\
            jname.lower() == "densing ethel n.":
            return "ethel"
        elif jname.lower() == "kylle b. aliño" or jname.lower() == "kylle aliño" or jname.lower() == "aliño kylle" or\
            jname.lower() == "aliño kylle b.":
            return "kylle"
        elif jname.lower() == "john marlie n. compas" or jname.lower() == "john marlie compas" or jname.lower() == "compas john marlie" or\
            jname.lower() == "compas john marlie n.":
            return "john marlie"
        elif jname.lower() == "emarie tulod" or jname.lower() == "tulod emarie":
            return "emarie"

    def person(self,name: str = None):

        if name is not None:
            name = self.N_n(name)
        
        if name is None:
            if self.password is not None and self.password == 2004221:
                today = date.today()
                for person in self.persons:
                    for name, info in person.items():
                        age = today.year - info["birth_date"].year
                        birthday_passed = today.month > info["birth_date"].month or (
                                today.month == info["birth_date"].month and today.day >= info["birth_date"].day
                        )
                        if birthday_passed:
                            if today.month == info["birth_date"].month and today.day == info["birth_date"].day:
                                age += 1
                                print(f"Happy birthday, {name.capitalize()}! They are now {age} years old.")
                            else:
                                if name != "josuan":
                                    print(f"{name.capitalize()} is now {age} years old and is {info['gender']}")
                                else:
                                    print(f"{name.capitalize()} is now {age} years old and is {info['gender']} (The dev. of this code)")
                        else:
                            if name != "josuan":
                                print(f"{name.capitalize()} is {age - 1} years old and is {info['gender']}")
                            else:
                                print(f"{name.capitalize()} is {age - 1} years old and is {info['gender']} (The dev. of this code)")
            else:
                if self.password is None:
                    print('Enter password! "Jwan(password=???????).person()"')
                elif self.password != 2004221:
                    print("Wrong password!")
                
        else:
            found_person = False
            for person in self.persons:
                for person_name, info in person.items():
                    if person_name.lower() == name.lower():
                        age = date.today().year - info["birth_date"].year
                        self.get_fullname(name.lower())
                        print(f"is {age} years old and is {info['gender']}.")
                        found_person = True
                        break
            if not found_person:
                print("Person not found.")

    def get_birthday(self, birthday):
        for person in self.persons:
            for name, info in person.items():
                if info["birth_date"].month == birthday.month and info["birth_date"].day == birthday.day:
                    print(f"The person with the birthday {birthday} is {name.capitalize()}.")
                    return
        print("No person has a birthday on that date.")

    def get_gender(self, name):
        name = name.lower()
        for person in self.persons:
            for person_name, info in person.items():
                if name.lower() == person_name.lower():
                    print(f"{name.capitalize()}: is {info['gender'].capitalize()}")
                    return
        print("person not found.")

    def get_fullname(self, name: str = None):
        if name is not None:
            name = name.lower()
            for person in self.persons:
                if name in person:
                    getfullname = person[name]['fullname']
                    print(getfullname, end=' ')
                    return
            print(f"No person with the name '{name}' found.")
        else:
            for person in self.persons:
                for full in person.values():
                    print(full['fullname'])

wan = Jwan().get_fullname("kylle")