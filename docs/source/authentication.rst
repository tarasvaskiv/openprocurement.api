.. _authentication:

Authentication
==============

Some of the API requests (especially the ones that are read-only GET
requests) do not require any authenication.  The other ones, that modify data
into the database, require broker authentication via API key.  Additionally,
owner tokens are issued to facilitate multiple actor roles upon object creation.

API keys
--------

API key is username to use with Basic Authenication scheme (see :rfc:`2617#section-2`). 
