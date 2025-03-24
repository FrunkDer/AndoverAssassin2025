import woof

'''
sendall(message, pth)

shuffle(pth)

emailAssignment(first, last, pth)

emailAllAssignments(pth)

kill(first, last, sendemail=Boolean, pth)
'''
message = '''
Welcome back from break guys!!
You should all have gotten an email with your target.
Here's your task: If you're caught walking, you're out. Running, skipping, it's fair game, but if I see a picture of you walking, you're done.
'''
woof.sendall(message, "killers.csv")

woof.shuffle("killers.csv")

woof.emailAllAssignments("killers.csv")

#woof.kill("Evie", "Lagrandeur", True, "killers.csv")