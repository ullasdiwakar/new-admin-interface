$(document).ready(function(){
    $('#delete-button').click(function(e){
        e.preventDefault();
        var searchIDs = $("#delete-items:checked").map(function(){return $(this).val();}).get();
        if (confirm("Are you sure?"))
        {
            $.ajax({
                method : 'POST',
                url : '/delete_entities',
                data : {'IDs[]' : searchIDs},
                dataType : 'json',
                success : function(data){
                    alert(data.message);
                    location.reload(true);
                }
            });
        }
    });
    $("#all-checked").click(function () {
        $('input:checkbox').not(this).prop('checked', this.checked);
    });
});