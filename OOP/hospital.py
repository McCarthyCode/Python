class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    
    def __repr__(self):
        return "<Patient object {}, name {}, allergies {}, bed_number {}>".format(
            self.id, self.name, self.allergies, self.bed_number)

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    
    def admit(self, patient):
        if len(self.patients) == self.capacity:
            return self
        patient.bed_number = raw_input("Enter bed number for " + patient.name + ": ")
        self.patients.append(patient)
        return self

    def discharge(self, id):
        for i in range(len(self.patients)):
            if self.patients[i].id == id:
                self.patients[i].bed_number = None
                self.patients.pop(i)
        return self

    def display_info(self):
        print "Displaying info for", self.name
        print "Capacity:", self.capacity
        print "List of patients:"
        for i in self.patients:
            print i
        return self

h = Hospital("St. Margarita's", 2)

h.admit(Patient(0, "John Doe", "none")).admit(Patient(1, "Jane Doe", "none")).display_info()
h.admit(Patient(2, "Janet Weiss", "none"))
h.discharge(1).admit(Patient(2, "Janet Weiss", "none")).display_info()
