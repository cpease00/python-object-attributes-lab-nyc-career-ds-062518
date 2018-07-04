class Driver:
    
    def __init__(self):
#         self._first_name = first_name
#         self._last_name = last_name
#         self._miles_driven = miles_driven
#         self._rating = rating
        pass
        
    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, first):
        self._first = first
        
    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, last):
        self._last = last
        
    @property
    def miles_driven(self):
        return self._miles_driven
    
    @miles_driven.setter
    def miles_driven(self, miles_driven):
        self._miles_driven = miles_driven

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        self._rating = rating
    
    def greet_passenger(self):
        print("Hello! I'll be your driver today. My name is " + self.first + " " + self.last)