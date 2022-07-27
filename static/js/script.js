//   Date Picker
<script language="javascript">
    $(document).ready(function () {
        $("#date_picker").datepicker({
            minDate: 0
        });
    });
</script>

// Function to make alerts disappear automatically
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);


$('#delete-modal').on('shown.bs.modal', function () {
    $('#reference_match').trigger('focus')
  })


