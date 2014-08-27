import plugin_test
import plugins.usernames
from plugin_test import *


class UsernamesTest(plugin_test.PluginTest):

    def setUp(self):
        plugin_test.PluginTest.setUp(self, plugins.usernames)

    def test_add_username(self):
        nick('Art').says('.username steam')
        self.shouldSay("Art: Your username for steam isn't registered")

        nick('Art').says('.username steam art')
        self.shouldSay('Art: Noted: You use steam as "art"')

        nick('Art').says('.username steam')
        self.shouldSay('Art: Your steam username is "art"')

    def test_multiple_games(self):
        nick('Art').says('.games')
        self.shouldSay('Art: You don\'t have any games registered.')

        nick('Art').says('.username steam art1')
        self.shouldSay('Art: Noted: You use steam as "art1"')
        nick('Art').says('.username 3DS art2')
        self.shouldSay('Art: Noted: You use 3ds as "art2"')
        nick('Art').says('.username WiiU art3')
        self.shouldSay('Art: Noted: You use wiiu as "art3"')

        nick('Art').says('.games')
        self.shouldSay('Art: 3ds: art2 | steam: art1 | wiiu: art3')

        nick('Bob').says('.games art')
        self.shouldSay('Bob: art -> 3ds: art2 | steam: art1 | wiiu: art3')

    def test_lookup_users(self):
        nick('Dan').says('.usernames steam')
        self.shouldSay('Dan: Nobody seems to be playing that.')

        nick('Art').says('.username steam art')
        self.shouldSay('Art: Noted: You use steam as "art"')
        nick('Bob').says('.username steam bob')
        self.shouldSay('Bob: Noted: You use steam as "bob"')
        nick('Cat').says('.username steam cat')
        self.shouldSay('Cat: Noted: You use steam as "cat"')

        nick('Dan').says('.usernames steam')
        self.shouldSay('Dan: steam -> art: art | bob: bob | cat: cat')