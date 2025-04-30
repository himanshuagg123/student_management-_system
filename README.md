STUDENT MANAGEMENT SYETEM
DAY 1:
  1: created a student managemt system with the help of django and DRF in which i created app called student_records.
  2: in student records i created a model call Student which have three fields
      1: name(fieldtype:char)
      2: age(fieldtype:int)
      3: email(fieldtpye:email)
  3 i created a view in which i created two api one to get the data and one to post the data
  4: two learn about i created two types of function based and class based 
  5: api names:
      1: Student_details  : it is a function based api
      2: StudentDetailsPost : it is class based api

  6: create url pattern to call those api in urls.py
  7: to call those api i used POSTMAN 
      1: to get the list of student i used get request method  and url to get the data 
      2: to post the data i used post request method and type jason raw type data in body section of postman 
  8: 1: i learn somthing extra also like in my api part i manually type to get data in json format but to avoid it make code more readable and stable we can use serializer
    2: serializer is used to convert complex data types like Django model instances or querysets into native Python data types (such as dictionaries, lists, etc.) that can then be easily rendered into formats like JSON, XML, or others. This is essential for working with APIs in Django, especially with Django Rest Framework (DRF)
     
