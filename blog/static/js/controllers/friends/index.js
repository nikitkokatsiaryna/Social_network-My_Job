export default class extends Stimulus.Controller {

    static targets = ["name"]

    connect() {
        if (this.element.dataset.load === 'true') {
            this.load()
            return
        }
    }

    load() {
        // let friendId = event.currentTarget.dataset.id;

        $.ajax({
            type: 'get',
            url: `/friend/`,
            success: (response) => {
                // debugger
                this.element.outerHTML = response
            },
            error: (response) => {
                // debugger
            },
        })
    }

    showFriend(event) {
        let friendId = event.currentTarget.dataset.id;

        $.ajax({
            type: 'get',
            url: `friend/${friendId}/show/`,
            success: (response) => {
                debugger
                this.element.outerHTML = response
            },
        })
    }

    // scroll() {
    //     $.ajax({
    //         type: 'get',
    //         url: `/connect/`,
    //         success: (response) => {
    //
    //         }
    //     })

}
