// function spin(message){

//     var $msgElement = document.createElement( "div" );
//            $msgElement.innerHTML = "<i class='fa fa-spinner fa-spin '></i><h3>"+message+"</h3>"
//             dndod.popup( {
//                 msg: $msgElement,
//                 handler: function ( e, popup ) {
//                     popup.close()
//                 }
              
//               });
//               setTimeout((popup)=>{
//                 popup.close()
//                },3000)
           
//    }


$(document).ready(()=>{
    
    //login function
    function note(text){
        dndod.alert(text);
    }

     $('#login').click(()=>{
        var email=$('#exampleInputEmail3').val();
        var pass=$('#exampleInputPassword3').val();
         if(email===''||email==null){
             note('email cant be empty');
         }else if(pass==''||pass==null){
             note('Please enter the password')
         }

         else{
             $.ajax({
                 url:'/login',
                 method:'POST',
                 data:{
                     log:1,
                     email:email,
                     pass:pass

                 },
                 success:(data)=>{
                    reply=JSON.parse(data);
                    if(reply.info==='success'){
                        window.location.href=reply.msg;

                    }else(
                        note(reply.msg)
                    );

                 },
                 error:(error)=>{
                   
                     note('cannot communicate to the server for som reasons. Please check your internet connection and try again ')

                 }


             })
         }
     })

     $('.reg').click(()=>{
         
        var email=$('#em').val();
        var pass1=$('.p1').val();
        var pass2=$('.p2').val();
        var fname=$('#fname').val();
        var lname=$('#lname').val();
        var id=$('#id').val();
        var phone=$('#tel').val();
        var gender=$('#gender').val();
        var address=$('#addr').val();

        
       if(fname==''||fname==null){
             note('please enter the first name');
         }else if(lname==''||lname==null){
             note('please fill in the last name')
         }else if(id==''||id==null){
             note('please enter the your id')
         }else if(email===''||email==null){
            note('email cant be empty');
        }  else if(pass2==''||pass1==null){
            note('Please enter the password')
        }
         else if(phone==''||phone==''){
             note('plaease fill in your phone number')
         }else if(gender==''){
             note('please select your gender')
         }else if (address==''||address==null){
             note('please enter your address')
         }else if (pass1 !=pass2){
            note('password dont match')
        }

         else{
             $.ajax({
                 url:'register_user',
                 method:'post',
                 data:{
                     reg:1,
                     email:email,
                     pass:pass1,
                     fname:fname,
                     lname:lname,
                     id:id,
                     phone:phone,
                     gender:gender,
                     address:address
                 },
                 success:(data)=>{
                    reply=JSON.parse(data);
                    if(reply.info==='success'){
                        window.location.href=reply.msg;

                    }else(
                        note(reply.msg)
                    )
                    

                 },
                 error:()=>{
                   
                     note('cannot communicate to the server for som reasons. Please check your internet connection and try again')

                 }


             })
         }
     })

    //end of login func


    //start of make request

    $('.del').click(()=>{
        p_number=$('#parcel_no').val();
        p_location=$('#pick_loc').val();
        mpesa_code=$('#mpesa').val();
        delivery_method=$('#method').val();
        preference=$('#comment').val();
        if(p_number==''){
            note('Please provide your percel number')
        }else if(p_location==''){
            note('Please provide the pickup location')
        }
        else if(mpesa_code==''){
            note('Provide the payment code')
        }
        else if(delivery_method==''){
            note('select your prefeered delivery method')
        }
        else if(preference==''){
            note('Please provide a belief explanation of how you would like the parcel to be handled')
            
        }else{
            $.ajax({
                method:'post',
                url:'php/requests.php',
                data:{
                    get:1,
                    parcel:p_number,
                    mpesa_code:mpesa_code,
                    delivery:delivery_method,
                    preferencce:preference,
                    location:p_location,
                    client_id:client_id

                },
                success:(data)=>{
                    rep=JSON.parse(data)
                    note(rep.msg)


                }
            })
        }

    })
})


// function get_user_pending(){
//     $.ajax({
//         method:'post',
//         url:'php/requests.php',
//         data:{
//             pending:1,
//             client_id:client_id
//         },
//         success:(data)=>{
//             rep=JSON.parse(data);
//             for(i=0;i<rep.length;i++){
//             $('#pending tbody').append("<tr><td>"+(i+1)+"</td><td>"+rep[i].parcel_no+"</td><td>"+rep[i].destination+"</td><td>"+rep[i].pkup_location+"</td><td>"+rep[i].status+"</td><td>"+rep[i].delively_method+"</td><td><button class='btn btn-primary'>edit</button></td></tr>")
//             }
//         }
//     })
// }
// get_user_pending();


// function get_admin_pending(){
//     $.ajax({
//         method:'post',
//         url:'php/requests.php',
//         data:{
//             admin_pending:1,
//             client_id:client_id
//         },
//         success:(data)=>{
//             rep=JSON.parse(data);
//             for(i=0;i<rep.length;i++){
//             $('#admin_pending tbody').append("<tr><td>"+(i+1)+"</td><td>"+rep[i].parcel_no+"</td><td>"+rep[i].destination+"</td><td>"+rep[i].pkup_location+"</td><td>"+rep[i].status+"</td><td>"+rep[i].delively_method+"</td><td><button class='btn btn-primary' onclick='assign_driver("+rep[i].client_id+","+rep[i].booking_id+")'>verify</button></td></tr>")
//             }
//         }
//     })

//     setTimeout(()=>{
//         $('#admin_pending tbody ').empty()
//         get_admin_pending();
//     },8000
//     )
// }
// get_admin_pending();






///verify and assign customer to adriver
function assign_driver(client_id,booking_id){
    function notice( text ) {
        dndod.alert( text );
    }
   
   
       
        
            var $msgElement = document.createElement( "div" );
            
            $msgElement.innerHTML = "<div class='container' style='width:800px;'><h3 class='primary'>Assign Driver</H3><br><div class='col-md-4'><form><label >Driver</label><br>&nbsp<select class='form-control sel_driver' id='sel_driver'><option value=''>Select driver</option></select><br><label >Vehicle</label><br>&nbsp<select class='form-control sel_vehicle' id='sel_vehicle'><option value=''>Select vehicle</option></select><br><br></form></div><div class='col-md-8'><h4>vehicle description</h4><br><table id='vhcle' class='table table-bordered table-striped'><thead><tr><td>Plate number</td><td>Type</td><td>class</td><td>capacity</td><td>other specs</td></tr><thead><tbody><tbody></table></div></div>"
         
    
             dndod.popup( {
                 msg: $msgElement,
                 buttons: [ {
                         text: "Close",
                         handler: function ( e, popup ) {
                             popup.close()
                         }
                     },
                     {
                         text: "Assign",
                         type: "info",
                         handler: function ( e, popup ) {
                             driver = $( '#sel_driver' ).val()
                             vehicle=$('.sel_vehicle').val()
    
    
                             if ( driver === '' ||driver==null) {
                                 notice( 'Please select the driver' );
    
                              } else if ( vehicle === ''|| vehicle==null ) {
                                 notice( 'Please select transport vehicle' )
    
                            //  } else if (pass!=conf_pass)
                            //  {
                            //     notice('Passwords dont match!') 
                            //  }else if ( pass.length < 7 ) {
                            //      notice( 'Password too short. Enter a password that has 7 or mor e characters' )
                             } else {
    
    
    
                                $.ajax({
                                    method:'post',
                                    url:'php/requests.php',
                                    data:{
                                        assign_driver:1,
                                        client_id:client_id,
                                        booking_id:booking_id,
                                        driver:driver,
                                        v_id:vehicle
                                    },
                                    success:(data)=>{
                                        rep=JSON.parse(data);
                                        popup.close();
                                       notice(rep.msg)
                                    }
                                })
    
    
                             }
                         }
                     }
                 ]
             } );

             $.ajax({
                method:'post',
                url:'php/requests.php',
                data:{
                    drivervehicle:1
                   
                },
                success:(data)=>{
                    rep=JSON.parse(data);
                    for(i=0;i<rep[0].length;i++){
                        $('#sel_driver').append("<option value="+rep[0][i].staff_id+">"+rep[0][i].fullname+"</option>")

                    }
                    for(i=0;i<rep[1].length;i++){
                        $('#sel_vehicle').append("<option value="+rep[1][i].vehicle_id+">"+rep[1][i].regno+"</option>")

                    }
                   
                }
            })


 click_count=0;  
$(document.body).on('change','#sel_vehicle',function(){ 
    if (click_count>0){
       
        $('#vhcle tbody').empty();
        
    }click_count+=1;
     var id=$('#sel_vehicle').val();

       $.ajax({
            type:"POST",
            url:'php/requests.php',
            data:{
                vehicle:1,
                id:id
               
            },               
             success:function(reply){
                var rep=JSON.parse(reply)
                
            

                 $('#vhcle').append("<tr><td>"+rep[0]['regno']+"</td><td>"+rep[0]['model']+"</td><td>"+rep[0]['class']+"</td><td>"+rep[0]['misc']+"</td><td>"+rep[0]['misc']+"</td></tr")
                    
              
            //   $('tb').show();
          
             




},
error:function(){

notefy('','Failed! Check your internet connection and then try again')

}
})

});
        

         

///driver pending

// function get_driver_pending(){
//     $.ajax({
//         method:'post',
//         url:'php/requests.php',
//         data:{
//             driver_pending:1,
//             client_id:client_id
//         },
//         success:(data)=>{
//             rep=JSON.parse(data);
//             for(i=0;i<rep.length;i++){
//             $('#driver_pending tbody').append("<tr><td>"+(i+1)+"</td><td>"+rep[i].parcel_no+"</td><td>"+rep[i].destination+"</td><td>"+rep[i].pkup_location+"</td><td>"+rep[i].status+"</td><td>"+rep[i].delively_method+"</td><td><button class='btn btn-primary' onclick='confirm_delivery("+rep[i].client_id+","+rep[i].booking_id+")'>verify</button></td></tr>")
//             }
//         }
//     })

//     setTimeout(()=>{
//         $('#admin_pending tbody ').empty()
//         get_driver_pending();
//     },8000
//     )
// }
// get_driver_pending();
    
 



}