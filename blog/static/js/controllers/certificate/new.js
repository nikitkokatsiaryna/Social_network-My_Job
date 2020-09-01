export default class extends Stimulus.Controller {

    async createCertificate() {
        $.ajax({
            type: 'post',
            url: '/certificate/',
            success: (response) => {
                Swal.fire(
                    'Created!',
                    'Your certificate has been created.',
                    'success'
                );
            },
            error: (response) => {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong!',
                })
            },
        })
    }

}