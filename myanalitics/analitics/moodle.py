from django.db import models

# Copia aquí los modelos generados en moodle_models.py
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mdlm9Chat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    keepdays = models.BigIntegerField()
    studentlogs = models.SmallIntegerField()
    chattime = models.BigIntegerField()
    schedule = models.SmallIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_chat'
        db_table_comment = 'Each of these is a chat room'


class Mdlm9ChatMessages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    issystem = models.IntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_chat_messages'
        db_table_comment = 'Stores all the actual chat messages'


class Mdlm9Course(models.Model):
    id = models.BigIntegerField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.IntegerField()
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    enddate = models.BigIntegerField()
    relativedatesmode = models.IntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.SmallIntegerField()
    showreports = models.SmallIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    downloadcontent = models.IntegerField(blank=True, null=True)
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.IntegerField()
    enablecompletion = models.IntegerField()
    completionnotify = models.IntegerField()
    cacherev = models.BigIntegerField()
    originalcourseid = models.BigIntegerField(blank=True, null=True)
    showactivitydates = models.IntegerField()
    showcompletionconditions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdlm9_course'
        db_table_comment = 'Central course table'


class Mdlm9CourseCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    coursecount = models.BigIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    timemodified = models.BigIntegerField()
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255)
    theme = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdlm9_course_categories'
        db_table_comment = 'Course categories'


class Mdlm9CourseModules(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    module = models.BigIntegerField()
    instance = models.BigIntegerField()
    section = models.BigIntegerField()
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    added = models.BigIntegerField()
    score = models.SmallIntegerField()
    indent = models.IntegerField()
    visible = models.IntegerField()
    visibleoncoursepage = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.SmallIntegerField()
    groupingid = models.BigIntegerField()
    completion = models.IntegerField()
    completiongradeitemnumber = models.BigIntegerField(blank=True, null=True)
    completionview = models.IntegerField()
    completionexpected = models.BigIntegerField()
    showdescription = models.IntegerField()
    availability = models.TextField(blank=True, null=True)
    deletioninprogress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_course_modules'
        db_table_comment = 'course_modules table retrofitted from MySQL'


class Mdlm9CourseModulesCompletion(models.Model):
    id = models.IntegerField(primary_key=True)
    coursemoduleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    completionstate = models.IntegerField()
    viewed = models.IntegerField(blank=True, null=True)
    overrideby = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_course_modules_completion'
        db_table_comment = 'Stores the completion state (completed or not completed, etc'


class Mdlm9Enrol(models.Model):
    id = models.IntegerField(primary_key=True)
    enrol = models.CharField(max_length=20)
    status = models.BigIntegerField()
    courseid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    enrolstartdate = models.BigIntegerField(blank=True, null=True)
    enrolenddate = models.BigIntegerField(blank=True, null=True)
    expirynotify = models.IntegerField(blank=True, null=True)
    expirythreshold = models.BigIntegerField(blank=True, null=True)
    notifyall = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    cost = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    roleid = models.BigIntegerField(blank=True, null=True)
    customint1 = models.BigIntegerField(blank=True, null=True)
    customint2 = models.BigIntegerField(blank=True, null=True)
    customint3 = models.BigIntegerField(blank=True, null=True)
    customint4 = models.BigIntegerField(blank=True, null=True)
    customint5 = models.BigIntegerField(blank=True, null=True)
    customint6 = models.BigIntegerField(blank=True, null=True)
    customint7 = models.BigIntegerField(blank=True, null=True)
    customint8 = models.BigIntegerField(blank=True, null=True)
    customchar1 = models.CharField(max_length=255, blank=True, null=True)
    customchar2 = models.CharField(max_length=255, blank=True, null=True)
    customchar3 = models.CharField(max_length=1333, blank=True, null=True)
    customdec1 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customdec2 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customtext1 = models.TextField(blank=True, null=True)
    customtext2 = models.TextField(blank=True, null=True)
    customtext3 = models.TextField(blank=True, null=True)
    customtext4 = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_enrol'
        db_table_comment = 'Instances of enrolment plugins used in courses, fields marke'


class Mdlm9Forum(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    duedate = models.BigIntegerField()
    cutoffdate = models.BigIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    grade_forum = models.BigIntegerField()
    grade_forum_notify = models.SmallIntegerField()
    maxbytes = models.BigIntegerField()
    maxattachments = models.BigIntegerField()
    forcesubscribe = models.IntegerField()
    trackingtype = models.IntegerField()
    rsstype = models.IntegerField()
    rssarticles = models.IntegerField()
    timemodified = models.BigIntegerField()
    warnafter = models.BigIntegerField()
    blockafter = models.BigIntegerField()
    blockperiod = models.BigIntegerField()
    completiondiscussions = models.IntegerField()
    completionreplies = models.IntegerField()
    completionposts = models.IntegerField()
    displaywordcount = models.IntegerField()
    lockdiscussionafter = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_forum'
        db_table_comment = 'Forums contain and structure discussion'


class Mdlm9ForumDiscussions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    forum = models.BigIntegerField()
    name = models.CharField(max_length=255)
    firstpost = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    assessed = models.IntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    pinned = models.IntegerField()
    timelocked = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_forum_discussions'
        db_table_comment = 'Forums are composed of discussions'


class Mdlm9ForumPosts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    discussion = models.BigIntegerField()
    parent = models.BigIntegerField()
    userid = models.BigIntegerField()
    created = models.BigIntegerField()
    modified = models.BigIntegerField()
    mailed = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    messageformat = models.IntegerField()
    messagetrust = models.IntegerField()
    attachment = models.CharField(max_length=100)
    totalscore = models.SmallIntegerField()
    mailnow = models.BigIntegerField()
    deleted = models.IntegerField()
    privatereplyto = models.BigIntegerField()
    wordcount = models.BigIntegerField(blank=True, null=True)
    charcount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdlm9_forum_posts'
        db_table_comment = 'All posts are stored in this table'


class Mdlm9ForumRead(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    firstread = models.BigIntegerField()
    lastread = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_forum_read'


class Mdlm9Modules(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    search = models.CharField(max_length=255)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_modules'
        db_table_comment = 'modules available in the site'


class Mdlm9Role(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    shortname = models.CharField(max_length=100)
    description = models.TextField()
    sortorder = models.BigIntegerField()
    archetype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdlm9_role'
        db_table_comment = 'moodle roles'


class Mdlm9RoleAssignments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_role_assignments'
        db_table_comment = 'assigning roles in different context'


class Mdlm9User(models.Model):
    id = models.IntegerField(primary_key=True)
    auth = models.CharField(max_length=20)
    confirmed = models.IntegerField()
    policyagreed = models.IntegerField()
    deleted = models.IntegerField()
    suspended = models.IntegerField()
    mnethostid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.IntegerField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.BigIntegerField()
    lastaccess = models.BigIntegerField()
    lastlogin = models.BigIntegerField()
    currentlogin = models.BigIntegerField()
    lastip = models.CharField(max_length=45)
    secret = models.CharField(max_length=15)
    picture = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    mailformat = models.IntegerField()
    maildigest = models.IntegerField()
    maildisplay = models.IntegerField()
    autosubscribe = models.IntegerField()
    trackforums = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    trustbitmask = models.BigIntegerField()
    imagealt = models.CharField(max_length=255, blank=True, null=True)
    lastnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    firstnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    alternatename = models.CharField(max_length=255, blank=True, null=True)
    moodlenetprofile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdlm9_user'
        db_table_comment = 'One record for each person'


class Mdlm9UserEnrolments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    status = models.BigIntegerField()
    enrolid = models.ForeignKey(Mdlm9Enrol, on_delete=models.CASCADE, related_name='enrol_enrolments')
    userid = models.ForeignKey(Mdlm9User, on_delete=models.CASCADE, related_name='user_enrolments')
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdlm9_user_enrolments'
        db_table_comment = 'Users participating in courses (aka enrolled users) - everyb'

class Meta:
    app_label = 'analitics'
    # Cambia el nombre de la base de datos según sea necesario
    db_table = 'moodle_table'
    managed = False
    # Cambia el nombre de la base de datos según sea necesario
    using = 'other'