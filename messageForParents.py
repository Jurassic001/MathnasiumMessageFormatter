import pyperclip
import time

# Get the first line of the name.txt file, which (hopefully) contains the user's name
file = open("name.txt", "r")
instructor_name = file.readline().strip()
file.close()

# Set up key phrases that we'll be needing
message_greet = "Good Afternoon! This is " + instructor_name + " from Mathnasium. "
message_end = " Have a great rest of your day!"

# Set up some of the basic variables we'll be using
hadHW = False
hwTopic = ""
hwComplete = ""
sing = ""
poss = ""


def compare(str1: str, str2: str) -> bool:
    """This method compares two strings

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: If the strings are the same return true, return false otherwise
    """
    if str1.lower() == str2.lower():
        return True
    else:
        return False


def output(msg: str):
    """This method copies the input to the clipboard, prints it, and gives some small flavor text before exiting the program

    Args:
        msg (str): A string containing the desired message
    """
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


def getTopics() -> str:
    """This method asks for all the topics that the student worked on and returns a formatted string that lists them out.
    \nFormat changes based on # of elements

    Returns:
        str: A string acting as a formatted list of topics (i.e. "addition, subtraction, and multiplication.")
    """
    topicList: list[str] = []
    topicNum: int = 1
    topics: str = ""
    print("Enter the name of a topic the student worked on")
    print("or")
    print("Type DONE to continue")
    while True:
        # Keep asking for topics until the user enters DONE
        topic = str(input("Topic #" + str(topicNum) + ": "))
        if topic == "DONE":
            break
        else:
            topicList.append(topic.lower())
            topicNum += 1
    match len(topicList):
        case 0:
            # If the user entered no topics return a generic message
            return "a variety of different topics. "
        case 1:
            topics = topicList[0] + "."
            return topics
        case 2:
            topics = topicList[0] + " and " + topicList[1] + "."
            return topics
        case _:
            topics = ", ".join(topicList[:-1]) + ", and " + topicList[-1] + "."
            return topics


def assessmentCheck():
    """This method asks if the student had an assessment, asks if they finished the assessment, and then gives an appropriate response.
    \nIf the student finished the assessment, it'll ask if they worked on any other topics and what those topics were.
    """
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


def homework():
    """This method sets global vars relating to homework status and content based on user input
    """
    hw = str(input("Did they do any homework? (Y/N): "))
    if compare(hw, "Y"):
        global hadHW
        global hwTopic
        global hwComplete
        hadHW = True
        hwTopic = " " + str(input("What was their homework about? "))
        hwComplete = str(input("Did the student complete their homework? (Y/N): "))
        if compare(hwComplete, "Y"):
            hwComplete = " finished "
        else:
            hwComplete = " made good progress over "


def gender():
    """This method globally sets student pronouns based on user input
    """
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
if pages:
    masChecks = int(input("Mastery checks finished: "))
else:
    masChecks = 0


# Format the mastery check information so it looks nice
if not masChecks:
    mastery = ""
elif masChecks == 1:
    mastery = " " + sing + " also completed one mastery check over those topics!"
else:
    mastery = " " + sing + " also completed " + str(masChecks) + " mastery checks over those topics!"


# Decide if the user had a great or a good session based on the # of pages completed
if pages > 10:
    session_status = " had an awesome session today, "
elif pages >= 5:
    session_status = " had a great session today, "
else:
    session_status = " had a good session today, "


# Slightly alter the message if the student did homework and/or at least one page
if hadHW and pages:
    message_summary = name + session_status + sing.lower() + hwComplete + poss.lower() + hwTopic.lower() + " homework. "
    message_topics = "After homework " + sing.lower() + " completed " + str(pages) + " pages over " + getTopics()
elif hadHW and not pages:
    message_summary = name + session_status + sing.lower() + hwComplete + poss.lower() + hwTopic.lower() + " homework."
    message_topics = ""
elif not hadHW and pages:
    message_summary = name + session_status + "completing " + str(pages) + " pages! "
    message_topics = sing + " worked on " + getTopics()
else:
    message_summary = name + " had a good session today at Mathnasium. "
    message_topics = sing + " worked on a variety of different topics."


# Add additional comments if you have any
comments = input("Please add any additional comments about the session: ")


# Check if any comments were submitted, add a space for formatting if comments were submitted, and add a period if there isn't any end punctuation.
if len(comments):
    comments = " " + comments
    if comments[len(comments)-1] != "." and comments[len(comments)-1] != "!":
        comments = comments + "."


message = message_greet + message_summary + message_topics + mastery + comments + message_end
output(message)
