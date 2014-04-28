# -*- coding: utf-8 -*- 
tpl_page = """
<!DOCTYPE html>
<html>
<head>    
<title>Lists of {title}</title>
<meta charset="UTF-8" />
<link rel="stylesheet" href="/autoindex/style.css" />
</head>
<body>
<ul id="title">{title}</ul>
<table id="myTable" class="tablesorter">
	<thead>
		<tr>
			<th class="header">Type</th>
			<th class="header">Name</th>
			<th class="header">Date modified</th>
			<th class="header">Size</th>
		</tr>
	</thead>
	{data}
</table>

<div id="footer">
	Powered by <a href="https://github.com/defool/autoindex">autoindex</a>.
</div>
<script src="/autoindex/jquery.js"></script>
<script src="/autoindex/script.js"></script>
</body>
</html>
"""

tpl_data = """<tr>
<td>{type}</td><td><a href="{href}">{name}</a></td><td>{mtime}</td><td>{size}</td>
</tr>"""

def format_data(content, data):
	rows = ''.join(tpl_data.format(**d) for d in data)
	return tpl_page.format(data=rows, **content)

if __name__ == '__main__':
	print locals()