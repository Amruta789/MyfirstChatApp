print("Content-type: text/html")
print("\n")
print("<h1>Hello World</h1>")

print("""
    <form name='myform' action='' method='POST'>
        <input type='text' name='username'/>
        <input type='submit' value='Submit' name='submit'/>
    </form>
    """) 

import cgi
form=cgi.FieldStorage()
user=str(form.getvalue('username'))
user=user.upper()
print(user)
  