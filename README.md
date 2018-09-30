# React Native Material Icons Downloader

Download icons from [https://material.io/tools/icons](https://material.io) in React Native icons format.

### Getting started
```
usage: RNMaterialIcons.py [-h] -a ASSET [-n NAME] [-c COLOR] [-t THEME]
                          [-s SIZE] [-d DIR]

optional arguments:
  -h, --help            show this help message and exit
  -a ASSET, --asset ASSET
                        Asset name.
  -n NAME, --name NAME  Asset new name.
  -c COLOR, --color COLOR
                        Asset color (default: white)
  -t THEME, --theme THEME
                        Asset theme (default: round)
  -s SIZE, --size SIZE  Asset size (default: 24)
  -d DIR, --dir DIR     Directory where asset will be downloaded (default:
                        current)

```

### Examples

```sh
$ ./RNMaterialIcons.py -a account_cicle -c white -d /home/user/project/icon
```
```sh
$ ./RNMaterialIcons.py -a bookmarks -c black -d /home/user/project/icon -t baseline -n bookmark
```
```sh
$ ./RNMaterialIcons.py -a info -c white -s 48
```
