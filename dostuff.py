import woof

'''
sendall(message, pth)

shuffle(pth)

emailAssignment(first, last, pth)

emailAllAssignments(pth)

kill(first, last, sendemail=Boolean, pth)
'''
message = '''
Hey gahng,
Thinking of doing a "meet the assassins" post for insta. Send me a pic of you and a quote you'd like to put on the post.
'''
woof.sendall(message, "killers.csv")

# woof.shuffle("killers.csv")

# woof.emailAllAssignments("killers.csv")

#woof.kill("Aeva", "Cleare", sendemail=True, pth="killers.csv")