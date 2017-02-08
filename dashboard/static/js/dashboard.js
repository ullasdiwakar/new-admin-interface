$(document).ready(function(){
    $('#delete-button').click(function(e){
        e.preventDefault();
        var searchIDs = $("#delete-items:checked").map(function(){return $(this).val();}).get();
        $.ajax({
            method : 'POST',
            url : '/delete_entities',
            data : {'IDs[]' : searchIDs},
            dataType : 'json',
            success : function(data){
                alert(data.message);
            }
        });
        console.log(searchIDs);
    });
    $("#all-checked").click(function () {
        $('input:checkbox').not(this).prop('checked', this.checked);
    });
});