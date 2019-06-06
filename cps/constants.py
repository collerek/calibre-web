#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   This file is part of the Calibre-Web (https://github.com/janeczku/calibre-web)
#     Copyright (C) 2019 OzzieIsaacs, pwr
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import division, print_function, unicode_literals
import sys
import os
from collections import namedtuple


BASE_DIR            = sys.path[0]
STATIC_DIR          = os.path.join(BASE_DIR, 'cps', 'static')
TEMPLATES_DIR       = os.path.join(BASE_DIR, 'cps', 'templates')
TRANSLATIONS_DIR    = os.path.join(BASE_DIR, 'cps', 'translations')
CONFIG_DIR          = os.environ.get('CALIBRE_DBPATH', BASE_DIR)


ROLE_USER               = 0 << 0
ROLE_ADMIN              = 1 << 0
ROLE_DOWNLOAD           = 1 << 1
ROLE_UPLOAD             = 1 << 2
ROLE_EDIT               = 1 << 3
ROLE_PASSWD             = 1 << 4
ROLE_ANONYMOUS          = 1 << 5
ROLE_EDIT_SHELFS        = 1 << 6
ROLE_DELETE_BOOKS       = 1 << 7
ROLE_VIEWER             = 1 << 8

ALL_ROLES = {
                "admin_role": ROLE_ADMIN,
                "download_role": ROLE_DOWNLOAD,
                "upload_role": ROLE_UPLOAD,
                "edit_role": ROLE_EDIT,
                "passwd_role": ROLE_PASSWD,
                "edit_shelf_role": ROLE_EDIT_SHELFS,
                "delete_role": ROLE_DELETE_BOOKS,
                "viewer_role": ROLE_VIEWER,
            }

DETAIL_RANDOM           = 1 <<  0
SIDEBAR_LANGUAGE        = 1 <<  1
SIDEBAR_SERIES          = 1 <<  2
SIDEBAR_CATEGORY        = 1 <<  3
SIDEBAR_HOT             = 1 <<  4
SIDEBAR_RANDOM          = 1 <<  5
SIDEBAR_AUTHOR          = 1 <<  6
SIDEBAR_BEST_RATED      = 1 <<  7
SIDEBAR_READ_AND_UNREAD = 1 <<  8
SIDEBAR_RECENT          = 1 <<  9
SIDEBAR_SORTED          = 1 << 10
MATURE_CONTENT          = 1 << 11
SIDEBAR_PUBLISHER       = 1 << 12
SIDEBAR_RATING          = 1 << 13
SIDEBAR_FORMAT          = 1 << 14

ADMIN_USER_ROLES        = (ROLE_VIEWER << 1) - 1 - (ROLE_ANONYMOUS | ROLE_EDIT_SHELFS)
ADMIN_USER_SIDEBAR      = (SIDEBAR_FORMAT << 1) - 1

UPDATE_STABLE       = 0 << 0
AUTO_UPDATE_STABLE  = 1 << 0
UPDATE_NIGHTLY      = 1 << 1
AUTO_UPDATE_NIGHTLY = 1 << 2

LOGIN_STANDARD      = 0
LOGIN_LDAP          = 1
LOGIN_OAUTH_GITHUB  = 2
LOGIN_OAUTH_GOOGLE  = 3


DEFAULT_PASSWORD    = "admin123"
DEFAULT_PORT        = 8083
try:
    env_CALIBRE_PORT = os.environ.get("CALIBRE_PORT", DEFAULT_PORT)
    DEFAULT_PORT = int(env_CALIBRE_PORT)
except ValueError:
    print('Environment variable CALIBRE_PORT has invalid value (%s), faling back to default (8083)' % env_CALIBRE_PORT)
del env_CALIBRE_PORT


EXTENSIONS_AUDIO    = {'mp3', 'm4a', 'm4b'}
EXTENSIONS_CONVERT  = {'pdf', 'epub', 'mobi', 'azw3', 'docx', 'rtf', 'fb2', 'lit', 'lrf', 'txt', 'htmlz', 'rtf', 'odt'}
EXTENSIONS_UPLOAD   = {'txt', 'pdf', 'epub', 'mobi', 'azw', 'azw3', 'cbr', 'cbz', 'cbt', 'djvu', 'prc', 'doc', 'docx',
                       'fb2', 'html', 'rtf', 'odt', 'mp3',  'm4a', 'm4b'}
# EXTENSIONS_READER = set(['txt', 'pdf', 'epub', 'zip', 'cbz', 'tar', 'cbt'] +
#                         (['rar','cbr'] if feature_support['rar'] else []))


def has_flag(value, bit_flag):
    return bit_flag == (bit_flag & (value or 0))


"""
 :rtype: BookMeta
"""
BookMeta = namedtuple('BookMeta', 'file_path, extension, title, author, cover, description, tags, series, '
                                  'series_id, languages')


# clean-up the module namespace
del sys, os, namedtuple
