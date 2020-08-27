export default class extends Stimulus.Controller {

    createExperience() {
        $.ajax({
            type: 'post',
            url: '/experiences/',
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken')
            },
            success: (response) => {
                // # Не заходит сюда


                // debugger
                // this.element.outerHTML = response
                toastr.success('Successfully created.')

                // $('.modal').fadeOut();
            },
            error: (xhr, errmsg, err) => {
                toastr.error(errmsg)
            },
        })
    }

}