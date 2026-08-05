class student:
    name='Manoj'
    roll_no=  513
    aadhar='1234 5678 9012'
    panno='ABCDE1234F'
    def __init__(self):
        print('This is my first constructor in OOPS')
    def read(self):
        print(f'{self.name} is reading')
    def write(self):
        print(f'{self.name} is writing')
k=student()
print(k.name)
print(k.roll_no)
print(k.aadhar)
print(k.panno)
k.read()
k.write()