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
            url: '/skill/new',
            success: (response) => {
                this.getController('modal').element.innerHTML = response
            }
        })
    }

    editForm(event) {
        let skillId = event.currentTarget.dataset.id;

        $.ajax({
            type: 'get',
            url: `/skill/${skillId}/edit/`,
            success: (response) => {
                // debugger
                this.getController('modal').element.innerHTML = response
            },
            error: (response) => {
                // debugger
            },
        })
    }


    async deleteObject(event) {
        let result = await Swal.fire({
            title: 'Are you sure?',
            text: "Do you realy want to delete this education?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        })
        if (result.dismiss) return


        let skillId = $(event.target).closest('[data-id]').data('id')


        $.ajax({
            type: 'DELETE',
            url: `/skill/${skillId}/`,
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken')
            },

            success: (response) => {
                this.load()
            },
            error: (responce) => {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong!',
                })
            },
        })
    }

}