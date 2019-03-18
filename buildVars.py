# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "profilesSwitcher",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Profiles Switcher"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""Profiles switcher is an addon that allows you to switch back and forth between two configuration profiles from your choice."""),
	# version
	"addon_version" : "1.0",
	# Author(s)
	"addon_author" : u"Hamada Trichine <hamadalog25@gmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/hamadatrichine/profilesSwitcher",
	# Documentation file name
	"addon_docFileName" : "readme.html",
    "addon_nvdaMinimumVersion" : "2018.3",
    "addon_lastTestedNvdaVersion" : "2018.4.1",
    "addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["addon\globalPlugins\chatClient\__init__.py","addon\globalPlugins\chatClient\clientGui.py","addon\globalPlugins\chatClient\clientNetwork.py","addon\globalPlugins\chatClient\chatBox.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
