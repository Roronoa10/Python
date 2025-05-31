import csv
def fcasi(reader):
    courseStudentInfo = dict()
    
    for row in reader:
        if row['Student Name'] not in courseStudentInfo:
            courseStudentInfo[row['Student Name']] = [row['Student Name']] 
            
        else:
            courseStudentInfo[row['Student Name']].append(row['Student Id'])
    print(courseStudentInfo)
try:
    with open ('/home/student_user/Class11/SampleFile.csv' ,'r') as file:
        reader = csv.DictReader(file)
        fcasi(reader)  
        
except:
    print('File dose not found')
finally:
    file.close()
