1. What is the difference between git and GitLab?
Git is a distributed version control system that can be installed on a computer, allowing developers to track changes in their code collaboratively. In contrast, GitLab is an online hosting service that provides a platform for hosting Git repositories, which can be accessed securely over the internet.

2. What is the difference between GitLab, GitHub, and BitBucket?
They are all version control platforms for managing code. GitHub is primarily focused on open-source collaboration and is known for its large community, GitLab provides a more comprehensive suite for software development and deployment, while BitBucket is more focused on private repositories with deep integration into Atlassian tools.

3. Why would I ever want to use git, but not GitLab?
Using Git can be particularly beneficial for individual use due to its flexibility, simplicity, and control over version control processes. This way, one can manage their code locally, work offline, and customize workflows without being tied to a specific platform like GitLab.

4. What are the steps to update the GitLab server with some changes I made on my computer?
Firstly, stage the changes to be included in the next commit by using git add <file>. Then, commit the staged changes to the local repository with git commit -m "message". Pull to avoid conflicts, using git pull. Finally, push the changes to the server using git push. 

5. What is a branch and why would I use one?
(Hubert)

6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
(Hubert)

7. Give an example of a set of git commands that would result in a merge conflict.
(Hubert)

8. Is Git suitable for latex documents?
(Hubert)

9. Should I from now on version my word and powerpoint slides using git? Why/why not?
While it is advantageous to have version control in these documents, word documents (.doc and .docx) and powerpoint slides (.ppt .pptx) can use binary formats to store information. These file types are harder for Git to compress meaning that the repository will likely become much larger in size. As such Git is not recommended for word and powerpoint slides.   

10. What could happen when I push my latest commit to the remote repository without pulling first?
If other people have made edits in the git repository since your last commit then you could overwrite other peoples' changes and cause conflicts.

11. What happens when I pull without commiting my local changes first?
If you pull without first commiting, you could overwrite your local files, possibly erasing your local changes before they have been comitted to Git.

12. What is the difference between branching and forking?
Branches are more closely related to the original repository and exist within it whereas forks are stored in a seperate repositories. This means that only people with access to the original repository can edit a branch whereas a fork can be made into any other repository where anyone can edit it.
