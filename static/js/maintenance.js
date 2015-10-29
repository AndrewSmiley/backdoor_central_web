/**
 * Created by pridemai on 10/28/15.
 */
function esxiCheckAlive(){
    $.ajax({
        url : "/ajax_handler/esxi_check_alive/",
        type: "get",
        data : {
  ////          'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
      //      'semester_name' : $('#semester').find(":selected").text()

        },
        dataType: "html",
        success: function(data, textStatus, jqXHR){
            //try to append the html data recieved
            alert(data);
            //console.log(data)
            //$("#course").html(data);
            //getVmsInCourse();
          //
          //  $("#scholarship_dialog").dialog({
          //      width: '600px',
          //      padding: '100px',
          //      //#height: '500px',
          //      autoOpen: false,
          //      show: {
          //          effect: "blind",
          //          duration: 1000
          //      },
          //      hide: {
          //          effect: "explode",
          //          duration: 1000
          //      }
          //  });
          //
          //  $("#registration_id").attr('value', registration_id)
          //$("#scholarship_dialog").dialog("open");


        }
,
            error: function(jqXHR, textStatus, errorThrown){
            alert("Unable to check status of ESXi Server")

        }

    });
}
