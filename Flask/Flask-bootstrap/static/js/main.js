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
	  	console.log(lang);

		var url = window.location.href; 

		// if (url.endsWith('/ru')){
		//    url += lang
		// }
		window.location.href = url + lang;

		// var stateObj = { foo: "bar" };
		// console.log(window.location.href)
		// location.replace('ru')
	});

});

