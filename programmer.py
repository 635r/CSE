class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, education, job):
        super(Employee, self).__init__(name, education)
        self.job = job

    def work(self):
        print("%s goes to work" % self.name)


class Programmer(Employee):
    def __init__(self, name, education, job):
        super(Programmer, self).__init__(name, education, job)

    def work(self):
        print("%s goes to work" % self.name)
