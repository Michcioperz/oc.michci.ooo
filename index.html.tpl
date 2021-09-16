<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Michcio's collection of picrews</h1>
    <ul>
      {{ range (datasource "oc" | coll.Sort "dt" | coll.Reverse) -}}
      <li>
        <p>
	  <time datetime="{{ .dt }}">{{ .dt }}</time>
	  |
	  generated with <a href="https://picrew.me/image_maker/{{ .id }}">#{{ .id }}</a>
	</p>
	<p><img src="{{ .id }}.png"></p>
      </li>
      {{- end }}
    </ul>
  </body>
</html>
