class Person:
    """Base class for all person types in our system"""
    
    def __init__(self, id, name, age):
        """Initialize a Person object
        
        Args:
            id (int): Unique identifier
            name (str): Person's full name
            age (int): Person's age
        """
        self.id = id
        self.name = name
        self.age = age
    
    def display_info(self):
        """Display basic information about the person"""
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"
    
    @classmethod
    def create_from_dict(cls, data_dict):
        """Class method to create a Person from a dictionary
        
        Args:
            data_dict (dict): Dictionary containing person data
            
        Returns:
            Person: A new Person instance
        """
        return cls(
            id=data_dict['id'],
            name=data_dict['name'],
            age=data_dict['age']
        )


class Student(Person):
    """Student class that inherits from Person"""
    
    # Class attribute to track the number of students
    student_count = 0
    
    def __init__(self, id, name, age, course, grade):
        """Initialize a Student object
        
        Args:
            id (int): Unique identifier
            name (str): Student's full name
            age (int): Student's age
            course (str): Course name
            grade (int): Student's grade in the course
        """
        # Call the parent class constructor
        super().__init__(id, name, age)
        self.course = course
        self.grade = grade
        
        # Increment the student count
        Student.student_count += 1
    
    def display_info(self):
        """Override the display_info method to include student-specific information"""
        basic_info = super().display_info()
        return f"{basic_info}, Course: {self.course}, Grade: {self.grade}"
    
    def get_status(self):
        """Determine the student's status based on grade"""
        if self.grade >= 90:
            return "Excellent"
        elif self.grade >= 80:
            return "Good"
        elif self.grade >= 70:
            return "Satisfactory"
        else:
            return "Needs Improvement"
    
    @classmethod
    def get_student_count(cls):
        """Class method to return the total number of students"""
        return cls.student_count
    
    @classmethod
    def create_from_dict(cls, data_dict):
        """Class method to create a Student from a dictionary
        
        Args:
            data_dict (dict): Dictionary containing student data
            
        Returns:
            Student: A new Student instance
        """
        return cls(
            id=int(data_dict['id']),
            name=data_dict['name'],
            age=int(data_dict['age']),
            course=data_dict['course'],
            grade=int(data_dict['grade'])
        ) 