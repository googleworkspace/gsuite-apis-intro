G Suite APIs Intro codelab
==========================

This codelab introduces developers to G Suite APIs (Gmail, Google Drive, Calendar, Sheets, Slides, etc.) by writing a simple Python script that lists the first 100 files/folders in a user's Google Drive. Access it at http://g.co/codelabs/gsuite-apis-intro.

Introduction
------------

This codelab introduces you to using G Suite (REST/HTTP) APIs. The example will be done in Python for brevity and wide availability, but you can also choose to use your favorite development language. You'll learn how to use the developer console to create and manage projects, including obtaining the credentials you'll need in your app. With the formalities taken care of, you'll write an app to display the first 100 files & folders in your Google Drive by using the Drive API.

Pre-requisites
--------------

- A Google account (G Suite accounts may require administrator approval)
- Familiarity to POSIX-compliant systems like Linux & Mac OS X
- Ability to create source files with either a code editor or shell commands.
- Basic skills in [Python](http://python.org) (2 or 3), but you use [any supported language](http://developers.google.com/api-client-library)
- Some files and/or folders in your [Google Drive](http://drive.google.com)

Repo files
----------

Filename | Description
--- | ---
`drive_list.py` | The original sample
`drive_list-new.py` | Same as `drive_list.py` but uses the newer auth libraries

Support
-------

- Stack Overflow: https://stackoverflow.com/questions/tagged/google-drive-sdk

If you've found an error in this sample, please file an issue. Patches are
encouraged; please refer to [CONTRIBUTING](CONTRIBUTING.md) for details.
