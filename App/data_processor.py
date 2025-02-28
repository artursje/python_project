import os
import pandas as pd
import matplotlib.pyplot as plt
from .data_models import Student

class StudentDataProcessor:
    """Class for processing student data"""
    
    def __init__(self, input_file):
        """Initialize with the input file path
        
        Args:
            input_file (str): Path to the input CSV file
        """
        self.input_file = input_file
        self.students = []
        self.stats = {}
    
    def read_data(self):
        """Read student data from CSV file"""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file not found: {self.input_file}")
        
        # Use pandas to read the CSV file
        df = pd.read_csv(self.input_file)
        
        # Convert each row to a Student object
        for _, row in df.iterrows():
            student = Student.create_from_dict(row)
            self.students.append(student)
            
        print(f"Loaded {len(self.students)} students from {self.input_file}")
        return self.students
    
    def process_data(self):
        """Process the student data"""
        if not self.students:
            print("No students to process. Call read_data() first.")
            return
        
        # Calculate average grade by course
        course_grades = {}
        for student in self.students:
            if student.course not in course_grades:
                course_grades[student.course] = []
            course_grades[student.course].append(student.grade)
        
        # Calculate stats
        self.stats['course_avg'] = {course: sum(grades)/len(grades) 
                                   for course, grades in course_grades.items()}
        
        self.stats['overall_avg'] = sum(s.grade for s in self.students) / len(self.students)
        self.stats['top_student'] = max(self.students, key=lambda s: s.grade)
        self.stats['by_status'] = self._group_by_status()
        
        return self.stats
    
    def _group_by_status(self):
        """Group students by their status"""
        status_groups = {}
        for student in self.students:
            status = student.get_status()
            if status not in status_groups:
                status_groups[status] = []
            status_groups[status].append(student)
        return status_groups
    
    def generate_report(self, output_file):
        """Generate a report and save to file
        
        Args:
            output_file (str): Path to the output file
        """
        if not self.stats:
            print("No stats to report. Call process_data() first.")
            return
            
        with open(output_file, 'w') as f:
            f.write("Student Data Analysis Report\n")
            f.write("===========================\n\n")
            
            f.write(f"Total students: {Student.get_student_count()}\n\n")
            
            f.write("Average Grades by Course:\n")
            for course, avg in self.stats['course_avg'].items():
                f.write(f"  {course}: {avg:.2f}\n")
            
            f.write(f"\nOverall Average: {self.stats['overall_avg']:.2f}\n")
            
            f.write("\nTop Performing Student:\n")
            f.write(f"  {self.stats['top_student'].display_info()}\n")
            
            f.write("\nStudents by Status:\n")
            for status, students in self.stats['by_status'].items():
                f.write(f"\n  {status} ({len(students)} students):\n")
                for student in students:
                    f.write(f"    - {student.name}: {student.grade}\n")
        
        print(f"Report generated: {output_file}")
        return output_file
    
    def visualize_data(self, output_dir):
        """Create visualizations of the data
        
        Args:
            output_dir (str): Directory to save the visualizations
        """
        if not self.stats:
            print("No stats to visualize. Call process_data() first.")
            return
            
        os.makedirs(output_dir, exist_ok=True)
        
        # Create a bar chart of average grades by course
        courses = list(self.stats['course_avg'].keys())
        avgs = list(self.stats['course_avg'].values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(courses, avgs)
        plt.title('Average Grades by Course')
        plt.xlabel('Course')
        plt.ylabel('Average Grade')
        plt.ylim(0, 100)
        
        # Add the average values on top of each bar
        for i, avg in enumerate(avgs):
            plt.text(i, avg + 1, f'{avg:.1f}', ha='center')
        
        # Save the plot
        plot_path = os.path.join(output_dir, 'course_averages.png')
        plt.savefig(plot_path)
        plt.close()
        
        print(f"Visualization saved: {plot_path}")
        return plot_path 