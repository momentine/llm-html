---
title: "Best Practice"
track: best-case
layout: track
---

{% if site.data.intro.html %}
{{ site.data.intro.html | markdownify }}
{% endif %}

{% assign comps = site.pages | where: 'track', page.track | where: 'kind', 'component' | sort: 'order' %}
{% for c in comps %}
<a id="{{ c.slug }}"></a>
{{ c.content }}
{% endfor %}
