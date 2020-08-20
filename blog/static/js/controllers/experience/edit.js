export default class extends Stimulus.Controller {

    updateForm() {
        let experienceId = this.element.dataset.experienceId

        $.ajax({
            type: 'PATCH',
            url: `/experiences/${experienceId}/`,
            success: (response) => {
                debugger
                this.element.outerHTML = response
            }
        })
    }
}