#!/usr/bin/env python

import os

ADDITIONAL_LOCALES = ["en-US", "multi"]
TAG = "default"
AUS_SERVER = "dev-stage01.build.mozilla.org"
FTP_SERVER = "dev-stage01.build.mozilla.org"
AUS_UPLOAD_BASE_DIR = "/opt/aus2/snippets/staging"
AUS_DIR_BASE_NAME = "Fennec-%(version)s-build%(buildnum)d"
FTP_UPLOAD_BASE_DIR = "/pub/mozilla.org/mobile/candidates/%(version)s-candidates/build%(buildnum)d"
DOWNLOAD_BASE_URL = "http://%s%s" % (FTP_SERVER, FTP_UPLOAD_BASE_DIR)
#DOWNLOAD_BASE_URL = "http://ftp.mozilla.org/pub/mozilla.org/mobile/candidates/%(version)s-candidates/build%(buildnum)d"
APK_BASE_NAME = "fennec-%(version)s.%(locale)s.android-arm.apk"
BUILDID_BASE_URL = DOWNLOAD_BASE_URL + "/%(platform)s_info.txt"
FFXBLD_SSH_KEY = '~/.ssh/ffxbld_dsa'
CLTBLD_SSH_KEY = '~/.ssh/id_rsa'

RELEASE_UPDATE_URL = "http://download.mozilla.org/?product=fennec-%(version)s-complete&os=%(platform)s&lang=%(locale)s"
BETATEST_UPDATE_URL = "http://stage.mozilla.org/pub/mozilla.org/mobile/candidates/%(version)s-candidates/build%(buildnum)d/%(apk_name)s"
SNIPPET_TEMPLATE = """version=1
type=complete
url=%(url)s
hashFunction=sha512
hashValue=%(sha512_hash)s
size=%(size)d
build=%(buildid)s
appv=%(version)s
extv=%(version)s
"""

KEYSTORE = "%s/.android/android.keystore" % os.environ['HOME']

JAVA_HOME = "/tools/jdk6"
JARSIGNER = "%s/bin/jarsigner" % JAVA_HOME
KEY_ALIAS = "nightly"

config = {
    "log_name": "sign_android_staging_beta",
    "work_dir": "staging_beta",

    "additional_locales": ADDITIONAL_LOCALES,
    "locales_file": "buildbot-configs/mozilla/l10n-changesets_mobile-beta.json",
    "release_config_file": "buildbot-configs/mozilla/staging_release-fennec-mozilla-beta.py",

    "platforms": ['android', 'android-xul', 'android-armv6'],
    "platform_config": {
        'android': {},
        'android-xul': {
            'locales': ['en-US', 'multi'],
        },
        'android-armv6': {
            'locales': ['en-US'],
            'apk_base_name': 'fennec-%(version)s.%(locale)s.android-arm-armv6.apk',
        },
    },
    "update_platforms": ['android'],
    "update_platform_map": {
        'android': 'Android_arm-eabi-gcc3',
        'android-xul': 'Android_arm-eabi-gcc3-xul',
        'android-armv6': 'Android_arm-eabi-gcc3-armv6',
    },
#    "enable_partner_repacks": True,
#    "partner_platforms": ['android'],
#    "partners": ['google-play'],
    "update_channels": {
        'release': {
            'url': RELEASE_UPDATE_URL,
            'template': SNIPPET_TEMPLATE,
            'dir_base_name': AUS_DIR_BASE_NAME,
        },
        'betatest': {
            'url': BETATEST_UPDATE_URL,
            'template': SNIPPET_TEMPLATE,
            'dir_base_name': '%s-test' % AUS_DIR_BASE_NAME,
        },
        'releasetest': {
            'url': RELEASE_UPDATE_URL,
            'template': SNIPPET_TEMPLATE,
            'dir_base_name': '%s-test' % AUS_DIR_BASE_NAME,
        },
    },
    "ftp_upload_base_dir": FTP_UPLOAD_BASE_DIR,
    # These should be from release_config, but that has stage-ffxbld
    # which doesn't work with dev-stage01.
    "ftp_ssh_key": FFXBLD_SSH_KEY,
    "ftp_user": "ffxbld",

    "aus_ssh_key": CLTBLD_SSH_KEY,
    "aus_upload_base_dir": AUS_UPLOAD_BASE_DIR,

    "apk_base_name": APK_BASE_NAME,
    "unsigned_apk_base_name": APK_BASE_NAME,
    "download_base_url": DOWNLOAD_BASE_URL,
    "download_unsigned_base_subdir": "unsigned/%(platform)s/%(locale)s",
    "download_signed_base_subdir": "%(platform)s/%(locale)s",
    "buildid_base_url": BUILDID_BASE_URL,
    "old_buildid_base_url": BUILDID_BASE_URL,

    "keystore": KEYSTORE,
    "key_alias": KEY_ALIAS,
    "env": {
        "PATH": JAVA_HOME + "/bin:%(PATH)s",
    },
    "exes": {
        "jarsigner": JARSIGNER,
        "zipalign": "/tools/android-sdk-r13/tools/zipalign",
    },
    "signature_verification_script": "tools/release/signing/verify-android-signature.sh",

    "user_repo_override": "users/stage-ffxbld",
    "tag_override": TAG,
    "repos": [{
        "repo": "http://hg.mozilla.org/%(user_repo_override)s/tools",
        "dest": "tools",
    },{
        "repo": "http://hg.mozilla.org/%(user_repo_override)s/buildbot-configs",
        "dest": "buildbot-configs",
    }],
}
