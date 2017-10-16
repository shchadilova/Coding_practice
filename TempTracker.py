# Problem : 
# Write a class TempTracker with these methods:
# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean of all temps we've seen so far
# get_mode()—returns a mode of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), # get_mean(), and get_mode() over speeding up the insert() method.

class TempTracker:
    
    def __init__(self):
        
        #max T
        self.max_temperature = 0
        #min T
        self.min_temperature = 110
        #mean T
        self.sum_of_temperatures = 0
        self.number_of_temperatures = 0
        self.mean = None
        #mode T
        self.frequency_counter = [0] * 111
    	self.max_counter = 0
        self.mode = None
        
    def insert(self, T):
        #min T
        if self.min_temperature > T:
            self.min_temperature = T
        #max T
        if self.max_temperature < T:
            self.max_temperature = T
        #mean T    
        self.number_of_temperatures +=1
        self.sum_of_temperatures += T
        self.mean = self.sum_of_temperatures /  self.number_of_temperatures
        #mode T    
        self.frequency_counter[T] +=1 
        if self.frequency_counter[T] > self.max_counter:
            self.max_counter = self.frequency_counter[T]
            self.mode = T
        
    def get_max(self):
		return self.max_temperature
    def get_min(self):
		return self.min_temperature
    def get_mean(self):
        return self.mean
    def get_mode(self):
        return self.mode
            
        
        

    

# check some test cases:

tracker = TempTracker()
tracker.insert(1)
tracker.insert(2)
tracker.insert(3)
tracker.insert(1)
tracker.insert(0)
print("min: " + str(tracker.get_min()))
print("max: " + str(tracker.get_max()))
print("mean: " + str(tracker.get_mean()))
print("mode: " + str(tracker.get_mode()))
