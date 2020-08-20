// document.getElementById('button').addEventListener('click', function () {
//     document.querySelector('.modal').style.display = 'flex'
// });
//
// document.querySelector('.modal-close').addEventListener('click', function () {
// document.querySelector('.modal').style.display = 'none'
// })

// $('#experienceForm').on('submit', (event) => {
//     event.preventDefault();
//     event.stopPropagation();
//     const form = event.currentTarget;
//
//
//     $.ajax({
//         type: form.method,
//         url: form.action,
//         data: $(event.currentTarget).serialize(),
//         success: (response) => {
//             $('#experienceModal .modal-body').html(response);
//             toastr.success('Successfully created.')
//             $(".modal-close").trigger("click");
//             $('.modal').fadeOut();
//         },
//
//         error: (xhr, errmsg, err) => {
//             toastr.error(errmsg)
//         },
//     });
// });
//
//
// $('#experienceUpdateForm').on('submit', (event) => {
//     event.preventDefault();
//     event.stopPropagation();
//     const form = event.currentTarget;
//
//
//     $.ajax({
//         type: form.method,
//         url: form.action,
//         data: $(event.currentTarget).serialize(),
//         success: (response) => {
//             $('#experienceUpdateModal .modal-body').html(response);
//             toastr.success('Successfully created.')
//             $(".modal-close").trigger("click");
//             $('.modal').fadeOut();
//         },
//
//         error: (xhr, errmsg, err) => {
//             toastr.error(errmsg)
//         },
//     });
// });

// $('#addExperience').on('click', (event) => {
//     $.ajax({
//         type: 'get',
//         url: '/experiences/new',
//         success: (response) => $('#modal .modal-body').html(response),
//         error: (xhr, errmsg, err) => toastr.error(errmsg),
//     });
// })

$('.experience').on('click', (event) => {
    let experienceId = event.currentTarget.dataset.id;

    $.ajax({
        type: 'get',
        url: `/experiences/${experienceId}/edit`,
        success: (response) => $('#modal .modal-body').html(response),
        error: (xhr, errmsg, err) => toastr.error(errmsg),
    });
})


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
