
students= ["Jaden", "Tiana","Frank","Mo"]
year_started= [2018,2019,2020,2021]

def report(students, year_started):
    return f"{students} started PerScholas in {year_started} and currently looking for jobs"
    
print("Welcome to PerScholas Directory of students...")
user_input= input("Please type the student name to check: ").capitalize()

for person in students:
    result= f"Sorry! {user_input} cannot be found"
    if user_input == person:
            i= students.index(person)
            result= report(person, year_started[i])
            break
        
print(result)



