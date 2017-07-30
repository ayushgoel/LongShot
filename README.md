This repository creates a python framework to notify when your github repo has an unreleased tag.

Motivation
---

Many of the repositories that handle a pod (cocoapods) release a new version using a tag but forget to create a [release](https://help.github.com/articles/about-releases/). This becomes an issue for consumers of the pod. They are unable to understand the updates added a new version.

Usage
---

1. [Create a github token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)

2. Create `github_token.py` and add following line to it

    ```python
    GITHUB_TOKEN = "<Token from Github>"
    ```

3. If you want notifications on [flock](https://flock.com/), [create an incoming webhook](https://docs.flock.com/display/flockos/Create+An+Incoming+Webhook)

4. Create `flock_constants.py` and add following line to it

    ```python
    FLOCK_MESSAGE_HOOK = "<HOOK_URL>"
    ```

5. Update `repositories.py` with the repositories you want to keep an eye on.
5. `start.py` is the entry point for this repository. Use python 2+ version to run it.

:v: enjoy.

Author
---

Ayush Goel, ayushgoel111@gmail.com

License
---

LongShot is available under the MIT license. See the [LICENSE][LICENSE] file for more info.
