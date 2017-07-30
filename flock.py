import requests
import flock_constants


# def text_for_missing_releases():


def notify_group_about_missing_release_notes(text):
    payload = {"text": text}
    response = requests.post(flock_constants.FLOCK_MESSAGE_HOOK, json=payload)
    try:
        print "Message posted with UID {0}".format(response.json()["uid"])
    except:
        pass
