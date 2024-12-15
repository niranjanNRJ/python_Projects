while True: # keep on asking for the mail address from user 
   
    email = input("Enter The E-mail To slice : ") # Takes the mail address from the user 
    
    if email.count('@') == 1 and len(email[:email.index('@')]) > 0 and  len (email[email.index('@')+1:]) > 3:
         #checks that given mail is vaild or not
        
        print("The Username For The E-mail : " + email[:email.index('@')]) # gives the username
        print("The Domain For The E-mail : "+ email[email.index('@')+1:]) # gives the domain name 
        print("\n") # leaves one space
    else:
        print("Invaild Email!!")
