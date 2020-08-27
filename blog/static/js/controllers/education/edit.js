export default class extends Stimulus.Controller {

    updateForm() {
        let educationId = this.element.dataset.experienceId

        $.ajax({
            type: 'PATCH',
            url: `/education/${educationId}/`,
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken')
            },

            success: (response) => {
                debugger
                this.element.outerHTML = response
            },
            error: (xhr, errmsg, err) => {
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

    deleteObject() {
        let educationId = this.element.dataset.experienceId


        $.ajax({
            type: 'DELETE',
            url: `/education/${educationId}/`,
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken')
            },

            success: (response) => {
                toastr.success('Successfully deleted')
            },
            error: (xhr, errmsg, err) => {
                toastr.error(errmsg)
            },
        })
    }
}