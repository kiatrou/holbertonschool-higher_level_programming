#!/usr/bin/python3


attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Template
template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

def generate_invitations(template, attendees):
    # check if template is a string
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    # check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return
    # check if the template is empty
    if template == "":
        print("Template is empty, no output files generated.")
        return
    # check if the attendees list is emtpy
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    # check if each item in attendees is a dictionary
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: each attendee must be a dictionary")
            return

    # enumerate gives both the position and the item when looping through a list
    for i, attendee in enumerate(attendees):
        # start with the original template
        personalised_invitation = template

        # replace each placeholder, if the key doesn't exist, use N/A
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # replace "None" string with N/A
        if event_date == None:
            event_date = "N/A"
        if event_location == None:
            event_location = "N/A"
        if name == None:
            name = "N/A"
        if event_title == None:
            event_title = "N/A"

        # do the actual replacement
        personalised_invitation = personalised_invitation.replace("{name}", name)
        personalised_invitation = personalised_invitation.replace("{event_title}", event_title)
        personalised_invitation = personalised_invitation.replace("{event_date}", event_date)
        personalised_invitation = personalised_invitation.replace("{event_location}", event_location)

        # create filename and start from 1
        filename = f"output_{i + 1}.txt"
        # write to file
        try:
            with open(filename, 'w') as file:
                file.write(personalised_invitation)
        except PermissionError:
            print(f"Don't have permission to create file output_{i+1}.txt")
        except OSError:
            print(f"System error creating file output_{i+1}.txt")

generate_invitations(template, attendees)