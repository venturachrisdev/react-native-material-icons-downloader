#! /usr/bin/python3
import argparse
import io
import urllib.request as request
import zipfile

# Author: Christopher Ventura <venturachrisdev@gmail.com>

SOURCE = 'https://material.io'
ENDPOINT = '/tools/icons/static/icons'
URL = '{}{}'.format(SOURCE, ENDPOINT)
PLATFORM = 'android'
EXTENSION = 'zip'
ASSET_EXTENSION = 'png'

# Android drawable dimensions from material.io zip 
android_sizes = [
  'res/drawable-mdpi/',
  'res/drawable-hdpi/',
  'res/drawable-xhdpi/',
  'res/drawable-xxhdpi/',
  'res/drawable-xxxhdpi/',
]

# React Native icons sizes
react_sizes = [
  '.',
  '@1x.',
  '@2x.',
  '@3x.',
  '@4x.',
]

# React Native assets platform
platforms = [
  'android',
  'ios',
]

default_options = {
  'theme': 'round',
  'color': 'white',
  'size': 24,
  'platform': 'none',
}

def build_asset_url(options):
  url = '{}/{}-{}'.format(
    URL,
    options['theme'],
    options['asset'],
  )
  return url

def build_platform_url(options):
  url = '{}-{}-{}.{}'.format(
    build_asset_url(options),
    PLATFORM,
    options['color'],
    EXTENSION,
  )
  return url

def build_android_filename(android_name, options):
  filename = '{}{}_{}_{}_{}.png'.format(
    android_name,
    options['theme'],
    options['asset'],
    options['color'],
    options['size'],
  )
  return filename

def build_platform_dimension(platform, dim):
  if platform == 'android' or platform == 'ios':
    return '{}{}.'.format(dim, platform)
  else:
    return dim

def build_react_filename(dim, options):
  platform_dim = build_platform_dimension(options["platform"], dim)
  filename = '{}{}{}'.format(
    options['name'],
    platform_dim,
    ASSET_EXTENSION
  )
  return filename

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-a', '--asset', help='Asset name.', required=True,
                      dest='asset')
  parser.add_argument('-n', '--name', help='Asset new name.', required=False,
                      dest='name')
  parser.add_argument('-c', '--color', help='Asset color (default: white)',
                      required=False, dest='color')
  parser.add_argument('-t', '--theme', help='Asset theme (default: round)',
                      required=False, dest='theme')
  parser.add_argument('-s', '--size', help='Asset size (default: 24)',
                      required=False, dest='size')
  parser.add_argument('-d', '--dir', help='Directory where asset will be downloaded (default: current)',
                      required=False, dest='dir')
  parser.add_argument('-p', '--platform', help='Assets platform target (default: none)',
                      required=False, dest='platform')
  args = parser.parse_args()

  options = default_options

  if args.asset:
    options['asset'] = args.asset
    # If there's no name, use asset name
    options['name'] = args.asset
    if args.theme:
      options['theme'] = args.theme
    if args.color:
      options['color'] = args.color
    if args.size:
      options['size'] = args.size
    if args.name:
      options['name'] = args.name # Override
    if args.platform:
      options['platform'] = args.platform
    file_url = build_platform_url(options)
    try:
      # Download from material.io
      response = request.urlopen(file_url)
      data = response.read()
      # Read .zip downloaded file
      zipped_file = zipfile.ZipFile(io.BytesIO(data))
      with zipped_file as folder:
        # For every file in .zip
        for file in folder.namelist():
          # android dimensions => react native size
          for size, dim in zip(android_sizes, react_sizes):
            filename = build_android_filename(size, options)
            # if this file is the same we built (we've found our file)
            if filename == file:
              # Build react equivalent name
              react_name = build_react_filename(dim, options)
              with folder.open(file) as android_icon:
                android_icon_content = android_icon.read()
                # Save as React Native icon
                with open(react_name, "wb") as react_icon:
                  react_icon.write(android_icon_content)
      # Everything went OK
      print('[*] {} icon downloaded successfully from {}'.format(options['asset'], SOURCE))
    except Exception as e:
      print(e)
      print('[!] Sorry, we couldn\'t find \'{}\' {} icon.'.format(
        options['asset'], options['theme']))
      print('[*] You can visit {} for more icon names'.format(SOURCE))
  else:
    print('[!] Asset name is required')
