// document.getElementById('button').addEventListener('click', function () {
//     document.querySelector('.modal').style.display = 'flex'
// });
//
// document.querySelector('.modal-close').addEventListener('click', function () {
// document.querySelector('.modal').style.display = 'none'
// })

$('#experienceForm').on('submit', (event) => {
    event.preventDefault();
    event.stopPropagation();
    const form = event.currentTarget;


    $.ajax({
        type: form.method,
        url: form.action,
        data: $(event.currentTarget).serialize(),
        success: (response) => {
            $('#experienceModal .modal-body').html(response);
            toastr.success('Successfully created.')
            $(".modal-close").trigger("click");
            $('.modal').fadeOut();
        },

        error: (xhr, errmsg, err) => {
            toastr.error(errmsg)
        },
    });
});


$('#educationForm').on('submit', (event) => {
    event.preventDefault();
    event.stopPropagation();
    const form = event.currentTarget;

    $.ajax({
        type: form.method,
        url: form.action,
        data: $(event.currentTarget).serialize(),
        success: (response) => {
            $('#educationModal .modal-body').html(response);
            toastr.success('Successfully created.')
            $(".modal-close").trigger("click");
            $('.modal').fadeOut();
        },
        error: (xhr, errmsg, err) => {
            toastr.error(errmsg)
        },
    });
});

// $.ajax({
//         type: 'patch',
//         url: '/sdasdasd/sadasd/'
//     }).done(() => {
//         asdasd
//     }).error((response) => {
//         asdfasdf
//     })
