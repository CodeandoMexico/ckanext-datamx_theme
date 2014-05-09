Contributing
============

For contributing we will use the CKAN guidelines see our contributing guidelines:
[http://docs.ckan.org/en/latest/contributing](http://docs.ckan.org/en/latest/contributing)


## Among them we want to highlight:
##Reporting issues
If you’ve found a bug in our CKAN extension (ckanext-datamx_theme), open a new issue on [CKANext-datamx_theme GitHub Issues](https://github.com/CodeandoMexico/ckanext-datamx_theme/issues) (try searching first to see if there’s already an issue for your bug).
If you can fix the bug yourself, please send a [pull request](https://github.com/CodeandoMexico/ckanext-datamx_theme/pulls)!


##Writing commit messages is important for us to review the code
We use the version control system git for our code and documentation, so when contributing code or docs you’ll have to commit your changes to git and write a git commit message. Generally, follow the commit guidelines from the Pro Git book:

* Try to make each commit a logically separate, digestible changeset.
* The first line of the commit message should concisely summarise the changeset.
* Optionally, follow with a blank line and then a more detailed explanation of the changeset.
* Use the imperative present tense as if you were giving commands to the codebase to change its behaviour, e.g. Add tests for..., make xyzzy do frotz..., this helps to make the commit message easy to read.

If your commit has an issue in the CKAN issue tracker put the issue number at the start of the first line of the commit message like this: [#123]. This makes our review job much easier!

####Here’s an example of a good CKAN commit message:

```
[#607] Allow reactivating deleted datasets

Currently if a dataset is deleted and users navigate to the edit form,
there is no state field and the delete button is still shown.

After this change, the state dropdown is shown if the dataset state is
not active, and the delete button is not shown.
```
