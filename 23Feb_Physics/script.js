$(document).ready(function(){

var speed=[0, 0];
var pos =[0, 0];
var dirX =1;
var dirY = 1;



function odo(){$('.log').html( speed +'   '+ pos + '  |') };
odo();

function set(){$('.elem').css({"left": pos[0], "top":pos[1]}); odo() };
function init(){pos = [5, 275];speed=[4,1];set()};

init();

$("#one").click(function(){ speed[0]+=1; odo() });
$("#two").click(function(){ speed[1]+=1; odo() });

function invertX() {  dirX*=(-1) };
function invertY() {  dirY*=(-1) };

function createMess() {
    $(".playScreen").append("<p class='elem'>t</p>")

};

function move(){
    for (i=0;i<=speed[0];i++)
      if (pos[0]<=0)        {invertX(); pos[0]+=5; set(); odo();red();}
      else if(pos[0]>=290)  {invertX(); pos[0]-=5; set(); odo();red();}
      else                  {(pos[0]+=(5*dirX));set();odo(); red();


      };

  for (i=0;i<=speed[1];i++)
      if (pos[1]<=0)         {invertY(); pos[1]+=5; set(); odo();red();}
      else if(pos[1]>=280)   {invertY() ; pos[1]-=5; set(); odo();red();}
      else                   {(pos[1]-=(5*dirY));set();odo(); red()}

  };

function red(){$('.elem').toggleClass('red');};

var nul = setInterval(function(){ move(); }, 100);






$('#three').click(function()  {   setInterval(function(){ move(); }, 100);  });
$('#four').click(function()   {   clearInterval(nul);  });

$('.iconMenu').click(function(){
    $('.sideBar').toggle("show");
    });

$('.rightBox').click(function(){ location.reload();  });


});
