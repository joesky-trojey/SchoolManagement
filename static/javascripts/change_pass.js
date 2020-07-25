function notice( text ) {
    dndod.alert( text );
}
$( '#chg_psw' ).click(
    
    function ()
    {
        var $msgElement = document.createElement( "div" );
        $msgElement.innerHTML = "<div class='container' style='width:500px;'><h3 class='primary'>Change your password</H3><br><form><label >New password</label><br>&nbsp<input class='form-control psd' type='password' placeholder='enter new password.' ><br><label >Confirm new password</label><br>&nbsp<input class='form-control psd_c' type='password' placeholder='enter the password to confirm' ><br></form></div>"

         dndod.popup( {
             msg: $msgElement,
             buttons: [ {
                     text: "Close",
                     handler: function ( e, popup ) {
                         popup.close()
                     }
                 },
                 {
                     text: "Change",
                     type: "info",
                     handler: function ( e, popup ) {
                         pass = $( '.psd' ).val()
                         conf_pass = $( '.psd_c' ).val();
                         


                         if ( pass === '' ||pass==null) {
                             notice( 'password cannot be empty' );

                         } else if ( conf_pass === ''|| conf_pass==null ) {
                             notice( 'Please confirm your password' )

                         } else if (pass!=conf_pass)
                         {
                            notice('Passwords dont match!') 
                         }else if ( pass.length < 7 ) {
                             notice( 'Password too short. Enter a password that has 7 or mor e characters' )
                         } else {



                             $.ajax( {
                                 url: 'server/change_password.php',
                                 method: 'post',
                                 data: {
                                     'pass': 1,
                                     'conf_pass': pass,
                                     'type':session,
                                     'uname':uname

                                 },

                                 success: function ( received_data ) {
                                     rep = JSON.parse( received_data );
                                     notefy( rep.type, rep.msg );


                                 },
                                 error: function ( e ) {
                                     notice( 'Uh oh terrible erroh has occured....failed to submit data' )

                                 }

                             } )


                         }
                     }
                 }
             ]
         } );
    }
    
)