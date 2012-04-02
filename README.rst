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

This ZenPack has no special installation considerations.  Depending on the
version of Zenoss you're installing the ZenPack into, you will need to verify
that you have the correct package (.egg) to install.

* Zenoss 4.1 and later: The ZenPack file must end with ``-py2.7.egg``.
* Zenoss 3.0 - 4.0: The ZenPack file must end with ``-py2.6.egg``.
* Zenoss 2.2 - 2.5: The ZenPack file must end with ``-py2.4.egg``.

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
