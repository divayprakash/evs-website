# IMPORTANT

Please follow the guide [here][1] to contribute to the website code. The steps
to follow in this tutorial are outlined in [section 1][2] below.

After completing your work, your fork of the repository will be out of date in
case your pull request is merged ino the main project. If so, you will need to
rebase your repo and clean up history. Skip to [section 2][3] for a tutorial on
the same.

## Section 1

Steps to follow :

- Fork the project & clone locally
- Create an upstream remote and sync your local copy before you branch.
- Create branch for each separate piece of work
  - If fixing bug, name the branch as `bugname_fix`
  - If adding feature, name the branch as `featurename_feature`
  - If working on enhancement, name the branch as `enhancementname_enhancement`
- Work!
- Commit your chages to this branch
  - Write good COMMIT message
  - If fixing an issue, uses `closes #issue_number` or `fixes #issue_number` at
  the end of your commit message to automatically close issue
- Push your branch to the origin remote
- Create pull request on GitHub
- Respond to any code review feedback

## Section 2

Follow the guide [here][4] from the subhead labelled **Cleaning your history
(optional)** (btw, this isn't optional :wink:).

Additionally, always remember:
>Always code as if the guy who ends up maintaining your code will be a violent
psychopath who knows where you live.

[1]:https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/
[2]:https://github.com/divayprakash/evs-website/blob/master/CONTRIBUTING.md#section-1
[3]:https://github.com/divayprakash/evs-website/blob/master/CONTRIBUTING.md#section-2
[4]:http://codeinthehole.com/writing/pull-requests-and-other-good-practices-for-teams-using-github/
