===============================================================================
ZenPacks.networking.HPProcurve
===============================================================================


About
===============================================================================

This ZenPack adds support for monitoring HP ProCurve switches.


Features
-------------------------------------------------------------------------------

The following features are provided:

* CPU utilization monitoring.
* Power supply status monitoring.
* Fan status monitoring.
* Event mappings for HP ProCurve SNMP traps.
* Identification of HP ProCurve hardware model in product catalog.


Prerequisites
-------------------------------------------------------------------------------

==================  ========================================================
Prerequisite        Restriction
==================  ========================================================
Zenoss Platform     2.2 or greater
Zenoss Processes    zenperfsnmp, zentrap
==================  ========================================================


Limitations
-------------------------------------------------------------------------------

The serial number from the modeler is not currently retrieved.


Usage
===============================================================================


Installation
-------------------------------------------------------------------------------

This ZenPack has no special installation considerations. You should install the
most recent version of the ZenPack for the version of Zenoss you're running.

* `Packages for Zenoss 4.2`_
* `Packages for Zenoss 4.1`_
* `Packages for Zenoss 4.0`_
* `Packages for Zenoss 3.2`_

.. _Packages for Zenoss 4.2: http://zenpacks.zenoss.com/pypi/github/4.2/ZenPacks.networking.HPProcurve
.. _Packages for Zenoss 4.1: http://zenpacks.zenoss.com/pypi/github/4.1/ZenPacks.networking.HPProcurve
.. _Packages for Zenoss 4.0: http://zenpacks.zenoss.com/pypi/github/4.0/ZenPacks.networking.HPProcurve
.. _Packages for Zenoss 3.2: http://zenpacks.zenoss.com/pypi/github/3.2/ZenPacks.networking.HPProcurve

To install the ZenPack you must copy the ``.egg`` file to your Zenoss master
server and run the following command as the ``zenoss`` user::

    zenpack --install <filename.egg>

After installing you must restart Zenoss by running the following command as
the ``zenoss`` user on your master Zenoss server::

    zenoss restart

If you have distributed collectors you must also update them after installing
the ZenPack.


Configuring
-------------------------------------------------------------------------------

This ZenPack requires standard Zenoss SNMP monitoring configuration. Use the
following steps to configure Zenoss to monitor your HP ProCurve switches using
SNMP.

1. Verify that SNMP is enabled on the switch.
2. Verify that the switch is configured to send SNMP traps to the address of
   one of your Zenoss collector servers.
3. Verify that the switch's SNMP community string is in the ``zSnmpCommunities``
   list for the the ``/Network/Switch/HP`` device class.
4. Add your HP ProCurve switch(es) to the ``/Network/Switch/HP`` device class.


Removal
-------------------------------------------------------------------------------

This ZenPack has no special removal considerations. To remove this ZenPack you
must run the following command as the ``zenoss`` user on your master Zenoss
server::

    zenpack --remove ZenPacks.zenoss.SolarisMonitor

You must then restart the master Zenoss server by running the following command
as the ``zenoss`` user::

    zenoss restart
