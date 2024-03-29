# -*- coding: utf-8 -*-

'''
 Module
     development_config.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_func_struct_vue is free software: you can redistribute it
     and/or modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation, either version 3 of the
     License, or (at your option) any later version.
     flask_func_struct_vue is distributed in the hope that it will
     be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class DevelopmentConfig with attribute(s) and method(s).
     Development database configuration.
'''

import sys

try:
    from app_server.configuration.database import BaseConfig
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DevelopmentConfig(BaseConfig):
    '''
        Define class DevelopmentConfig with attribute(s) and method(s).
        Development database configuration.
        It defines:

            :attributes:
                | DB_USER - Database connection username
                | DB_PASSWORD - Database connection user password
                | DB_HOST - Database server address
                | DB_PORT - Database server port
                | DB_DIALECT - Database dialect prefix
                | SQLALCHEMY_DATABASE_URI - Set DB URI
            :methods:
                | None
    '''

    DB_USER = 'mydbuser'
    DB_PASSWORD = 'mydbpassword'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_NAME = 'manage_users'
    DB_DIALECT = 'mysql+mysqlconnector'
    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
