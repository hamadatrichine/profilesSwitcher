# profileSwitcher: Switch back and forth between two profiles from your choice.
# Copyright (c) 2019 Hamada Trichine.

import wx
import gui
import config
import addonHandler
from os.path import basename, splitext
from globalPluginHandler import GlobalPlugin
from globalCommands import SCRCAT_CONFIG
from ui import message
from tones import beep
from settingsPanel import SettingsPanel

addonHandler.initTranslation()
# config template.
confspec = {
    'firstProfile':'string(default="")',
    'secondProfile':'string(default="")',
    'active':'integer(default=0)'
}
config.conf.spec['profilesSwitcher'] = confspec


class GlobalPlugin(GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(SettingsPanel)

    def activateProfile(self, profileName):
        try:
            profileToActivate = config.conf['profilesSwitcher'][profileName]
            config.conf.manualActivateProfile(profileToActivate)
            if profileToActivate:
                message(
                    # Translators: A message spoken when a selected profile is activated.
                    _('The {profile} profile is now active.'.format(profile=profileToActivate))
                )
                return True
            else:
                message(
                    # Translators: A message spoken when you switch to the normal configuration.
                    _('Using the normal configuration.')
                )
                return True
        except IOError as e:
            notFoundFileName = basename(e.message.split(': "')[1][:-2])
            message(
                # Translators: An error message spoken when a configuration profile is not found.
                _('Error, the {profile} profile does not exist.').format(profile=splitext(notFoundFileName)[0])
            )
            beep(75, 200)
            return False

    def script_switchProfile(self, gesture):
        if config.conf['profilesSwitcher']['active']:
            if self.activateProfile('firstProfile'):
                config.conf['profilesSwitcher']['active'] = 0
                beep(250, 50)
        else:
            if self.activateProfile('secondProfile'):
                config.conf['profilesSwitcher']['active'] = 1
                beep(250, 50)

    # Translators: The doc string for the switchProfile script.
    script_switchProfile.__doc__ = _('Switch back and forth between two configuration profiles.')
    script_switchProfile.category = SCRCAT_CONFIG

    def terminate(self):
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(SettingsPanel)

    __gestures = {'KB:NVDA+SHIFT+P':'switchProfile'}
