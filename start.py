import github
import github_token
import repositories
import tagsparser
import flock


def main():
    g = github.Github(github_token.GITHUB_TOKEN)
    for repo in repositories.REPOSITORIES:
        data = g.get_tags_and_releases(repo["owner"], repo["name"], repositories.COUNT)
        print "Got", data
        unreleased_tags = tagsparser.find_unreleased_tags(data["tags"], data["releases"])
        text = ""
        for tag_data in data["tags"]:
            print "XYZ", tag_data
            if tag_data["name"] in unreleased_tags:
                text += "No release for tag {0}, it can be found on {1}".format(tag_data["name"], tag_data["target"]["commitUrl"])
        flock.notify_group_about_missing_release_notes(text)


if __name__ == '__main__':
    main()
