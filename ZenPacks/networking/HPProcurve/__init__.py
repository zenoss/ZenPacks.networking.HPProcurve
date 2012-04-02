###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2008, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import Globals

from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused

unused(Globals)


class ZenPack(ZenPackBase):
    def install(self, app):
        """Custom install method for this ZenPack."""
        self.pre_install(app)
        super(ZenPack, self).install(app)

    def pre_install(self, app):
        """Perform steps that should be done before default install."""
        devices = app.zport.dmd.Devices
        events = app.zport.dmd.Events

        # /Network/Switch/HP device class is a prerequisite.
        devices.createOrganizer('/Network/Switch/HP')

        # /Net/traps event class is a prerequisite.
        events.createOrganizer('/Net/traps')
