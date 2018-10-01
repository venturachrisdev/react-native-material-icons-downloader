# React Native Material Icons Downloader

Download icons from [https://material.io](https://material.io/tools/icons) in React Native icons format.

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
  -p PLATFORM, --platform PLATFORM
                        Assets platform target (default: none)

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

You can download the same icon and different size for each platform:

```sh
$ ./RNMaterialIcons.py -a check -p android -s 24
```
```sh
$ ./RNMaterialIcons.py -a check -p ios -s 48
```

This will generate
```
check.android.png (24dp)
check.ios.png (48dp)
check@1x.android.png (24dp)
check@1x.ios.png (48dp)
check@2x.android.png (24dp)
check@2x.ios.png (48dp)
check@3x.android.png (24dp)
check@3x.ios.png (48dp)
check@4x.android.png (24dp)
check@4x.ios.png (48dp)
```
