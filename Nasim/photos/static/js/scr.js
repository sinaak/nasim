    
$(window).scroll(function () {
                    var height = $('body').height();
                    var scrollTop = $(window).scrollTop();
    
                      if(scrollTop>2){
                          $('#header').css({ 'position': 'fixed', 'top' : '0' });
                    } 
    else{
        $('#header').css({ 'position': 'relative', 'top': '30px'});
    }
                }); 
