export default class extends Stimulus.Controller {

    async reateExperience() {
        $.ajax({
            type: 'post',
            url: '/experiences/',
            success: (response) => {
                Swal.fire(
                    'Created!',
                    'Your education has been created.',
                    'success'
                );

            },
            error: (xhr, errmsg, err) => {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong!',
                })
            },
        })
    }

}