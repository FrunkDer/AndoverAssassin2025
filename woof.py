import win32com.client
import csv
import random

outlook = win32com.client.Dispatch("Outlook.Application")

def sendall(message):
    emailstr = ''
    with open("killers.csv", mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            emailstr += f"{row[3]}; "
        

    body = f'''Hey Assassins,
{message}
    
Frank
    '''
    mail = outlook.CreateItem(0)
    mail.To = emailstr
    mail.Subject = "Unfriendly Assassin Email"
    mail.Body = body
    mail.Send()
    print("Email Sent Successfully")

def emailAssignment(first, last):
    data = []
    with open("killers.csv", mode="r", encoding="utf-8") as f:
        person = None
        reader = csv.reader(f)
        for row in reader:
            if row[1] == first and row[2] == last:
                #print(f"Found Person {row}")
                person = row.copy()
            data.append(row.copy())
        if not person:
            print("name not found")
            return False

    
    targetid = person[4]
    #print(f"Target id is {targetid}")
    target = None
    for row in data:
        #print(f"Row: {row}")
        if row[0] == targetid:
            target = row.copy()
            #print(f"Target = {target}")
            break
    if not target:
        print("target not found\n\n")
        return False
    
    mail = outlook.CreateItem(0)
    mail.To = person[3]
    mail.Subject = "Assassin - Target Assigned!"
    mail.Body = f'''Hi {person[1]},
    Your target for Assassin is {target[1]} {target[2]}.
    Happy Hunting,
    Frank'''
    mail.Send()
    print(f"Mail sent to {person[1]} {person[2]} successfully")
    
def shuffle():
    remainingids = []
    currentdata = []
    with open("killers.csv", mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                break
            remainingids.append(row[0])
            currentdata.append(row)
    random.shuffle(remainingids)

    newdata = []
    for i in range(len(remainingids)):
        for row in currentdata:
            if remainingids[i] == row[0]:
                newdata.append(row)
                newdata[i][4] = remainingids[i-1]
        
    with open("killers.csv", mode="w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(newdata)
    print("Successfully Shuffled Killers")

def kill(first, last, sendemail):
    data = []
    with open("killers.csv", mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
            #Find dead id and killer id
            if row[1] == first and row[2] == last:
                deadid = row[4]
                killerid = row[0]
    #remove dead id and get new target
    for i, row in enumerate(data):
        if row[0] == deadid:
            newtargetid = row[4]
            data.pop(i)
            break
    #assign new target
    for row in data:
        if killerid == row[0]:
            row[4] = newtargetid
            break
    
    with open("killers.csv", mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        print("Killed and reassigned target successfully.")

    if sendemail:
        emailAssignment(first, last)

def emailAllAssignments():
    with open("killers.csv", mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            emailAssignment(row[1], row[2])
    print("\nSent all emails!")
