import requests
import flock_constants


def create_flockML_for_tags(repo_owner, repo_name, tags):
    if not tags:
        return None
    return "<flockml>" +\
           "({0}/{1}) missing release: <br/>".format(repo_owner, repo_name) +\
           "<br/>".join([i.flockML() for i in tags]) +\
           "</flockml>"


def notify_group_about_missing_release_notes(flockML):
    payload = {"text": flockML,
               "flockml": flockML}
    response = requests.post(flock_constants.FLOCK_MESSAGE_HOOK, json=payload)
    try:
        print "Message posted with UID {0}".format(response.json()["uid"])
    except:
        pass
