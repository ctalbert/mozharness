# This is a template config file for jetperf production

config = {

    "datazilla_urls": ['http://10.8.73.32/jetperf/load_test'],

    "exes": {
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
    },

    "find_links": ["http://puppetagain.pub.build.mozilla.org/data/python/packages"],

    "default_actions": [
        'clobber',
        'pull',
        'build',
        'download-and-extract',
        'create-virtualenv',
        'install',
        'test',
        'baseline',
        'report-tbpl-status'
        ],
}
