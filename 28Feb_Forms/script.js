$(document).ready(function(){

function init(){
  $(".free").hide();
  $(".multiple").hide();
};

init();

    $('.header').click(function(){
        $(this).toggle();
    })

    $('#one').click(function(){
        $('#Q_one').toggle();
    });




    $('#single').click(function(){
      $(".single").show();
      $(".free").hide();
      $(".multiple").hide();
    });

    $('#multiple').click(function(){
        $(".single").hide();
        $(".free").hide();
        $(".multiple").show();
    });

    $('#free').click(function(){
        $(".single").hide();
        $(".free").show();
        $(".multiple").hide();
    });





    $('#two').click(function(){
        $('#Q_two').toggle();
    });

    $('#three').click(function(){
        $('#Q_three').toggle();
    });

    $('#four').click(function(){
        $('#Q_four').toggle();
    });





});
