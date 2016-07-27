# import files into variable called 'text'
import csv

'''with open("filename.csv") as csvfile:
    reader = csv.DictReader(csvfile)
'''

f = open('filename.csv', 'rb')
reader = csv.reader(f)
headers = reader.next()

column = {}

for h in headers:
    column[h] = []

for row in reader:
    for h, v in zip(headers,row):
        column[h].append(v)

file = open('info.txt', 'r')
temp = file.readlines()
file.close()
text_template = "".join(temp)

for i in range(0,len(column["First_Name"])):

    text = text_template
    
    text = text.replace("P_name", column["First_Name"][i])
    text = text.replace("AIR_OR_TRAIN", column["Where"][i])
    text = text.replace("HOST", column["Host"][i])
    text = text.replace("H_PHONE", column["Host_Phone"][i])
    text = text.replace("DRIVER1", column["Driver1"][i])
    text = text.replace("D1_phone", column["Driver1_Phone"][i])
    text = text.replace("DRIVER2", column["Driver2"][i])
    text = text.replace("D2_phone", column["Driver2_Phone"][i])
    text = text.replace("ARRIVAL_DAY", column["ArrivalDay"][i])
    text = text.replace("ARRIVAL_TIME", column["ArrivalTime"][i])
    text = text.replace("DEP_DAY", column["DepDay"][i])
    text = text.replace("DEP_TIME", column["DepTime"][i])

    
    if column["Host"][i].find("and ") >= 0:
        text = text.replace("RESPECTIVELY", "respectively")
        text = text.replace("(s)", "s")
        text = text.replace("IS_ARE", "are")
        
    else:
        text = text.replace("RESPECTIVELY", "")
        text = text.replace("(s)", "")
        text = text.replace("IS_ARE", "is")

    new_file = column["First_Name"][i] + "_" + column["Last_Name"][i] + ".txt"
    new_txt_file = open(new_file, "w")
    new_txt_file.write(text)
    new_txt_file.close()
    

    

