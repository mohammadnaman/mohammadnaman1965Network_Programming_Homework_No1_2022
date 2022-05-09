## Q1
# A
graduatedstudent=["bassam","rana","mohannad","sara","joudy"] #انشاء قائمة تحوي اسماء الطلاب
for i in range(5) :                                          # هذه اضافة لاعطاء المستخدم عدة محاولات
    
    name=input("enter your name:")                           # طلب من المستخدم ادخال الاسم المراد معرفة نتيجته واسناده لمتغير

    if name in graduatedstudent:                             # اختبار شرط اذا كان الطالب متخرج 
       print("great...you are graduated")
       break
    else:
    
       print("opss... sory you aren't graduated")