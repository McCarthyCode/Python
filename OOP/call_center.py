class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self):
        print "id:    ", self.id
        print "name:  ", self.name
        print "number:", self.number 
        print "time:  ", self.time
        print "reason ", self.reason

call = Call(123, "Mia Rudolph", "800-555-1234", "2:31pm", "Just to say hi")
call.display()

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(calls)
    
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self

    def remove(self):
        self.calls = self.calls[1:]
        self.queue_size -= 1
        return self

    def info(self):
        print "length of queue:", self.queue_size
        for i in self.calls:
            print "  name:        ", i.name
            print "  phone number:", i.number

cc = CallCenter([
    Call(123, "Mia Rudolph", "800-555-1234", "2:31pm", "Just to say hi"),
    Call(133, "Joe Schmoe", "800-555-1212", "2:34pm", "In need of tech support"),
])

cc.info()
cc.remove().info()
cc.add(Call(133, "Jenny Smith", "800-555-1111", "2:42pm", "Trying to sell us stuff")).info()
