from flask import Flask
app = Flask(__name__)
# Define a simple class
class test:
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def sum(self):
     c=self.a+self.b
     print("Summation=",c)
     return " "

# Define a route
@app.route('/')
def rootcall():
    m=int(input("Enter the first number"))
    n=int(input("Enter the second number"))
    c=int(input("Enter the choice="))
    obj = test(m,n)  
    return obj.sum()

if __name__ == '__main__':
    app.run(debug=True)