
def find_unreleased_tags(tags, releases):
    set_of_tags = set([i["name"] for i in tags])
    set_of_released_tags = set([i["tag"]["name"] for i in releases])
    print set_of_tags
    print set_of_released_tags
    return set_of_tags.difference(set_of_released_tags)
