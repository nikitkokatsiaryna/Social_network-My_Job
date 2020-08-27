export default class extends Stimulus.Controller {

    createEducation() {
        $.ajax({
            type: 'post',
            url: '/education/',
            success: (response) => {
                debugger
                this.element.outerHTML = response
            },
            error: (xhr, errmsg, err) => {
                toastr.error(errmsg)
            },
        })
    }

}