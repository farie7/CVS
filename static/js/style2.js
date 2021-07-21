    $(document).ready(function() {
        $("#payment").change(function() {
            if ($("#payment").val() == 'ECOCASH') {
                console.log("this is ecocash")
                $("#hidden-panel1").show()
            } else if  ($("#payment").val() == 'ONEMONEY') {
                console.log("this is onemoney")
                $("#hidden-panel1").show()}
                else {
                console.log("this is bank")
                $("#hidden-panel1").hide()
            }
        })
    });

