# Foreman2Icinga

This Python tool generates
Icinga2 configuration file fetching informations from a Foreman server.

For using it, proper values should be configured in `config.py`,
at least the `baseurl` and `auth` parameters.

The script currently only define hosts and hostgroups.

The tools is composed of:

 - `ForemanExtractor` class, to get informations from a Foreman server;
 - `IcingaGenerator` class, to generate Icinga2 definitions;
 - `generate.py` script, that fetches information from Foreman and prints out Icinga2 definition.

To run it just:

   ./generate.py

It will print hosts and hostgroups definition on standard output.

For parameters and sample values see the included `config.py.sample`.
