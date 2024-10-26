from requests import get

from json import dumps
from pathlib import Path
from pprint import pprint
from sys import path


api_url = 'https://api.github.com'

username = ...
token = Path(...).read_text().strip()

params = {
    'headers': {
        "accept": "application/vnd.github+json",
        # "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    },
    "org": "TOP-DataScience421",
    "type": "all",
    "sort": "created",
    "direction": "asc",
}

response = get(
    url=f'{api_url}/orgs/{params["org"]}/repos',
    json=dumps(params),
    auth=(username, token)
)
repos = response.json()

for rep in repos:
    print(rep['name'])

# _scripts
# Baskov
# Danieljan
# Ermoshkina
# Evlampieva
# Kirillov
# Krjukov
# Lebedev
# Mezenov
# Tregulov
# Zotkina
# Habirov


# >>> pprint(repos[0], sort_dicts=False)
# {'id': 773983862,
#  'node_id': 'R_kgDOLiIOdg',
#  'name': '_scripts',
#  'full_name': 'TOP-DataScience421/_scripts',
#  'private': False,
#  'owner': {'login': 'TOP-DataScience421',
#            'id': 163906017,
#            'node_id': 'O_kgDOCcUB4Q',
#            'avatar_url': 'https://avatars.githubusercontent.com/u/163906017?v=4',
#            'gravatar_id': '',
#            'url': 'https://api.github.com/users/TOP-DataScience421',
#            'html_url': 'https://github.com/TOP-DataScience421',
#            'followers_url': 'https://api.github.com/users/TOP-DataScience421/followers',
#            'following_url': 'https://api.github.com/users/TOP-DataScience421/following{/other_user}',
#            'gists_url': 'https://api.github.com/users/TOP-DataScience421/gists{/gist_id}',
#            'starred_url': 'https://api.github.com/users/TOP-DataScience421/starred{/owner}{/repo}',
#            'subscriptions_url': 'https://api.github.com/users/TOP-DataScience421/subscriptions',
#            'organizations_url': 'https://api.github.com/users/TOP-DataScience421/orgs',
#            'repos_url': 'https://api.github.com/users/TOP-DataScience421/repos',
#            'events_url': 'https://api.github.com/users/TOP-DataScience421/events{/privacy}',
#            'received_events_url': 'https://api.github.com/users/TOP-DataScience421/received_events',
#            'type': 'Organization',
#            'user_view_type': 'public',
#            'site_admin': False},
#  'html_url': 'https://github.com/TOP-DataScience421/_scripts',
#  'description': 'Примеры кода из лекций',
#  'fork': False,
#  'url': 'https://api.github.com/repos/TOP-DataScience421/_scripts',
#  'forks_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/forks',
#  'keys_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/keys{/key_id}',
#  'collaborators_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/collaborators{/collaborator}',
#  'teams_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/teams',
#  'hooks_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/hooks',
#  'issue_events_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/issues/events{/number}',
#  'events_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/events',
#  'assignees_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/assignees{/user}',
#  'branches_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/branches{/branch}',
#  'tags_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/tags',
#  'blobs_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/git/blobs{/sha}',
#  'git_tags_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/git/tags{/sha}',
#  'git_refs_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/git/refs{/sha}',
#  'trees_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/git/trees{/sha}',
#  'statuses_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/statuses/{sha}',
#  'languages_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/languages',
#  'stargazers_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/stargazers',
#  'contributors_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/contributors',
#  'subscribers_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/subscribers',
#  'subscription_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/subscription',
#  'commits_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/commits{/sha}',
#  'git_commits_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/git/commits{/sha}',
#  'comments_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/comments{/number}',
#  'issue_comment_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/issues/comments{/number}',
#  'contents_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/contents/{+path}',
#  'compare_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/compare/{base}...{head}',
#  'merges_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/merges',
#  'archive_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/{archive_format}{/ref}',
#  'downloads_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/downloads',
#  'issues_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/issues{/number}',
#  'pulls_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/pulls{/number}',
#  'milestones_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/milestones{/number}',
#  'notifications_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/notifications{?since,all,participating}',
#  'labels_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/labels{/name}',
#  'releases_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/releases{/id}',
#  'deployments_url': 'https://api.github.com/repos/TOP-DataScience421/_scripts/deployments',
#  'created_at': '2024-03-18T18:32:38Z',
#  'updated_at': '2024-10-14T17:18:08Z',
#  'pushed_at': '2024-10-14T17:18:04Z',
#  'git_url': 'git://github.com/TOP-DataScience421/_scripts.git',
#  'ssh_url': 'git@github.com:TOP-DataScience421/_scripts.git',
#  'clone_url': 'https://github.com/TOP-DataScience421/_scripts.git',
#  'svn_url': 'https://github.com/TOP-DataScience421/_scripts',
#  'homepage': '',
#  'size': 1094,
#  'stargazers_count': 0,
#  'watchers_count': 0,
#  'language': 'Python',
#  'has_issues': True,
#  'has_projects': True,
#  'has_downloads': True,
#  'has_wiki': True,
#  'has_pages': False,
#  'has_discussions': False,
#  'forks_count': 0,
#  'mirror_url': None,
#  'archived': False,
#  'disabled': False,
#  'open_issues_count': 0,
#  'license': None,
#  'allow_forking': True,
#  'is_template': False,
#  'web_commit_signoff_required': False,
#  'topics': [],
#  'visibility': 'public',
#  'forks': 0,
#  'open_issues': 0,
#  'watchers': 0,
#  'default_branch': 'main',
#  'permissions': {'admin': True,
#                  'maintain': True,
#                  'push': True,
#                  'triage': True,
#                  'pull': True},
#  'security_and_analysis': {'secret_scanning': {'status': 'disabled'},
#                            'secret_scanning_push_protection': {'status': 'disabled'},
#                            'dependabot_security_updates': {'status': 'disabled'},
#                            'secret_scanning_non_provider_patterns': {'status': 'disabled'},
#                            'secret_scanning_validity_checks': {'status': 'disabled'}}}
