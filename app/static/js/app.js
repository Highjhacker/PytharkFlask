$(document).ready(function() {
    // Permet de fermer un toast en cliquant sur la croix
    $('#toast-container .toast').click(function(){
        $(this).fadeOut(function(){
           $(this).remove();
        });
    });
}); // end of document ready
