$(function(){
    $('.selectpicker').selectpicker();
	$('select.selectpicker').on('change', function (e) {
		var selected = $('.selectpicker option:selected').val();
		var lang;
		if (selected == 'Russian'){
			lang = 'ru'
		} else {
			lang = 'en'
		}
		
		var regex = /\/\w{2}\//g;
		var url = window.location.href; 
		var replaced = url.search(regex) >= 0;
		if(replaced){
		    new_url = url.replace(regex, '/' + lang + '/');
		} else {
			new_url = url + lang;
		}
		window.location.href = new_url;
		
	});

});

