/////////////////////////
// jsvaScript for post page
////////////////////////

$(function(){
    // Excuted when js-menu-icon js clicked
    $('.js-menu-icon').click(function(){
      // $(this) : self element, namely div.js-menu-icon
      // next() : Next to div.js-menu-icon, namly div.menu
      //toggle() : Switched show and hide
        $(this).next().toggle();
    })
})