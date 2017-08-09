# Anemoi

**The greatest Slack chatbot ever devised by man crafted lovingly with human hands**

[![zephyrus wind engraving by Ken Mayer](docs/images/readme-anemoi.jpg)](https://en.wikipedia.org/wiki/Anemoi)

## Overview

Anemoi is a sample Slack chatbot exercise that can respond to simple weather requests.  

## Documentation

Further documentation can be found in the [docs](https://github.com/looselycoupled/anemoi/tree/master/docs) directory.  The documentation has been created with [mkdocs](http://www.mkdocs.org/) to make it easier to review and maintain project information.  To run a local webserver displaying the HTML version make sure you have the development dependencies installed and run with the following command.

    mkdocs serve --dev-addr=0.0.0.0:8080


Once the documentation server has started up, open a browser to view the documentation:

<img src="docs/images/docs-screenshot.png" alt="Drawing" style="width: 600px;"/>


## Setup

Setup is fairly standard for a Python codebase without automated installation using pip or easy_install (coming soon&trade;).  The following instructions will help you install and configure the bot for your own use.

### Download

At the moment, the only setup available is by cloning or downloading the codebase from the Github [repo](https://github.com/looselycoupled/anemoi).

    git clone git@github.com:looselycoupled/anemoi.git

## Dependencies

This codebase was developed with Python 2.7 and various libraries installed with `pip`.  To install the required dependencies use the command below:

    pip install -r requirements.txt


### Configuration

This codebase uses [confire](confire.readthedocs.org) for configuration which makes use of YAML files.  A default/template file has been provided at `conf/settings.template.yaml`.  Copy this file and then rename it using your desired environment name in place of the word `template`.  As an example, one could create a development environment copy using the bash command below.

    cp conf/settings.template.yaml conf/settings.development.yaml

Then supply the correct values as identified within the template as shown below.

    zip_code: DEFAULT_ZIPCODE_HERE

    slack:
      access_token: INSERT_TOKEN_HERE
      bot_id: INSERT_HERE

    dark_sky:
      access_token: INSERT_TOKEN_HERE

### Startup

To start the bot after creating a config file, you can use the supplied `anemoibot` executable file as shown below:

    $ ./anemoibot start
    [2017-08-08 21:32:42 -0400] INFO {anemoi.start:60} SlackBot v0.0.1 starting up with bot ID: U6A9TFYCB

### More info

The supplied CLI support standard `-h` flag during execution to provide extra help per the example below:

    $ ./anemoibot -h
    usage: anemoibot [-h] [-v] [--slack_token SLACK_TOKEN] [--bot_id BOT_ID]
                     [--darksky_token DARKSKY_TOKEN]
                     {start,list} ...

    Slack client to respond to user messages

    positional arguments:
      {start,list}                   commands
        start                        List available features of the chatbot
        list                         List available features of the chatbot

    optional arguments:
      -h, --help                     show this help message and exit
      -v, --version                  show program's version number and exit

    slack options:
      --slack_token SLACK_TOKEN      for Slack integration
      --bot_id BOT_ID                Slack ID of the bot

    dark sky options:
      --darksky_token DARKSKY_TOKEN  for DarkSky integration

See the [Setup](https://github.com/looselycoupled/anemoi/tree/master/docs/setup.md) page for more information on how to configure a production environment.

## Tests

This project includes a suite of automated tests.  For your convenience, a `Makefile` has been provided with a target for evaluating the test suite.  Use the following command to run the tests.

    $ make test


## Branches / Git Workflow

When working on Anemoi, keep in mind that the project is set up in a typical production/release/development cycle as described in _[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)_. A typical workflow is as follows:

1. Select an issue from the [issues page](https://github.com/looselycoupled/anemoi/issues) - preferably one that is "ready" then move it to "in-progress" using labels or just comment that you are working on it.

2. Create a branch off of develop called "feature-[feature name]", work and commit into that branch.

        ~$ git checkout -b feature-myfeature develop

3. Once you are done working (and everything is tested) merge your feature into develop.

        ~$ git checkout develop
        ~$ git merge --no-ff feature-myfeature
        ~$ git branch -d feature-myfeature
        ~$ git push origin develop

4. Repeat. Releases will be routinely pushed into master via release branches, then deployed to the server.

## Versioning

This codebases uses a form of [Semantic Versioning](http://semver.org/) to structure version numbers.  In general, the results of each sprint will increment the minor version while any special releases (bug fixes, etc.) will increment the patch number.

## About

In Greek mythology the [Anemoi](https://en.wikipedia.org/wiki/Anemoi) were wind gods who were each ascribed a cardinal direction from which their respective winds came.  They were also associated with various seasons and weather conditions.  The project picture is of a an engraving of Zephyrus - the west wind and bringer of light spring and early summer breezes.

### Attribution

The image used in this README, [zephyrus wind engraving by Ken Mayer](https://www.flickr.com/photos/ken_mayer/4149824777) from [Flickr](https://www.flickr.com/), is provided for reuse with some rights reserved through the [Creative Commons Attribution 2.0 Generic](https://creativecommons.org/licenses/by/2.0/) license.
