import wx
import gui
import config
import addonHandler
from transFromNVDA import transFromNVDA

addonHandler.initTranslation()


class SettingsPanel(gui.SettingsPanel):
    # Translators: The name of the settings category.
    title = _("Profile switcher")
    
    def makeSettings(self, sizer):
        boxSizer = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
        profilesList = [profile for profile in config.conf.listProfiles()]
        profilesList.insert(0, transFromNVDA('(normal configuration)'))
        self.firstProfile = boxSizer.addLabeledControl(
            # Translators: The label of the first profile selection widget.
            _("&First profile to switch to:"),
            wx.Choice, choices=profilesList
        )
        self.secondProfile = boxSizer.addLabeledControl(
            # Translators: The label of the secondary profile selection widget.
            _("&Second profile to switch to:"),
            wx.Choice, choices=profilesList
        )
        self.playSound = boxSizer.addItem(wx.CheckBox(
            self,
            id=-1,
            # Translators: The checkBox label of turning sound playing on alerts on or off.
            label=_('&Play sound on alerts.'))
        )
        self.playSound.SetValue(config.conf['profilesSwitcher']['shouldPlaySound'])
        firstChoice = self.firstProfile.FindString(config.conf['profilesSwitcher']['firstProfile'])
        secondChoice = self.secondProfile.FindString(config.conf['profilesSwitcher']['secondProfile'])
        self.firstProfile.SetSelection(firstChoice if firstChoice != wx.NOT_FOUND else 0)
        self.secondProfile.SetSelection(secondChoice if secondChoice != wx.NOT_FOUND else 0)

    def onSave(self):
        firstChoice = self.firstProfile.GetSelection()
        secondChoice = self.secondProfile.GetSelection()
        config.conf['profilesSwitcher']['firstProfile'] = self.firstProfile.GetString(firstChoice) if firstChoice else ''
        config.conf['profilesSwitcher']['secondProfile'] = self.secondProfile.GetString(secondChoice) if secondChoice else ''
        config.conf['profilesSwitcher']['shouldPlaySound'] = self.playSound.GetValue()

