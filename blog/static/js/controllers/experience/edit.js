export default class extends Stimulus.Controller {

    updateForm() {
        let experienceId = this.element.dataset.experienceId


        $.ajax({
            type: 'PATCH',
            url: `/experiences/${experienceId}/`,
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken')
            },


            success: (response) => {
                debugger
                toastr.success('Successfully created.')
                // this.element.outerHTML = response
            },
            error: (xhr, errmsg, err) => {
                debugger
                toastr.error(errmsg)
            },
        })
    }

    preDeleteObject() {
        let press

        $.ajax(
            press = confirm('Do you realy want to delete the form?'))
        if (press) {
            this.deleteObject()
        }
    }

    // async deleteObject() {
    //     let result = await Swal.fire({
    //         title: 'Are you sure?',
    //         text: "You won't be able to revert this!",
    //         icon: 'warning',
    //         showCancelButton: true,
    //         confirmButtonColor: '#3085d6',
    //         cancelButtonColor: '#d33',
    //         confirmButtonText: 'Yes, delete it!'
    //     })
    //     if (result.discard) return
    //
    //
    //     let experienceId = this.element.dataset.experienceId
    //
    //
    //     $.ajax({
    //         type: 'DELETE',
    //         url: `/experiences/${experienceId}/`,
    //         headers: {
    //             'X-CSRFToken': Cookies.get('csrftoken')
    //         },
    //
    //         success: (response) => {
    //             debugger
    //             toastr.success('Successfully deleted')
    //         },
    //         error: (xhr, errmsg, err) => {
    //             debugger
    //             toastr.error(errmsg)
    //         },
    //     })
    //
    //     Swal.fire(
    //         'Deleted!',
    //         'Your file has been deleted.',
    //         'success'
    //     )
    // }
}