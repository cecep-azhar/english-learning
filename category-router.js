/* Shared category resolution/loading logic for index.html and quiz.html.
   Canonical slugs and default must match content/categories.json (see notes/task.md A1). */
(function (global) {
  'use strict';

  var CANONICAL = [
    'general', 'business', 'finance', 'admin', 'web-design', 'seo',
    'graphic-design', 'video-editing', 'virtual-assistant',
    'copywriting', 'software-engineering'
  ];
  var DEFAULT_CATEGORY = 'software-engineering';
  var SESSION_KEY = 'ff_active_category';

  function resolveCategory() {
    var raw = null;
    try {
      raw = new URLSearchParams(location.search).get('category');
    } catch (e) { /* URLSearchParams unsupported: fall through to default */ }

    if (!raw) {
      var stored = null;
      try { stored = sessionStorage.getItem(SESSION_KEY); } catch (e) {}
      if (stored && CANONICAL.indexOf(stored) !== -1) {
        return { slug: stored, wasInvalid: false };
      }
      return { slug: DEFAULT_CATEGORY, wasInvalid: false };
    }

    if (CANONICAL.indexOf(raw) !== -1) {
      try { sessionStorage.setItem(SESSION_KEY, raw); } catch (e) {}
      return { slug: raw, wasInvalid: false };
    }

    return { slug: DEFAULT_CATEGORY, wasInvalid: true, attempted: raw };
  }

  function rememberCategory(slug) {
    try { sessionStorage.setItem(SESSION_KEY, slug); } catch (e) {}
  }

  // Normalizes the two content shapes in the wild:
  //   scripts.json          -> { title, total_items, scripts }
  //   content/<slug>.json   -> { id, name, scripts }
  function normalizeContent(raw, slug) {
    return {
      id: raw.id || slug,
      name: raw.name || raw.title || slug,
      scripts: raw.scripts || []
    };
  }

  function fetchJSON(url) {
    return fetch(url).then(function (resp) {
      if (!resp.ok) throw new Error('HTTP ' + resp.status + ' for ' + url);
      return resp.json();
    });
  }

  function fetchCategoryContent(slug) {
    return fetchJSON('/content/' + slug + '.json').then(function (raw) {
      return normalizeContent(raw, slug);
    });
  }

  function fetchCategoryMeta(slug) {
    return fetchJSON('/content/categories.json').then(function (data) {
      var list = data.categories || [];
      for (var i = 0; i < list.length; i++) {
        if (list[i].id === slug) return list[i];
      }
      return null;
    });
  }

  global.CategoryRouter = {
    CANONICAL: CANONICAL,
    DEFAULT_CATEGORY: DEFAULT_CATEGORY,
    SESSION_KEY: SESSION_KEY,
    resolveCategory: resolveCategory,
    rememberCategory: rememberCategory,
    normalizeContent: normalizeContent,
    fetchCategoryContent: fetchCategoryContent,
    fetchCategoryMeta: fetchCategoryMeta
  };
})(window);
