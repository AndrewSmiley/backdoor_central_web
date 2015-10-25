/**
 * Created by Andrew on 10/25/15.
 */
    function getFilesInFolder(){
    $.ajax({
        url : "/ajax_handler/get_files_for_search/",
        type: "get",
        data : {
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
            'folder' : $('.folder').find(":selected").text()

        },
        dataType: "html",
        success: function(data, textStatus, jqXHR){
            //try to append the html data recieved
            console.log(data)
            $(".files_div").html(data);
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
            alert("Unable to fetch scholarship form. Please try again or contact the site administrators.")

        }

    });
}