age=int(input("Enter age= "))
grade=int(input("Enter your grade= "))
exm_score=(int(input("Enter exam score= ")))
prev_scl_name='Elite Academy'

if age>=6 and age <=12:
    if grade>=5:
        if prev_scl_name=='Elite Academy':
            if exm_score>=60:
                print("Eligible for admission")
            else:
                print("NotEligible")
        else:
            if exm_score>=70:
                print("Eligible for Admission")
            else:
                print("Not eligible")
    else:
        print("Not eligible")
else:
    print("Not Eligible")

    
    