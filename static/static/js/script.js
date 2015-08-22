var hostname=window.location.origin;
$('.word-btn').click(function(){
	$('.search-result').hide();
	$('.word-canvas').show();
	$('.word-canvas #word').text($(this).find('.word').text());
	$('.word-canvas #description').text($(this).find('.description').text());
	$("#buzzer").attr("src",$(this).attr('data-audio') );
	$("#bookmark").removeClass('btn-success');
	$("#bookmark").addClass('btn-primary');
	var word=$("#word").text();
	//alert("http://127.0.0.1:8000/bookmark/check/?word="+$("#word").text());
	$.ajax({
	  url: hostname+"/bookmark/check/?word="+$("#word").text(),
	  beforeSend: function( xhr ) {
	    xhr.overrideMimeType( "text/plain; charset=x-user-defined" );
	  }
	}).done(function( data ) {
		data = $.parseJSON(data)
	   	if(data){
	   		//alert($("#word").text() + "  " + word);
			if($("#word").text()==word && data.status_type=="YES"){
				$("#bookmark").removeClass('btn-primary');
				$("#bookmark").addClass('btn-success');
			}
		}
	});
});

$('#search-word').keyup(function(e) {
    clearTimeout($.data(this, 'timer'));
    if (e.keyCode == 13)
      search(true);
    else
      $(this).data('timer', setTimeout(search, 10));
});
function search(force) {
    var existingString = $("#search-word").val();
    $('.word-table tbody tr').each(function(index, row)
	{
		var allCells = $(row).find('.word');
		if(allCells.length > 0)
		{
			var found = false;
			allCells.each(function(index, td)
			{
				var regExp = new RegExp(existingString, 'i');
				if(regExp.test($(td).text()))
				{
					found = true;
					return false;
				}
			});
			if(found == true)$(row).show();else $(row).hide();
		}
	});
}

var buzzer = $('#buzzer')[0];  

$('.play-music').click(function()  { 
    $('#buzzer')[0].play();    
    return false;    
});  

$('#bookmark').click(function(){
	$('.search-result').hide();
	var word=$("#word").text();
	var description=$("#description").text();
	var audio_url=$("#buzzer").attr('src');
	//alert("http://127.0.0.1:8000/bookmark/create/?word="+word+"&description="+description+"&audio_url="+audio_url);
	$.ajax({
	  url: hostname+"/bookmark/create/?word="+word+"&description="+description+"&audio_url="+audio_url,
	  beforeSend: function( xhr ) {
	    xhr.overrideMimeType( "text/plain; charset=x-user-defined" );
	  }
	}).done(function( data ) {
	   	//alert(data);
	   	if(data){
			if($("#word").text()==word){
				$("#bookmark").removeClass('btn-primary');
				$("#bookmark").addClass('btn-success');
			}
		}
	});
});

$("#clear-bookmark").click(function(){
	$('.search-result').hide();
	if(confirm("Do you want to remove all bookmarked data?")){
		$.ajax({
		  url: hostname+"/bookmark/clear/",
		  beforeSend: function( xhr ) {
		    xhr.overrideMimeType( "text/plain; charset=x-user-defined" );
		  }
		}).done(function( data ) {
		   	data = $.parseJSON(data)
		   	if(data){
		   		//alert($("#word").text() + "  " + word);
				if(data.status_type=="YES"){
					//refresh
					location.reload(true);
				}
			}
		});
	}else{

	}
	return false;
});

$("#share").click(function(){
	alert("Comming Soon");
	return false;
});
