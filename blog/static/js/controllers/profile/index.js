import BaseController from '../base.js'

export default class extends BaseController {

    static targets = ["name"]

    connect() {
        if (this.element.dataset.load === 'true') {
            this.load()
            return
        }
    }

    loadForm() {
        $.ajax({
            type: 'get',
            url: '/profile/new',
            success: (response) => {
                this.getController('modal').element.innerHTML = response
            }
        })
    }

    editForm(event) {
        let profileId = event.currentTarget.dataset.id;

        $.ajax({
            type: 'get',
            url: `/profile/${profileId}/edit/`,
            success: (response) => {
                // debugger
                this.getController('modal').element.innerHTML = response
            },
            error: (response) => {
                // debugger
            },
        })
    }
}
