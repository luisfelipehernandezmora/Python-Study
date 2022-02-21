'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]
'''
"""response = client.conversations_info(channel="C0XXXXXXX")

https://stackoverflow.com/questions/66311700/how-read-slack-channel-messages-using-python-slackclient]"""
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
#tokenp=os.environ["token"]
client = WebClient(token=os.environ["token"])
conversation_history = []
# ID of the channel you want to send the message to
channel_id = "TGHSHCM8S" # this is Coding Nomads channel Id

result = client.conversations_info(channel="CHRH0ED37")
conversation_history = result["messages"]
print(conversation_history)



# try:
#     # Call the conversations.history method using the WebClient
#     # conversations.history returns the first 100 messages by default
#     # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
#    # result = client.conversations_history(channel=channel_id)
#     result = client.conversations_info(channel="CHRH0ED37")
#     conversation_history = result["messages"]
#     print(conversation_history)
#     #Print results
#     logger.info("{} messages found in {}".format(len(conversation_history), id))

# except SlackApiError as e:
#     logger.error("Error creating conversation: {}".format(e))