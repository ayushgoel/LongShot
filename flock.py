import requests
import flock_constants


def create_flockML_for_tags(tags):
    return "<flockml>" +\
           "Missing release for: <br/>" + "<br/>".join([i.flockML() for i in tags]) +\
           "<flockml>"


def notify_group_about_missing_release_notes(flockML):
    payload = {"text": flockML,
               "flockml": flockML}
    response = requests.post(flock_constants.FLOCK_MESSAGE_HOOK, json=payload)
    try:
        print "Message posted with UID {0}".format(response.json()["uid"])
    except:
        pass
