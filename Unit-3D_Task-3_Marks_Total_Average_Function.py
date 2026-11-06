first_subject=float(input("enter first subject marks:"))
second_subject=float(input("enter second subject marks:"))
third_subject=float(input("enter third subject marks:"))
def average (first_subject,second_subject,third_subject):
    total=first_subject+second_subject+third_subject
    average_of_that=total/3
    return total,average_of_that
total,average_of_that =average (first_subject,second_subject,third_subject)
print("total marks are",total)
print("The average of three subjects is",average_of_that)