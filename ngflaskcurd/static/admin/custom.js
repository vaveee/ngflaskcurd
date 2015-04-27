



var keys = keys || function (o) { var a = []; for (var k in o) a.push(k); return a; };

/**

var slugify = function (string) {
	string='';

	var accents = "ãàáäâèéëêìíïîõòóöôùúüûñç";
	var without = "aaaaaeeeeiiiiooooouuuunc";
	
	var map = {'@': ' at ', '\u20ac': ' euro ',
	    '$': ' dollar ', '\u00a5': ' yen ',
	    '\u0026': ' and ', '\u00e6': 'ae', '\u0153': 'oe'};

  return string
    // Handle uppercase characters
    .toLowerCase()

    // Handle accentuated characters
    .replace(
      new RegExp('[' + accents + ']', 'g'),
      function (c) { return without.charAt(accents.indexOf(c)); })

    // Handle special characters
    .replace(
      new RegExp('[' + keys(map).join('') + ']', 'g'),
      function (c) { return map[c]; })

    // Dash special characters
    .replace(/[^a-z0-9]/g, '-')

    // Compress multiple dash
    .replace(/-+/g, '-')

    // Trim dashes
    .replace(/^-|-$/g, '');
};

**/