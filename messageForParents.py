import pyperclip
import time

# Delete this line for personal use
from privateInfo import privateInfo

# Replace "privateInfo.name" with your name for personal use
instructor_name = privateInfo.name

# Set up key phrases that we'll be needing
message_greet = "Good Afternoon! This is " + instructor_name + " from Mathnasium. "
message_end = " Have a great rest of your day!"

# Set up some of the basic variables we'll be using
hadHW = False
hwTopic = ""
sing = ""
poss = ""


# This method compares strings
def compare(str1: str, str2: str):
    if str1 == str2 or str1 == (str.lower(str2)) or str1 == (str.capitalize(str2)):
        return True
    else:
        return False


# This method copies the message to the clipboard, prints it, and gives some small flavor text
def output(msg):
    pyperclip.copy(msg)
    print(msg)
    print("")
    print("")
    time.sleep(1)
    print("Message to parent copied to clipboard!")
    time.sleep(2)
    print("Closing window...")
    time.sleep(0.5)
    exit()


# This method asks for all the topics that the student worked on and returns a formatted string that lists them out
def getTopics():
    topicList = []
    topicNum = 1
    topics = ""
    print("Enter the name of a topic the student worked on")
    print("or")
    print("Type DONE to print message to parent")
    while True:
        # Keep asking for topics until the user enters DONE
        topic = str(input("Topic #" + str(topicNum) + ": "))
        if topic == "DONE":
            break
        else:
            topicList.append(topic.lower())
            topicNum += 1
    if len(topicList) == 1:
        topics = topicList[0] + "."
        return topics
    elif len(topicList) == 2:
        topics = topicList[0] + " and " + topicList[1] + "."
        return topics
    else:
        for i in range(len(topicList)):
            # Format the given topics into a neat sentence
            if i + 1 == len(topicList):
                topics = topics + "and " + topicList[i] + "."
                return topics
            else:
                topics = topics + topicList[i] + ", "


# This method asks if the student had an assessment, asks if they finished the assessment, and then gives an appropriate response.
# If the student finished the assessment, it'll ask if they worked on any other topics and what those topics were.
def assessmentCheck():
    assess = str(input("Did they have an assessment? (Y/N): "))
    if compare(assess, "Y"):
        assessFinish = str(input("Did they finish it? (Y/N): "))
        if compare(assessFinish, "Y"):
            otherWork = str(input("Did they do any other work? (Y/N): "))
            if compare(otherWork, "Y"):
                # Finished the assessment, worked on something else
                assessMessage = message_greet + name + " had a good session today! " + sing + " completed an assessment during the first half of the session. " + sing + " also worked on " + getTopics() + message_end
                output(assessMessage)
            else:
                # Finished the assessment, that was all they did
                assessMessage = message_greet + name + " had a good session today! " + sing + " worked on an assessment for the whole session and finished it. " + sing + " worked super hard and was very focused on the assessment." + message_end
                output(assessMessage)
        else:
            # Worked on the assessment, did not finish it
            assessMessage = message_greet + name + " had a good session today! " + sing + " worked on an assessment for the whole session and " + sing.lower() + " was pretty focused. " + sing + "'ll keep working on it next time." + message_end
            output(assessMessage)


# This method changes our response based on if the student did homework
def homework():
    hw = str(input("Did they do any homework? (Y/N): "))
    if compare(hw, "Y"):
        global hadHW
        global hwTopic
        hadHW = True
        hwTopic = str(input("What was their homework about? "))


# This method gets student pronouns
def gender():
    global sing
    global poss
    sing = str(input("Is the student a He or She? "))
    if compare(sing, "He"):
        sing = str("He")
        poss = str("His")
    elif compare(sing, "She"):
        sing = str("She")
        poss = str("Her")
    else:
        sing = str("They")
        poss = str("Their")


"""
Below is where everything comes together
"""

# Ask for some simple establishing information about the student
name = str(input("Student name: "))
gender()
# Run the assessment function to determine if they did any assessment work
assessmentCheck()
# Did they work on any homework?
homework()
# If they had a regular session then ask how many pages and mastery checks they completed
pages = int(input("Pages finished: "))
masChecks = int(input("Mastery checks finished: "))


# Format the mastery check information so it looks nice :)
if masChecks == 0:
    mastery = ""
elif masChecks == 1:
    mastery = " " + sing + " also completed one mastery check over those topics!"
else:
    mastery = " " + sing + " also completed " + str(masChecks) + " mastery checks over those topics!"

# Decide if the user had a great or a good session based on the # of pages completed (make pages a string afterwards)
if pages > 10:
    session_status = " had an awesome session today, "
elif pages >= 5:
    session_status = " had a great session today, "
else:
    session_status = " had a good session today, "
pages = str(pages)

# Organize all of our collected information and ship it out
if hadHW:
    message_summary = name + session_status + sing.lower() + " made good progress over " + poss.lower() + " " + hwTopic.lower() + " homework. "
    message_topics = "After homework " + sing.lower() + " completed " + pages + " pages over " + getTopics()
else:
    message_summary = name + session_status + "completing " + pages + " pages! "
    message_topics = sing + " worked on " + getTopics()

# Add additional comments if you have any
comments = input("Please add any additional comments about the session: ")

# Check if any comments were submitted and add a space for formatting if comments were submitted.
alphaList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range (len(alphaList)):
    if comments.__contains__(alphaList[i]):
        comments = " " + comments
        break

message = message_greet + message_summary + message_topics + mastery + comments +  message_end
output(message)
