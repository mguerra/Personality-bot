import os

answerdict = {'A':5,'B':4,'C':3,'D':2}


os.system('clear')
answerlist = []
print "Hello, what is your name?\n"
name = raw_input()
os.system('clear')
print "Hello "+name+" how are you?\n"
raw_input()

os.system('clear')
print "Oh, I see. Anyways, you're probably wondering what kind of bot I am. What kind of bot do you think I am?\n"
raw_input()

os.system('clear')
print "Ah, close, but no cigar, I'm a personality bot! I will ask you some questions and I'll tell you what kind of personality you are. Would you like to do that? Please answer with a simple yes or no.\n"
answer_one = raw_input()

if answer_one.lower() == "yes":
    print "Cool, lets start then! (press enter)" 
elif answer_one.lower() == "no": 
    print "Oh, you party pooper! This is my game, press enter please :)"
else: 
    print "Too bad kid, you have no choice! muah ha ha! press enter please :)"
    
    raw_input()
    
os.system('clear')
print "From the following questions which statement do you most relate to? Please choose only one answer\n"
print "A. I like art / I consider myself an artist"
print "B. I like to be organized / I hate clutter"
print "C. I am very energetic / I am the life of the party"
print "D. I like to help others / my friends would say I'm a friendly person\n"  

answerlist.append(raw_input())
os.system('clear')
print "thats really cool! We should get some ice cream sometime. Anyways, here's your next question "+name+"!\n"
print "From the following questions which statement do you most relate to? Please choose only one answer"
print "A. I like to try new things and experiment with different stuff"
print "B. I like it when my room is clean and organized"
print "C. It's easy for me to make friends"
print "D. I tend to help others before I help myself\n"  
    
answerlist.append(raw_input())
os.system('clear')
print "Wow! You're a really interesting person! I bet we would be best friends if I were a real person... :( oh well, here's your next question buddy!\n"
print "From the following questions which statement do you most relate to? Please choose only one answer"
print "A. I want to travel a lot when I am older"
print "B. Most of my friends would say I am a perfectionist"
print "C. I'm not quiet around strangers"
print "D. Even though I disagree, I let others get their way because I want to get along with them\n"  
    
answerlist.append(raw_input())
os.system('clear')
print "Hmmm, I think we have a lot in common! You know, being a robot is a pretty lonely life. If I ever become a human, we should hang out! Here's your last question!\n"
print "From the following questions which statement do you most relate to? Please choose only one answer\n"
print "A. When someone disagrees with me, I am open to listening to what they say and respect what they say."
print "B. Some people say I'm a predictable person"
print "C. I don't like to be alone"
print "D. I tend to be quiet most of the time because I don't want to bug anyone.\n"  
answerlist.append(raw_input())
os.system('clear')

for person in answerlist:
    print "You are a " +person+  
    
    20 = 
    
