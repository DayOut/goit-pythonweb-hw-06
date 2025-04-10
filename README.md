To run app:
```
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
# create .env file with your actual pass for DB (example in repo)

# to create fake data in DB
poetry run python -m goit_pythonweb_hw_06.seed

# to show required results
poetry run python -m goit_pythonweb_hw_06.my_select
```

Example response from app:
```
 poetry run python -m goit_pythonweb_hw_06.my_select
-----------------------------------------------------
1. Top 5 students by avg grade:
('Michael Stewart', 4.518501862203907)
('Jesse Burns', 4.229559921935097)
('Mallory Mullins', 3.8253405602029784)
('Alicia Turner', 3.7193041140255594)
('Caitlin Tucker', 3.573003620379412)
-----------------------------------------------------
2. Student with highest grade at subject with id 2:
('Debra Taylor', 4.56431200374496)
-----------------------------------------------------
3. Average per group for subject 1:
[('Group 2', 3.0854764945061577), ('Group 3', 2.94218509830462), ('Group 1', 3.287865711508228)]
-----------------------------------------------------
4. Average grade for thread:
2.987150332507904
-----------------------------------------------------
5. Courses by teacher 2:
[('Approach',)]
-----------------------------------------------------
6. Students in group 2:
('Vickie Fry',)
('Elizabeth Phillips',)
('Jeremy Fischer',)
('Angel Johnson',)
('Stephanie Santiago',)
('Anthony Brewer',)
('Erica Pham',)
('Caitlin Tucker',)
('Alicia Turner',)
('Benjamin Hernandez',)
('Sarah Campbell',)
('Jason Wilson',)
('Debra Taylor',)
('Linda Porter',)
('Brandon Gamble',)
-----------------------------------------------------
7. Grades in group 2 at subject 1:
('Vickie Fry', 2.077523632177584)
('Vickie Fry', 4.755996378619814)
('Vickie Fry', 3.816809947583235)
('Elizabeth Phillips', 4.7965038965616085)
('Jeremy Fischer', 3.079381782228174)
('Angel Johnson', 1.247298937427558)
('Stephanie Santiago', 3.9961606547673845)
('Erica Pham', 2.8715544247166718)
('Erica Pham', 1.4639764616780777)
('Caitlin Tucker', 3.3858369237104315)
('Caitlin Tucker', 1.9857819632082419)
('Caitlin Tucker', 3.7876632674804664)
('Caitlin Tucker', 2.727489387455325)
('Benjamin Hernandez', 3.663229711468569)
('Sarah Campbell', 2.053997096253088)
('Sarah Campbell', 3.841836075598683)
('Jason Wilson', 1.7694725782908298)
('Linda Porter', 4.218063781885093)
-----------------------------------------------------
8. Average grade for teacher 1:
3.0840349720325513
-----------------------------------------------------
9. Student 1 subjects:
('Approach',)
('Budget',)
('Production',)
-----------------------------------------------------
10. Subjects for student 3 taught by teacher 1:
[('Recognize',)]
```