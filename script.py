'''Code For The CI/CD Pipeline'''

import os
import re
from github.Repository import Repository
import requests
import base64
import github
from github import Github, GithubException, InputGitAuthor


#added this to know paste locatin
START_COMMENT = '<!--START_SECTION:cp-->'
END_COMMENT = '<!--END_SECTION:cp-->'
listReg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"


#getting tokens from user input
token = os.environ['INPUT_TOKEN']
repository = os.environ['INPUT_REPOSITORY']
copy_file_location = os.environ['INPUT_COPY-FILE-LOCATION']
paste_file_location = os.environ['INPUT_PASTE-FILE-LOCATION']



#github auth
g = Github(token)
repo = g.get_user().get_repo(repository)


#getting user info
userInfoQuery = """
{
    viewer {
      login
      email
      id
    }
  }
"""

#Functions for later use
def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def decode_readme(data: str):
    '''Decode the contents of old readme'''
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')

def generate_new_readme(stats: str, readme: str):
    '''Generate a new Readme.md'''
    stats_in_readme = f"{START_COMMENT}\n{stats}\n{END_COMMENT}"
    return re.sub(listReg, stats_in_readme, readme)


#getting commiter info
headers = {"Authorization": "Bearer " + token}
user_data = run_query(userInfoQuery)  # Execute the query
username = user_data["data"]["viewer"]["login"]
email = user_data["data"]["viewer"]["email"]
id = user_data["data"]["viewer"]["id"]
print("Username " + username)
committer = InputGitAuthor(username, email)


#getting files
file2paste = repo.get_contents(paste_file_location)
rdmd = decode_readme(file2paste.content)
file2copy = repo.get_contents(copy_file_location)
dbmd = decode_readme(file2copy.content)
new_readme = generate_new_readme(stats= dbmd, readme=rdmd)



#push commit
if new_readme != rdmd:
    try:
        repo.update_file(path=file2paste.path, message='Updated with Copy Paste Bot',
                                 content=new_readme, sha=file2paste.sha, branch='master',
                                 committer=committer)
    except:
        repo.update_file(path=file2paste.path, message='Updated with Copy Paste Bot',
                                 content=new_readme, sha=file2paste.sha, branch='main',
                                 committer=committer)


#status that updated
print("File updated")
