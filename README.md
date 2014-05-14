CKAN extension
============

CKAN extension for Datamx(ckanext-datamx-theme)

##Dependencies
- CKAN

##Installation: 
To install the plugin, enter your virtualenv and load the source:

```
$ git clone https://github.com/CodeandoMexico/ckanext-datamx_theme
cd ckanext-datamx_theme
(pyenv)$ python setup.py develop
```
This will also register a plugin entry point, so you now should be able to add the following to your CKAN .ini file:

Add datamx_theme to the .ini file.
```
ckan.plugins = datamx_theme
```
Restart Apache
```
# service restart apache2
```

## Screenshots
![DataMX](https://s3.amazonaws.com/github-static/datamxio.png)

##Using our code? We'd love to know
We want to keep track of the projects that used our extension, let us know!

##¿Questions or issues?
We keep the project's conversation in our issues page [issues](https://github.com/CodeandoMexico/ckan-kitchen/issues). If you have any other question you can reach us at <equipo@codeandomexico.org>.

##Contribute
We want this project to be the result of a community effort. You can collaborate with [code](https://github.com/CodeandoMexico/ckan-kitchen/pulls), [ideas](https://github.com/CodeandoMexico/ckanext-datamx_theme/issues) and [bugs](https://github.com/CodeandoMexico/ckanext-datamx_theme/issues)

##Core Team
This project is an initiative of [Codeando México](https://github.com/CodeandoMexico?tab=members).

The core team:
- [Braulio Chávez](https://github.com/HackerOfDreams)
- [Noé Domínguez](https://github.com/poguez)
- [Miguel Martinez](https://github.com/miguelmc)

##Licence

Crafted by [Codeando México](https://github.com/CodeandoMexico?tab=members), 2014.

Available unde the licence: GNU Affero General Public License (AGPL) v3.0. Read the document [LICENSE](/LICENSE) for more information
