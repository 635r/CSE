class Person(object):
    def __init__(self, name, education, job):
        self.name = name
        self.education = education
        self.job = job

    def work(self):
        print("%s goes to work" % self.name)


class Employee(object):
    def __init__(self, name, education, job):
        (super,Employee).__init__("name", "education", "job")

    def work(self):
        print("%s goes to work" % self.name)


class Programmer(object):
    def __init__(self, name, education, jobs):
        (super, Programmer).__init__("name", "education", "job")

    def work(self):
        print("%s goes to work" % self.name)