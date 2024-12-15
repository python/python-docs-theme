Changelog
=========

`2024.12 <https://github.com/python/python-docs-theme/releases/tag/2024.12>`_
-----------------------------------------------------------------------------

- Hide header and search bar when printing (#204)
    Contributed by Hugo van Kemenade

`2024.10 <https://github.com/python/python-docs-theme/releases/tag/2024.10>`_
-----------------------------------------------------------------------------

- Add support for Python 3.13 (#196)
    Contributed by Hugo van Kemenade
- Drop support for Python 3.8 (#197)
    Contributed by Hugo van Kemenade
- Add script for handling translations (#195)
    Contributed by Rafael Fontenelle
- Generate digital attestations for PyPI (PEP 740) (#198)
    Contributed by Hugo van Kemenade

`2024.6 <https://github.com/python/python-docs-theme/releases/tag/2024.6>`_
---------------------------------------------------------------------------

- Add backgrounds and borders to admonitions (#190)
    Contributed by Hugo van Kemenade
- Use different colour for 'Return value: Borrowed reference' (#188)
    Contributed by Hugo van Kemenade

`2024.4 <https://github.com/python/python-docs-theme/releases/tag/2024.4>`_
---------------------------------------------------------------------------

- Add colour to version change directives (#185)
    Contributed by Hugo van Kemenade
- Only show 'Last updated on ...' when ``last_updated`` defined (#183)
    Contributed by Hugo van Kemenade
- Use system font stack for all code (#186)
    Contributed by Hugo van Kemenade

`2024.3 <https://github.com/python/python-docs-theme/releases/tag/2024.3>`_
---------------------------------------------------------------------------

- Modernise font: use system font stack to improve text readability and webpage performance (#174)
    Contributed by Hugo van Kemenade
- Remove incorrect CSS property (#178)
    Contributed by Kerim Kabirov

`2024.2 <https://github.com/python/python-docs-theme/releases/tag/2024.2>`_
---------------------------------------------------------------------------

- Do not underline navigation links (#169)
   Contributed by Hugo van Kemenade
- Only apply underline offset to code formatting for underline visibility (#171)
   Contributed by Hugo van Kemenade

`2024.1 <https://github.com/python/python-docs-theme/releases/tag/2024.1>`_
---------------------------------------------------------------------------

- Underline links for readability and a11y (#160, #166)
   Contributed by Hugo van Kemenade
- Add ``hosted_on`` variable for a link in the footer (#165)
   Contributed by Hugo van Kemenade
- Consistently reference ``theme_root_icon`` (#163)
   Contributed by Marko Budiselic
- Dark mode: fix contrast of footer highlight (#162)
   Contributed by Hugo van Kemenade

`2023.9 <https://github.com/python/python-docs-theme/releases/tag/2023.9>`_
---------------------------------------------------------------------------

- Focus search box when pressing slash (#153)
   Contributed by Hugo van Kemenade

`2023.8 <https://github.com/python/python-docs-theme/releases/tag/2023.8>`_
---------------------------------------------------------------------------

- Add Python 3.12 and 3.13 classifiers (#147)
   Contributed by Hugo van Kemenade
- Dark mode: Also give aside.topic a dark background (#150)
   Contributed by Hugo van Kemenade
- Restore the menu on mobile devices (inadvertently broken in 2023.7) (#146)
   Contributed by Hugo van Kemenade

`2023.7 <https://github.com/python/python-docs-theme/releases/tag/2023.7>`_
---------------------------------------------------------------------------

- Fix compatibility with Sphinx 7.1 (#137)
   Contributed by Pradyun Gedam
- Enable the slash keypress to focus the search field (#141)
   Contributed by Mike Fiedler
- Sphinx 6.2 fix: add ``nav.contents`` where ``div.topic`` is used (#138)
   Contributed by Hugo van Kemenade
- Dark mode: fix contrast for C++ specific styling (#133)
   Contributed by Hugo van Kemenade
- Don't let long code literals extend beyond the right side of the screen (#139)
   Contributed by Hugo van Kemenade
- Test with Python 3.12 (#140)
   Contributed by Hugo van Kemenade

`2023.5 <https://github.com/python/python-docs-theme/releases/tag/2023.5>`_
---------------------------------------------------------------------------

- Add a dark theme. (#44)
   Contributed by Nils K
- Fix: Remove searchbox id from form. (fixes #117)
   Contributed by Nils K
- Update ``python-docs-theme`` to work with Sphinx 5 & 6. (#99 & #127)
   Contributed by Adam Turner
- Override font for ``.sig`` for consistency with other code blocks. (#121)
   Contributed by Chris Warrick
- Dark mode: add class to invert image brightness. (#128)
   Contributed by Hugo van Kemenade


`2023.3.1 <https://github.com/python/python-docs-theme/releases/tag/2023.3.1>`_
-------------------------------------------------------------------------------

- Skip cache-busting for old Sphinx #113


`2023.3 <https://github.com/python/python-docs-theme/releases/tag/2023.3>`_
---------------------------------------------------------------------------

- Fix problem with monospace rendering in Vivaldi #104
- Fix mobile nav obstructing content #96
- Reduce footer margin only for desktop #106
- Append a hash ?digest to CSS files for cache-busting #108


`2022.1 <https://github.com/python/python-docs-theme/releases/tag/2022.1>`_
----------------------------------------------------------------------------

- Add a configuration for license URL. (#90)
- Exclude the floating navbar from CHM help. (#84)
- Make sidebar scrollable and sticky (on modern browsers) (#91)


`2021.11.1 <https://github.com/python/python-docs-theme/releases/tag/2021.11.1>`_
----------------------------------------------------------------------------------

- Fix monospace again, on buggy Google Chrome (#87)
   Contributed by Tushar Sadhwani


`2021.11 <https://github.com/python/python-docs-theme/releases/tag/2021.11>`_
------------------------------------------------------------------------------

- Fix monospace on buggy Google Chrome (#85)
   Contributed by Tushar Sadhwani


`2021.8 <https://github.com/python/python-docs-theme/releases/tag/2021.8>`_
-----------------------------------------------------------------------------

- Add the copyright_url variable in the theme (#67)
   Contributed by jablonskidev
- Improve readability (#79)
   Contributed by Olga Bulat
- Remove #searchbox on mobile to fix a layout bug (#76)
   Contributed by Olga Bulat
- Fix the appearance of version/language selects (#74)
   Contributed by Olga Bulat


`2021.5 <https://github.com/python/python-docs-theme/releases/tag/2021.5>`_
-----------------------------------------------------------------------------

- Make the theme responsive (#46)
   Contributed by Olga Bulat.
- Use Python 3.8 for the Github Actions (#71)
   Contributed by Stéphane Wirtel.
- Use default pygments theme (#68)
   Contributed by Aaron Carlisle.
- Test Github action to validate the theme against docsbuild scripts. (#69)
   Contributed by Julien Palard.
- Add the copy button to pycon3 highlighted code blocks. (#64)
   Contributed by Julien Palard.


`2020.12 <https://github.com/python/python-docs-theme/releases/tag/v2020.12>`_
------------------------------------------------------------------------------

- Updated the readme, to remind user to install the package in a virtual environment. (#41)
   Contributed by Mariatta.
- Updated the package url, using the GitHub repository instead of docs.python.org (#49)
   Contributed by Pradyun Gedam.
- Added license information to the footer of the doc (#36)
   Contributed by Todd.
- Fixed typo in the footer (#52)
   Contributed by Dominic Davis-Foster.
- Added information on how to use the package (#32)
   Contributed by Tapasweni Pathak.
- Fixed code formatting (#53).
   Contributed by Hugo van Kemenade.
- Fixed code bgcolor and codetextcolor for Sphinx 3.1.0+ (#57)
   Contributed by Zhiming Wang.

2018.7
------
Corresponds to `44a8f30 <https://github.com/python/python-docs-theme/commit/44a8f306db9ec86d277a8a687538d5d51e415130>`_


`2018.2 <https://github.com/python/python-docs-theme/releases/tag/2018.2>`_
---------------------------------------------------------------------------

Initial release.
