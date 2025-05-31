import csv
try:
    with open ('/home/student_user/h/SampleFile.csv' ,'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['Program'].startswith('BBA'):
             print(len(row))
             break
        
except:
    print('File dose not found')
finally:
    file.close()
