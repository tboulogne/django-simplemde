var inscrybmdeJQuery = null;

if (typeof jQuery !== 'undefined') {
  inscrybmdeJQuery = jQuery;
} else if (typeof django !== 'undefined') {
  //use jQuery come with django admin
  inscrybmdeJQuery = django.jQuery
} else {
  console.error('cant find jQuery, please make sure your have jQuery imported before this script');
}

if (!!inscrybmdeJQuery) {
  inscrybmdeJQuery(function() {
    inscrybmdeJQuery.each(inscrybmdeJQuery('.inscrybmde-box'), function(i, elem) {
      var options = JSON.parse(inscrybmdeJQuery(elem).attr('data-inscrybmde-options'));
      options['element'] = elem;
      var inscrybmde = new InscrybMDE(options);
      elem.InscrybMDE = inscrybmde;
    });
  });
}