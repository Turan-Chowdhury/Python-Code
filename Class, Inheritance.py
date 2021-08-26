class Phone :
    def call(self) :
        print("You can call")

    def message(self) :
        print("You can message")

class Samsung(Phone) :
    def Photo(self) :
        print("You can take photo")

s = Samsung()
s.call()
s.message()
s.Photo()

print(issubclass(Samsung,Phone))
