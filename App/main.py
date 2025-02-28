import os
from .data_processor import StudentDataProcessor
from .utils import ensure_directory_exists, validate_csv_file

def main():
    """Main function to run the student data analysis application"""
    print("Student Data Analysis Tool")
    print("=========================")
    
    # Define file paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    output_dir = os.path.join(base_dir, 'output')
    
    ensure_directory_exists(output_dir)
    
    input_file = os.path.join(data_dir, 'students.csv')
    output_file = os.path.join(output_dir, 'report.txt')
    
    # Validate input file
    if not validate_csv_file(input_file):
        print(f"Error: Input file not found or not a CSV file: {input_file}")
        return
    
    # Create processor, read and process data
    processor = StudentDataProcessor(input_file)
    
    try:
        processor.read_data()
        processor.process_data()
        processor.generate_report(output_file)
        processor.visualize_data(output_dir)
        
        print("\nProcessing complete!")
        print(f"- Report saved to: {output_file}")
        print(f"- Visualizations saved to: {output_dir}")
        
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == "__main__":
    main()
