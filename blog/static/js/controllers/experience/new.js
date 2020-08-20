export default class extends Stimulus.Controller {

    createExperience() {
        $.ajax({
            type: 'post',
            url: '/experiences/',
            success: (response) => {
                debugger
                this.element.outerHTML = response
            },
            error: (response) => {
                // debugger
            },
        })
    }

}