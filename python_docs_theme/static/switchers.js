'use strict';

const _is_file_uri = (uri) => uri.startsWith('file://');

const _IS_LOCAL = _is_file_uri(window.location.href);
const _CONTENT_ROOT = document.documentElement.dataset.content_root;
const _CURRENT_PREFIX = _IS_LOCAL
  ? null
  : new URL(_CONTENT_ROOT, window.location).pathname;
const _CURRENT_RELEASE = DOCUMENTATION_OPTIONS.VERSION || '';
const _CURRENT_VERSION = _CURRENT_RELEASE.split('.').slice(0, 2).join('.');
const _CURRENT_LANGUAGE = DOCUMENTATION_OPTIONS.LANGUAGE?.toLowerCase() || 'en';

/**
 * Change the current page to the first existing URL in the list.
 * @param {Array<string>} urls
 * @private
 */
const _navigate_to_first_existing = async (urls) => {
  // Navigate to the first existing URL of urls.
  for (const url of urls) {
    try {
      const response = await fetch(url, { method: 'GET' })
      if (response.ok) {
        window.location.href = url;
        return url;  // Avoid race conditions with multiple redirects
      }
    } catch(err) {
      console.error(`Error in: ${url}`);
      console.error(err)
    }
  }

  // if all else fails, redirect to the d.p.o root
  window.location.href = '/';
};

/**
 * Navigate to the selected version.
 * @param {Event} event
 * @returns {Promise<void>}
 */
const on_version_switch = async (event) => {
  if (_IS_LOCAL) return;

  const selected_version = event.target.value;
  // Special 'default' case for English.
  const new_prefix =
    _CURRENT_LANGUAGE === 'en'
      ? `/${selected_version}/`
      : `/${_CURRENT_LANGUAGE}/${selected_version}/`;
  const new_prefix_en = `/${selected_version}/`;
  if (_CURRENT_PREFIX !== new_prefix) {
    // Try the following pages in order:
    // 1. The current page in the current language with the new version
    // 2. The current page in English with the new version
    // 3. The documentation home in the current language with the new version
    // 4. The documentation home in English with the new version
    await _navigate_to_first_existing([
      window.location.href.replace(_CURRENT_PREFIX, new_prefix),
      window.location.href.replace(_CURRENT_PREFIX, new_prefix_en),
      new_prefix,
      new_prefix_en,
    ]);
  }
};

/**
 * Navigate to the selected language.
 * @param {Event} event
 * @returns {Promise<void>}
 */
const on_language_switch = async (event) => {
  if (_IS_LOCAL) return;

  const selected_language = event.target.value;
  // Special 'default' case for English.
  const new_prefix =
    selected_language === 'en'
      ? `/${_CURRENT_VERSION}/`
      : `/${selected_language}/${_CURRENT_VERSION}/`;
  if (_CURRENT_PREFIX !== new_prefix) {
    // Try the following pages in order:
    // 1. The current page in the new language with the current version
    // 2. The documentation home in the new language with the current version
    await _navigate_to_first_existing([
      window.location.href.replace(_CURRENT_PREFIX, new_prefix),
      new_prefix,
    ]);
  }
};

/**
 * Set up the version and language switchers.
 * @returns {Promise<void>}
 */
const initialise_switchers = async () => {
  try {
    // Update the version select elements
    document
      .querySelectorAll('.version_switcher_placeholder select')
        .forEach((select) => {
          if (_IS_LOCAL) {
            select.disabled = true;
            select.title = 'Version switching is disabled in local builds';
          }
          select.addEventListener('change', on_version_switch);
          select.parentElement.classList.remove('version_switcher_placeholder');
        });

    // Update the language select elements
    document
      .querySelectorAll('.language_switcher_placeholder select')
        .forEach((select) => {
          if (_IS_LOCAL) {
            select.disabled = true;
            select.title = 'Language switching is disabled in local builds';
          }
          select.addEventListener('change', on_language_switch);
          select.parentElement.classList.remove('language_switcher_placeholder');
        });
  } catch (error) {
    console.error(error);
  }
};

if (document.readyState !== 'loading') {
  initialise_switchers();
} else {
  document.addEventListener('DOMContentLoaded', initialise_switchers);
}
