# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

''' 
class Championallytips(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    tip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championallytips'


class Championblurbs(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championblurbs'


class Championenemytips(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    tip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championenemytips'


class Championinfos(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    magic = models.IntegerField(blank=True, null=True)
    dificulty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championinfos'


class Championloadingimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    skinid = models.ForeignKey('Championskins', models.DO_NOTHING, db_column='skinid', blank=True, null=True)
    imageurl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championloadingimages'


class Championlores(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    lore = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championlores'


class Championnames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    championname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championnames'


class Championpassivedescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    championpassivedescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championpassivedescriptions'


class Championpassiveimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championpassiveimages'


class Championpassivenames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    championpassivename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championpassivenames'

'''
class Champions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    partype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'champions'

'''
class Championskins(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    championskinsname = models.TextField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    haschromas = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championskins'


class Championspelldescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    championspelldescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspelldescriptions'


class Championspelleffects(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey('Championspells', models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    effectindex = models.IntegerField(blank=True, null=True)
    effectburnvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspelleffects'


class Championspellimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey('Championspells', models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspellimages'


class Championspellleveltipeffects(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey('Championspells', models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    effectindex = models.IntegerField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspellleveltipeffects'


class Championspellleveltiplabels(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey('Championspells', models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    labelindex = models.IntegerField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspellleveltiplabels'


class Championspellnames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey('Championspells', models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    championspellnamesname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspellnames'


class Championspellresources(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey('Championspells', models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    resource = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspellresources'


class Championspells(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField(blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    cooldownburn = models.TextField(blank=True, null=True)
    costburn = models.TextField(blank=True, null=True)
    costtype = models.TextField(blank=True, null=True)
    maxammo = models.TextField(blank=True, null=True)
    rangeburn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspells'


class Championspelltooltips(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spellid = models.ForeignKey(Championspells, models.DO_NOTHING, db_column='spellid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    tooltip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championspelltooltips'


class Championsplashimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    skinid = models.ForeignKey(Championskins, models.DO_NOTHING, db_column='skinid', blank=True, null=True)
    imageurl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championsplashimages'


class Championsprites(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    imageurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championsprites'


class Championsquareimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    imageurl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championsquareimages'


class Championstats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    hpperlevel = models.IntegerField(blank=True, null=True)
    mp = models.IntegerField(blank=True, null=True)
    mpperlevel = models.IntegerField(blank=True, null=True)
    movespeed = models.IntegerField(blank=True, null=True)
    armor = models.IntegerField(blank=True, null=True)
    armorperlevel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spellblock = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spellblockperlevel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    attackrange = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hpregen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hpregenperlevel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mpregen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mpregenperlevel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    crit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    critperlevel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    attackdamage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    attackspeedoffset = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    attackspeedperlevel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championstats'


class Championtags(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championtags'


class Championtitles(models.Model):
    auto_id = models.AutoField(primary_key=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championtitles'


class Games(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    matchid = models.ForeignKey('Matches', models.DO_NOTHING, db_column='matchid', blank=True, null=True)
    bracketid = models.ForeignKey('Tournamentbrackets', models.DO_NOTHING, db_column='bracketid', blank=True, null=True)
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    gamesname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Gamestats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', primary_key=True)
    platformid = models.TextField(blank=True, null=True)
    gamecreation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gameduration = models.IntegerField(blank=True, null=True)
    mapid = models.ForeignKey('Maps', models.DO_NOTHING, db_column='mapid', blank=True, null=True)
    seasonid = models.IntegerField(blank=True, null=True)
    gameversion = models.TextField(blank=True, null=True)
    gamemode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestats'


class Gamestatsparticipantmasteries(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    participantid = models.ForeignKey('Gamestatsparticipants', models.DO_NOTHING, db_column='participantid', blank=True, null=True)
    masteryid = models.ForeignKey('Masteries', models.DO_NOTHING, db_column='masteryid', blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestatsparticipantmasteries'


class Gamestatsparticipantrunes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    participantid = models.ForeignKey('Gamestatsparticipants', models.DO_NOTHING, db_column='participantid', blank=True, null=True)
    runeid = models.ForeignKey('Masteries', models.DO_NOTHING, db_column='runeid', blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestatsparticipantrunes'


class Gamestatsparticipants(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    participantid = models.IntegerField(blank=True, null=True)
    summonername = models.TextField(blank=True, null=True)
    profileicon = models.IntegerField(blank=True, null=True)
    teamid = models.IntegerField(blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    spell1id = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='spell1id', blank=True, null=True)
    spell2id = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='spell2id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestatsparticipants'


class Gamestatsparticipantstats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    participantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='participantid', blank=True, null=True)
    win = models.BooleanField(blank=True, null=True)
    item0 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item0', blank=True, null=True)
    item1 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item1', blank=True, null=True)
    item2 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item2', blank=True, null=True)
    item3 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item3', blank=True, null=True)
    item4 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item4', blank=True, null=True)
    item5 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item5', blank=True, null=True)
    item6 = models.ForeignKey('Items', models.DO_NOTHING, db_column='item6', blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    largestkillingspree = models.IntegerField(blank=True, null=True)
    largestmultikill = models.IntegerField(blank=True, null=True)
    killingspree = models.IntegerField(blank=True, null=True)
    longesttimespentliving = models.IntegerField(blank=True, null=True)
    doublekills = models.IntegerField(blank=True, null=True)
    triplekills = models.IntegerField(blank=True, null=True)
    quadrakills = models.IntegerField(blank=True, null=True)
    pentakills = models.IntegerField(blank=True, null=True)
    unrealkills = models.IntegerField(blank=True, null=True)
    totaldamagedealt = models.IntegerField(blank=True, null=True)
    magicdamagedealt = models.IntegerField(blank=True, null=True)
    physicaldamagedealt = models.IntegerField(blank=True, null=True)
    rutedamagedealt = models.IntegerField(blank=True, null=True)
    largestcriticalstrike = models.IntegerField(blank=True, null=True)
    totaldamagedealttochampions = models.IntegerField(blank=True, null=True)
    magicdamagedealttochampions = models.IntegerField(blank=True, null=True)
    physicaldamagedealttochampions = models.IntegerField(blank=True, null=True)
    truedamagedealttochampions = models.IntegerField(blank=True, null=True)
    totalheal = models.IntegerField(blank=True, null=True)
    totalunitshealed = models.IntegerField(blank=True, null=True)
    damageselfmitigated = models.IntegerField(blank=True, null=True)
    damagedealttoobjectives = models.IntegerField(blank=True, null=True)
    damagedealttoturrets = models.IntegerField(blank=True, null=True)
    visionscore = models.IntegerField(blank=True, null=True)
    timeccingothers = models.IntegerField(blank=True, null=True)
    totaldamagetaken = models.IntegerField(blank=True, null=True)
    magicaldamagetaken = models.IntegerField(blank=True, null=True)
    physicaldamagetaken = models.IntegerField(blank=True, null=True)
    truedamagetaken = models.IntegerField(blank=True, null=True)
    goldearned = models.IntegerField(blank=True, null=True)
    goldspent = models.IntegerField(blank=True, null=True)
    turretkills = models.IntegerField(blank=True, null=True)
    inhibitorkills = models.IntegerField(blank=True, null=True)
    totalminionskilled = models.IntegerField(blank=True, null=True)
    neutralminionskilled = models.IntegerField(blank=True, null=True)
    neutralminionskilledteamjungle = models.IntegerField(blank=True, null=True)
    neutralminionskilledenemyjungle = models.IntegerField(blank=True, null=True)
    totaltimecrowdcontroldealt = models.IntegerField(blank=True, null=True)
    champlevel = models.IntegerField(blank=True, null=True)
    visionwardsboughtingame = models.IntegerField(blank=True, null=True)
    sightwardsboughtingame = models.IntegerField(blank=True, null=True)
    wardsplaced = models.IntegerField(blank=True, null=True)
    wardskilled = models.IntegerField(blank=True, null=True)
    firstbloodkill = models.BooleanField(blank=True, null=True)
    firstbloodassist = models.BooleanField(blank=True, null=True)
    firsttowerkill = models.BooleanField(blank=True, null=True)
    firsttowerassist = models.BooleanField(blank=True, null=True)
    firstinhibitorkill = models.BooleanField(blank=True, null=True)
    firstinhibitorassist = models.BooleanField(blank=True, null=True)
    combatplayerscore = models.IntegerField(blank=True, null=True)
    objectiveplayerscore = models.IntegerField(blank=True, null=True)
    totalplayerscore = models.IntegerField(blank=True, null=True)
    totalscorerank = models.IntegerField(blank=True, null=True)
    playerscore0 = models.IntegerField(blank=True, null=True)
    playerscore1 = models.IntegerField(blank=True, null=True)
    playerscore2 = models.IntegerField(blank=True, null=True)
    playerscore3 = models.IntegerField(blank=True, null=True)
    playerscore4 = models.IntegerField(blank=True, null=True)
    playerscore5 = models.IntegerField(blank=True, null=True)
    playerscore6 = models.IntegerField(blank=True, null=True)
    playerscore7 = models.IntegerField(blank=True, null=True)
    playerscore8 = models.IntegerField(blank=True, null=True)
    playerscore9 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestatsparticipantstats'


class Gamestatteambans(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    teamid = models.ForeignKey('Gamestatteams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    pickturn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestatteambans'


class Gamestatteams(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    teamid = models.IntegerField(blank=True, null=True)
    win = models.BooleanField(blank=True, null=True)
    firstblood = models.BooleanField(blank=True, null=True)
    firsttower = models.BooleanField(blank=True, null=True)
    firstinhibitor = models.BooleanField(blank=True, null=True)
    firstbaron = models.BooleanField(blank=True, null=True)
    firstdragon = models.BooleanField(blank=True, null=True)
    firstriftherald = models.BooleanField(blank=True, null=True)
    towerkills = models.IntegerField(blank=True, null=True)
    inhibitorkills = models.IntegerField(blank=True, null=True)
    baronkils = models.IntegerField(blank=True, null=True)
    dragonkills = models.IntegerField(blank=True, null=True)
    vilemawkills = models.IntegerField(blank=True, null=True)
    riftheraldkills = models.IntegerField(blank=True, null=True)
    dominionvictoryscore = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestatteams'


class Gametimelineframeeventbuildingkill(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    xposition = models.IntegerField(blank=True, null=True)
    yposition = models.IntegerField(blank=True, null=True)
    killerid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='killerid', blank=True, null=True)
    teamid = models.IntegerField(blank=True, null=True)
    buildingtype = models.TextField(blank=True, null=True)
    lanetype = models.TextField(blank=True, null=True)
    towertype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventbuildingkill'


class Gametimelineframeeventbuildingkillassists(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    buildingkillevent = models.ForeignKey(Gametimelineframeeventbuildingkill, models.DO_NOTHING, db_column='buildingkillevent', blank=True, null=True)
    assistingparticipantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='assistingparticipantid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventbuildingkillassists'


class Gametimelineframeeventchampionkill(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    xposition = models.IntegerField(blank=True, null=True)
    yposition = models.IntegerField(blank=True, null=True)
    killerid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='killerid', blank=True, null=True)
    victimid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='victimid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventchampionkill'


class Gametimelineframeeventchampionkillassists(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    championkillevent = models.ForeignKey(Gametimelineframeeventchampionkill, models.DO_NOTHING, db_column='championkillevent', blank=True, null=True)
    assistingparticipantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='assistingparticipantid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventchampionkillassists'


class Gametimelineframeeventelitemonsterkill(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    xposition = models.IntegerField(blank=True, null=True)
    yposition = models.IntegerField(blank=True, null=True)
    killerid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='killerid', blank=True, null=True)
    monstertype = models.ForeignKey('Gametimelineframeeventelitemonstertypes', models.DO_NOTHING, db_column='monstertype', blank=True, null=True)
    monstersubtype = models.ForeignKey('Gametimelineframeeventelitemonstersubtypes', models.DO_NOTHING, db_column='monstersubtype', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventelitemonsterkill'


class Gametimelineframeeventelitemonsterkillassists(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    elitemonsterkillevent = models.ForeignKey(Gametimelineframeeventelitemonsterkill, models.DO_NOTHING, db_column='elitemonsterkillevent', blank=True, null=True)
    assistingparticipantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='assistingparticipantid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventelitemonsterkillassists'


class Gametimelineframeeventelitemonstersubtypes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    monstersubtype = models.TextField()

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventelitemonstersubtypes'


class Gametimelineframeeventelitemonstertypes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    monstertype = models.TextField()

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventelitemonstertypes'


class Gametimelineframeeventitemdestroyed(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    participantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='participantid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventitemdestroyed'


class Gametimelineframeeventitempurchased(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    participantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='participantid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventitempurchased'


class Gametimelineframeeventitemsold(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    participantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='participantid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventitemsold'


class Gametimelineframeevents(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.ForeignKey('Gametimelineframeeventtypes', models.DO_NOTHING, db_column='type', blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'gametimelineframeevents'


class Gametimelineframeeventskilllevelup(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    skillslot = models.IntegerField(blank=True, null=True)
    participantid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='participantid', blank=True, null=True)
    leveluptype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventskilllevelup'


class Gametimelineframeeventtypes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventtypes'


class Gametimelineframeeventwardkill(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    wardtype = models.ForeignKey('Gametimelineframeeventwardtypes', models.DO_NOTHING, db_column='wardtype', blank=True, null=True)
    killerid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='killerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventwardkill'


class Gametimelineframeeventwardplaced(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.
    wardtype = models.ForeignKey('Gametimelineframeeventwardtypes', models.DO_NOTHING, db_column='wardtype', blank=True, null=True)
    creatorid = models.ForeignKey(Gamestatsparticipants, models.DO_NOTHING, db_column='creatorid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventwardplaced'


class Gametimelineframeeventwardtypes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    wardtype = models.TextField()

    class Meta:
        managed = False
        db_table = 'gametimelineframeeventwardtypes'


class Gametimelineframeparticipantframes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    participantid = models.IntegerField(blank=True, null=True)
    xposition = models.IntegerField(blank=True, null=True)
    yposition = models.IntegerField(blank=True, null=True)
    currentgold = models.IntegerField(blank=True, null=True)
    totalgold = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    xp = models.IntegerField(blank=True, null=True)
    minionskilled = models.IntegerField(blank=True, null=True)
    jungleminionskilled = models.IntegerField(blank=True, null=True)
    dominionscore = models.IntegerField(blank=True, null=True)
    teamscore = models.IntegerField(blank=True, null=True)
    field_timestamp = models.IntegerField(db_column='_timestamp', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'gametimelineframeparticipantframes'


class Gametimelines(models.Model):
    auto_id = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', primary_key=True)
    frameinterval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametimelines'

'''
class Itembuildintos(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True,related_name='i_itemid')
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    intoitemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='intoitemid', blank=True, null=True, related_name='intoitemid')

    class Meta:
        managed = False
        db_table = 'itembuildintos'


class Itembuiltfroms(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True,related_name='f_itemid')
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fromitemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='fromitemid', blank=True, null=True,related_name='fromitemid')

    class Meta:
        managed = False
        db_table = 'itembuiltfroms'


class Itemdescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    itemdescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemdescriptions'


class Itemeffects(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    effectindex = models.IntegerField(blank=True, null=True)
    effectvalue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemeffects'


class Itemimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemimages'


class Itemmaps(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    mapid = models.ForeignKey('Maps', models.DO_NOTHING, db_column='mapid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemmaps'


class Itemnames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    itemname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemnames'


class Itemplaintexts(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey('Languagecodes', models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    plaintext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemplaintexts'


class Items(models.Model):
    auto_id = models.AutoField(primary_key=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    requiredchampion = models.ForeignKey(Champions, models.DO_NOTHING, db_column='requiredchampion', blank=True, null=True)
    instore = models.BooleanField(blank=True, null=True)
    basegold = models.IntegerField(blank=True, null=True)
    purchasable = models.BooleanField(blank=True, null=True)
    totalgold = models.IntegerField(blank=True, null=True)
    sellgold = models.IntegerField(blank=True, null=True)
    hidefromall = models.BooleanField(blank=True, null=True)
    specialrecipie = models.ForeignKey('self', models.DO_NOTHING, db_column='specialrecipie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Itemstats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    stat = models.ForeignKey('Languageitems', models.DO_NOTHING, db_column='stat', blank=True, null=True)
    statvalue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemstats'


class Itemtags(models.Model):
    auto_id = models.AutoField(primary_key=True)
    itemid = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemtags'

 
class Languagecodes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    languagecode = models.TextField()
    languagetext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languagecodes'


class Languageitems(models.Model):
    auto_id = models.AutoField(primary_key=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languageitem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languageitems'
'''

class Languages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    languagecode = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Leagueabouts(models.Model):
    auto_id = models.AutoField(primary_key=True)
    leagueid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='leagueid', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagueabouts'


class Leaguenames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    leagueid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='leagueid', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    leaguenamesname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaguenames'


class Leagues(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    gid = models.TextField(blank=True, null=True)
    leaguename = models.TextField(blank=True, null=True)
    logourl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagues'


class Leaguetournamentrecords(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    bracketid = models.ForeignKey('Tournamentbrackets', models.DO_NOTHING, db_column='bracketid', blank=True, null=True)
    roster = models.ForeignKey('Tournamentrosters', models.DO_NOTHING, db_column='roster', blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaguetournamentrecords'

'''
class Maps(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    mapsname = models.TextField(blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maps'


class Mapunpurchasableitems(models.Model):
    auto_id = models.AutoField(primary_key=True)
    mapid = models.ForeignKey(Maps, models.DO_NOTHING, db_column='mapid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    itemid = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapunpurchasableitems'

'''
class Masteries(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    ranks = models.IntegerField(blank=True, null=True)
    prereq = models.ForeignKey('self', models.DO_NOTHING, db_column='prereq', blank=True, null=True)
    branchname = models.TextField(blank=True, null=True)
    columnindex = models.IntegerField(blank=True, null=True)
    rowindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masteries'


class Masterydescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    masteryid = models.ForeignKey(Masteries, models.DO_NOTHING, db_column='masteryid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    masterydescription = models.TextField(blank=True, null=True)
    descriptionindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterydescriptions'


class Masteryimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    masteryid = models.ForeignKey(Masteries, models.DO_NOTHING, db_column='masteryid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masteryimages'


class Masterynames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    masteryid = models.ForeignKey(Masteries, models.DO_NOTHING, db_column='masteryid', blank=True, null=True)
    patch = models.ForeignKey('Patches', models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    masteryname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterynames'


class Matches(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    bracketid = models.ForeignKey('Tournamentbrackets', models.DO_NOTHING, db_column='bracketid', blank=True, null=True)
    matchesname = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matches'

'''
class Patches(models.Model):
    auto_id = models.AutoField(primary_key=True)
    patch = models.TextField()

    class Meta:
        managed = False
        db_table = 'patches'

'''
class Playerbios(models.Model):
    auto_id = models.AutoField(primary_key=True)
    playerid = models.ForeignKey('Players', models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerbios'


class Players(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    ingamename = models.TextField(blank=True, null=True)
    photourl = models.TextField(blank=True, null=True)
    hometown = models.TextField(blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'


class Playersocialnetworks(models.Model):
    auto_id = models.AutoField(primary_key=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    networkname = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playersocialnetworks'


class Playerstatshistories(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    field_timestamp = models.DecimalField(db_column='_timestamp', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it started with '_'.
    assists = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    cspertenminutes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kdaratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    killparticipation = models.IntegerField(blank=True, null=True)
    win = models.BooleanField(blank=True, null=True)
    matchid = models.ForeignKey(Matches, models.DO_NOTHING, db_column='matchid', blank=True, null=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    opponentteamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='opponentteamid', blank=True, null=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerstatshistories'


class Playerstatssummaries(models.Model):
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    kdsratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kdaratiorank = models.IntegerField(blank=True, null=True)
    cspertenminutes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cspertenminutesrank = models.IntegerField(blank=True, null=True)
    killparticipation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    killparticipationrank = models.IntegerField(blank=True, null=True)
    mostplayedchampionsid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerstatssummaries'


class Playerstatssummariesmostplayedchampions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    playerstatssummaryid = models.ForeignKey(Playerstatssummaries, models.DO_NOTHING, db_column='playerstatssummaryid', blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    kdaratiorank = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerstatssummariesmostplayedchampions'


class Playertournamentstats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    playertournamentstatsname = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    teamacronym = models.TextField(blank=True, null=True)
    gamesplayed = models.IntegerField(blank=True, null=True)
    kda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    killparticipation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cspermin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)
    minutesplayed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playertournamentstats'


class Profileicons(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profileicons'


class Runedescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runeid = models.ForeignKey('Runes', models.DO_NOTHING, db_column='runeid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    runedescriptionsname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runedescriptions'


class Runeimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runeid = models.ForeignKey('Runes', models.DO_NOTHING, db_column='runeid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runeimages'


class Runenames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runeid = models.ForeignKey('Runes', models.DO_NOTHING, db_column='runeid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    runename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runenames'


class Runes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    tier = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    colloq = models.TextField(blank=True, null=True)
    plaintext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runes'


class Runesreforged(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    iconurl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runesreforged'


class Runesreforgedname(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runesreforgedid = models.ForeignKey(Runesreforged, models.DO_NOTHING, db_column='runesreforgedid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    runesreforgedname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runesreforgedname'


class Runesreforgedrunelongdescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runesreforgedruneid = models.ForeignKey('Runesreforgedrunes', models.DO_NOTHING, db_column='runesreforgedruneid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runesreforgedrunelongdescriptions'


class Runesreforgedrunenames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runesreforgedruneid = models.ForeignKey('Runesreforgedrunes', models.DO_NOTHING, db_column='runesreforgedruneid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    runesreforgedrunename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runesreforgedrunenames'


class Runesreforgedrunes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    runesreforgedid = models.ForeignKey(Runesreforged, models.DO_NOTHING, db_column='runesreforgedid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    slotindex = models.IntegerField(blank=True, null=True)
    iconurl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runesreforgedrunes'


class Runesreforgedruneshortdescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runesreforgedruneid = models.ForeignKey(Runesreforgedrunes, models.DO_NOTHING, db_column='runesreforgedruneid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    shortdescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runesreforgedruneshortdescriptions'


class Runestats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runeid = models.ForeignKey(Runes, models.DO_NOTHING, db_column='runeid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    stat = models.ForeignKey(Languageitems, models.DO_NOTHING, db_column='stat', blank=True, null=True)
    statvalue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runestats'


class Runetags(models.Model):
    auto_id = models.AutoField(primary_key=True)
    runeid = models.ForeignKey(Runes, models.DO_NOTHING, db_column='runeid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runetags'


class Stickers(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stickers'


class Summonerspelldescriptions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    summonerid = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='summonerid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    summonerspelldescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerspelldescriptions'


class Summonerspellimages(models.Model):
    auto_id = models.AutoField(primary_key=True)
    summonerid = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='summonerid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    fullurl = models.TextField(blank=True, null=True)
    spriteurl = models.TextField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerspellimages'


class Summonerspellmodes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    summonerid = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='summonerid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    mode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerspellmodes'


class Summonerspellnames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    summonerid = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='summonerid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    summonerspellname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerspellnames'


class Summonerspells(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField(blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    maxrank = models.IntegerField(blank=True, null=True)
    cooldownburn = models.TextField(blank=True, null=True)
    costburn = models.TextField(blank=True, null=True)
    summonerlevel = models.IntegerField(blank=True, null=True)
    costtype = models.TextField(blank=True, null=True)
    maxammo = models.IntegerField(blank=True, null=True)
    rangeburn = models.TextField(blank=True, null=True)
    resource = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerspells'


class Summonerspelltooltips(models.Model):
    auto_id = models.AutoField(primary_key=True)
    summonerid = models.ForeignKey(Summonerspells, models.DO_NOTHING, db_column='summonerid', blank=True, null=True)
    patch = models.ForeignKey(Patches, models.DO_NOTHING, db_column='patch', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    tooltip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerspelltooltips'


class Teambios(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    languagecode = models.ForeignKey(Languagecodes, models.DO_NOTHING, db_column='languagecode', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teambios'


class Teamplayers(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamplayers'


class Teamrosterstats(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    gamesplayed = models.IntegerField(blank=True, null=True)
    averageassists = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    averagedeaths = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    averagekills = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    averagekillparticipation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summonername = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamrosterstats'


class Teamrosterstatschampions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamrosterstatschampions'


class Teams(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    teamname = models.TextField(blank=True, null=True)
    photourl = models.TextField(blank=True, null=True)
    logourl = models.TextField(blank=True, null=True)
    acronym = models.TextField(blank=True, null=True)
    altlogourl = models.TextField(blank=True, null=True)
    homeleague = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='homeleague', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class Teamstarters(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamstarters'


class Teamstatshistories(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    field_timestamp = models.DecimalField(db_column='_timestamp', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it started with '_'.
    assists = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    win = models.BooleanField(blank=True, null=True)
    matchid = models.ForeignKey(Matches, models.DO_NOTHING, db_column='matchid', blank=True, null=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    opponentteamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='opponentteamid', blank=True, null=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamstatshistories'


class Teamstatshistorieschampions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamstatshistoriesid = models.ForeignKey(Teamstatshistories, models.DO_NOTHING, db_column='teamstatshistoriesid', blank=True, null=True)
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamstatshistorieschampions'


class Teamstatssummaries(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    kdsratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kdaratiorank = models.IntegerField(blank=True, null=True)
    averagewinlength = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    averagewinlengthrank = models.IntegerField(blank=True, null=True)
    firstdragonkillratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    firstdragonkillratiorank = models.IntegerField(blank=True, null=True)
    firsttowerratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    firsttowerratiorank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamstatssummaries'


class Teamstatssummariesaveragedamagebypositions(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    adc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    support = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    solo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jungle = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamstatssummariesaveragedamagebypositions'


class Teamsubs(models.Model):
    auto_id = models.AutoField(primary_key=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='playerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamsubs'


class Tournamentbracketmatchtypes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    bracketid = models.ForeignKey('Tournamentbrackets', models.DO_NOTHING, db_column='bracketid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    bestof = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentbracketmatchtypes'


class Tournamentbracketrosters(models.Model):
    auto_id = models.AutoField(primary_key=True)
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    bracketid = models.ForeignKey('Tournamentbrackets', models.DO_NOTHING, db_column='bracketid', blank=True, null=True)
    roster = models.ForeignKey('Tournamentrosters', models.DO_NOTHING, db_column='roster', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentbracketrosters'


class Tournamentbrackets(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    tournamentbracketsname = models.TextField(blank=True, null=True)
    groupposition = models.IntegerField(blank=True, null=True)
    groupname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentbrackets'


class Tournamentbrackettypes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    bracketid = models.ForeignKey(Tournamentbrackets, models.DO_NOTHING, db_column='bracketid', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    rounds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentbrackettypes'


class Tournamentrosters(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    turnamentrostersname = models.TextField(blank=True, null=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    tournamentid = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentrosters'


class Tournaments(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    title = models.TextField(blank=True, null=True)
    tournamentdescription = models.TextField(blank=True, null=True)
    leagueid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='leagueid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournaments'


class Tournamentteams(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.TextField()
    tournamentteamsname = models.TextField(blank=True, null=True)
    teamid = models.ForeignKey(Teams, models.DO_NOTHING, db_column='teamid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentteams'


class Videos(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    tournamentid = models.ForeignKey(Tournaments, models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='gameid', blank=True, null=True)
    matchid = models.ForeignKey(Matches, models.DO_NOTHING, db_column='matchid', blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos'
'''