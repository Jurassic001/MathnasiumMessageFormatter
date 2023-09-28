import pyperclip
import time

# If you want to download this for personal use you'll need to change the instructor name
instructor_name = "<Your Name Here>"

# Set up key phrases that we'll be needing
message_greet = "Good Afternoon! This is " + instructor_name + " from Mathnasium. "
message_end = " Have a great rest of your day!"


# This function copies the message to the clipboard, prints it, and gives some small flavor text
def output(msg):
    pyperclip.copy(msg)
    print(msg)
    print("")
    print("")
    time.sleep(1)
    print("Message to parent copied to clipboard!")
    time.sleep(2)
    print("Closing window in 3 seconds...")
    time.sleep(3)
    exit()


# This function asks for all the topics that the student worked on and returns a formatted string that lists them out
def getTopics():
    topicList = []
    topicNum = 0
    topics = ""
    print("Enter the name of a topic the student worked on")
    print("or")
    print("Type DONE to print message to parent")
    while True:
        # Keep asking for topics until the user enters DONE
        topicNum += 1
        topic = str(input("Topic #" + str(topicNum) + ": "))
        if topic == "DONE":
            break
        else:
            topicList.append(topic)
    for i in range(len(topicList)):
        # Format the given topics into a neat sentence
        if i + 1 == len(topicList):
            topics = topics + "and " + topicList[i] + ". "
            return topics
        else:
            topics = topics + topicList[i] + ", "


# This function asks if the student had an assessment, asks if they finished the assessment, and then gives an appropriate response.
# If the student finished the assessment, it'll ask if they worked on any other topics and what those topics were.
def assessmentCheck():
    assess = str(input("Did they have an assessment? (Y/N): "))
    if assess.__contains__("Y") or assess.__contains__("y"):
        assessFinish = str(input("Did they finish it? (Y/N): "))
        if assessFinish.__contains__("Y") or assessFinish.__contains__("y"):
            otherWork = str(input("Did they do any other work? (Y/N): "))
            if otherWork.__contains__("Y") or otherWork.__contains__("y"):
                # Finished the assessment, worked on something else
                assessMessage = message_greet + name + " had a good session today! " + gender + " completed an assessment during the first half of the session. " + gender + " also worked on " + getTopics() + message_end
                output(assessMessage)
            else:
                # Finished the assessment, that was all they did
                assessMessage = message_greet + name + " had a good session today! " + gender + " worked on an assessment for the whole session and finished it. " + gender + " worked super hard and was very focused on the assessment." + message_end
                output(assessMessage)
        else:
            # Worked on the assessment, did not finish it
            assessMessage = message_greet + name + " had a good session today! " + gender + " worked on an assessment for the whole session and " + gender.lower() + " was pretty focused. " + gender.lower() + "'ll keep working on it next time." + message_end
            output(assessMessage)


"""
Below is where everything comes together
"""

# Ask for some simple establishing information about the student
name = str(input("Student name: "))
gender = str(input("Is the student a He or She? "))
# Run the assessment function to determine if they did any assessment work
assessmentCheck()
# If they had a regular session then ask how many pages and mastery checks they completed
pages = str(input("Pages finished: "))
masChecks = int(input("Mastery checks finished: "))


# Format the mastery check information so it looks nice :)
if masChecks == 0:
    mastery = ""
if masChecks == 1:
    mastery = gender + " also completed one mastery check over those topics!"
else:
    mastery = gender + " also completed " + str(masChecks) + " mastery checks over those topics!"


# Organize all of our collected information and ship it out
message_summary = name + " had a good session today, completing " + pages + " pages! "
message_topics = gender + " worked on " + getTopics()
message = message_greet + message_summary + message_topics + mastery + message_end
output(message)
