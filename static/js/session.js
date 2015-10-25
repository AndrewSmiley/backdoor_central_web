/**
 * Created by Andrew on 10/25/15.
 */
    function getCoursesInSemester(){
    $.ajax({
        url : "/ajax_handler/get_courses_in_semester/",
        type: "post",
        data : {
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
            'semester_name' : $('#semester').find(":selected").text()

        },
        dataType: "html",
        success: function(data, textStatus, jqXHR){
            //try to append the html data recieved
            console.log(data)
            $("#course").html(data);
            getVmsInCourse();
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
            alert("Unable to get courses in semester.")

        }

    });
}

function getVmsInCourse(){
    $.ajax({
        url : "/ajax_handler/get_vms_in_course/",
        type: "post",
        data : {
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
            'course_name' : $('#course').find(":selected").text()

        },
        dataType: "html",
        success: function(data, textStatus, jqXHR){
            //try to append the html data recieved
            console.log(data)
            $("#virtual_machine").html(data);

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