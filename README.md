<h1 align="center">COPY PASTE ACTION</h1>  

</p>

<p align="center">
   <img src="https://img.shields.io/badge/language-python-blue?style"/>
   <img src="https://img.shields.io/github/license/ShreyamMaity/Copy-Paste-Action"/>
   <img src="https://img.shields.io/github/stars/ShreyamMaity/Copy-Paste-Action"/>
   <img src="https://img.shields.io/github/forks/ShreyamMaity/Copy-Paste-Action"/>
   <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/>
   <img src=https://visitor-badge.glitch.me/badge?page_id=ShreyamMaity.Copy-Paste-Action"/>
</p>

----

> GitHub Action for copying one markdown file and paste it to another markdown file's specific location.  
  


- This is a [GitHub Action](https://developer.github.com/actions/) to copy one markdown file data and paste it to another markdown file's specific location.

- This action runs in a Docker container and therefore only supports Linux.

## Prep Work

1. You need to update the markdown file(.md) with 2 comments. You can refer [here](#update-your-readme) for updating it.
2. You'll need a GitHub API Token with `repo` and `user` scope from [here](https://github.com/settings/tokens) if you're running the action.
   > enabling the `repo` scope seems **DANGEROUS**<br/>
   > but this GitHub Action only accesses your repository information and use the api to update the markdown file
   - You can use [this](#usage) example to work it out
3. You need to save the GitHub API Token in the repository secrets. You can find that in the Settings of your repository. Be sure to save those as the following.Reffer [here](#secrets) for more info
    - GitHub Personal Access Token as `TOKEN=<your github access token>`

  


## Usage :

The following example [workflow step](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow) will copy the data of the markdown file from specified location inside the repository running the action, to any markdown file with specified location index(by default README.md). If the data already exist at the destination Markdown File, It will not update anything.

```yml
name: Test Workflow
on: push
jobs:
  first-job:
    runs-on: ubuntu-latest
    steps:
      - name: Run Action
        uses: ShreyamMaity/Copy-Paste-Action@main
        with:
          TOKEN: ${{ secrets.TOKEN }}
          REPOSITORY : 'Your Repository Name'
          COPY-FILE-LOCATION : './database/db.md'
          PASTE-FILE-LOCATION : './README.md'
```
  

## Update your Readme

Add a comment to your `markdown file` or `README.md` like this:

```md
<!--START_SECTION:cp-->
<!--END_SECTION:cp-->
```

These lines will be our entry-points for the copy paste action.

## Secrets

* `token`: (required) GitHub Private Access Token used for the clone/push operations. To create it follow the [GitHub Documentation](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).
  

## Options ⚙️

The following input variable options can/must be configured:

|Input variable|Necessity|Description|
|--------------------|--------|-----------|
|`TOKEN`|Required|Your Github Token|
|`REPOSITORY`|Required|Name of your repository where you are running this github action|
|`COPY-FILE-LOCATION`|Required|The Specific Location of the markdown file from where you want to copy the data.For example `./file.md` or `./folder/file.md`|
|`PASTE-FILE-LOCATION`|Required|The Specific Location of the markdown file from where you want to paste the data of copied markdown file.For example `./README.md` or `./folder/file.md`|
  
## Examples

- Open this [repository](https://github.com/shreyammaity/student-offers/)
- This repository has a database.md fie inside Database folder
- This github action copies the information from database.md file and paste it to README.md file of the Repository


## Author

The Copy Paste GitHub action is written by [Shreyam Maity](https://github.com/ShreyamMaity)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
