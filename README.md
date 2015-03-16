# Foreman2Icinga

This Python tools generates
Icinga2 configuration file fetching informations from a Foreman server.

Before using it you should setup proper values in the `foremanconfig.py` file,
at least the `baseurl` and `auth` parameters.

The script currently only define hosts and hostgroups.

The tools is composed of:

 - `ForemanExtractor` class, to get informations from a Foreman server;
 - `IcingaGenerator` class, to generate Icinga2 definitions;
 - `generate.py` script, that fetches information from Foreman and prints out Icinga2 definition.

To run it just:

   ./generate.py

It will print hosts and hostgroups definition on standard output.

