$(document).ready(function(){
    $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get('/art_likes/', {article_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
           });    
        });
    
    });